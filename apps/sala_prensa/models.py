from wagtail.core.models import Page
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from wagtail.core.blocks import (
    URLBlock
)

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailmedia.edit_handlers import MediaChooserPanel
from rest_framework.fields import Field

from .blocks import BaseStreamBlock, GalleryStreamBlock, SocialNetworksBlock
from ..common.models import Autor, Sector


class NoticiaAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the NoticiaPage below. This allows Autor to be added to a NoticiaPage.
    """
    page = ParentalKey(
        'NoticiaPage', related_name='noticia_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_noticia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class NoticiaSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the NoticiaPage below. This allows Sector to be added to a NoticiaPage.

    """
    page = ParentalKey(
        'NoticiaPage', related_name='noticia_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_noticia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class NoticiaPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the NoticiaPage object and tags.
    """
    content_object = ParentalKey(
        'NoticiaPage', related_name='tagged_items', on_delete=models.CASCADE)


class NoticiaPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la noticia',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen principal",
        help_text='Solo modo horizontal; ancho horizontal entre 1000px y 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Cuerpo de la noticia", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=NoticiaPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'noticia_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'noticia_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the NoticiaAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the noticia_autor_
        relationship directly we'd print `noticia.NoticiaAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.noticia_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the NoticiaPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the NoticiaSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the noticia_sector_
        relationship directly we'd print `noticia.NoticiaSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.noticia_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.noticia_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.noticia_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the noticia post into a list we can access on the template.
        """
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    def interesting_news(self):
        return NoticiaPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to NoticiaPage as being NoticiaIndexPages
    parent_page_types = ['NoticiaIndexPage']

    # Specifies what content types can exist as children of NoticiaPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),

    ]


class NoticiaIndexPage(RoutablePageMixin, Page):

    # Speficies that only NoticiaPage objects can live under this index page
    subpage_types = ['NoticiaPage']

    # Defines a method to access the children of the page (e.g. NoticiaPage
    # objects).
    def children(self):
        return NoticiaPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(NoticiaIndexPage, self).get_context(request)
        context['posts'] = NoticiaPage.objects.descendant_of(
            self).live().order_by('-date_published')[:50]
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child NoticiaPage objects for this NoticiaPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = NoticiaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this NoticiaPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class GaleriaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'GaleriaPage', related_name='galeria_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_galeria_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class GaleriaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'GaleriaPage', related_name='galeria_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_galeria_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class GaleriaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'GaleriaPage', related_name='tagged_items', on_delete=models.CASCADE)


class GaleriaPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la galeria',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen principal",
        help_text='Solo modo horizontal; ancho horizontal entre 1000px y 3000px.'
    )
    body = StreamField(
        GalleryStreamBlock(), verbose_name="Imágenes de la galería", blank=False, min_num=1, max_num=10
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=GaleriaPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'galeria_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'galeria_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.galeria_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.galeria_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.galeria_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.galeria_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['GaleriaIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),

    ]


class GaleriaIndexPage(RoutablePageMixin, Page):

    subpage_types = ['GaleriaPage']

    def children(self):
        return GaleriaPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(GaleriaIndexPage, self).get_context(request)
        context['posts'] = GaleriaPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = GaleriaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class InfografiaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaPage', related_name='infografia_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_infografia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class InfografiaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaPage', related_name='infografia_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_infografia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class InfografiaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'InfografiaPage', related_name='tagged_items', on_delete=models.CASCADE)


class InfografiaPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la infografía',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Infografía",
        help_text='Solo modo cuadrado; ancho horizontal entre 1080px y 1080px.'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=InfografiaPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'infografia_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'infografia_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.infografia_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.infografia_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.infografia_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.infografia_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['InfografiaIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-350x350-c50', source='image')),

    ]


class InfografiaIndexPage(RoutablePageMixin, Page):

    subpage_types = ['InfografiaPage']

    def children(self):
        return InfografiaPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(InfografiaIndexPage, self).get_context(request)
        context['posts'] = InfografiaPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = InfografiaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class VideosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'VideosPage', related_name='videos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_videos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class VideosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'VideosPage', related_name='videos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_videos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class VideosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'VideosPage', related_name='tagged_items', on_delete=models.CASCADE)


class VideosPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el video',
        blank=False,
        verbose_name="Introducción",)
    link_video = models.URLField(
        "Video", blank=False, help_text='El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=VideosPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        FieldPanel('link_video'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'videos_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'videos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.videos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.videos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.videos_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.videos_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['VideosIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('link_video'),

    ]


class VideosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['VideosPage']

    def children(self):
        return VideosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(VideosIndexPage, self).get_context(request)
        context['posts'] = VideosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = VideosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class AudioAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'AudioPage', related_name='audio_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_audio_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class AudioSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'AudioPage', related_name='audio_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_audio_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class AudioPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'AudioPage', related_name='tagged_items', on_delete=models.CASCADE)


class AudioSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the audio URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class AudioPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el audio',
        blank=False,
        verbose_name="Introducción",)
    audio = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=AudioPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        MediaChooserPanel('audio'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'audio_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'audio_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.audio_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.audio_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.audio_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.audio_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['AudioIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('audio', AudioSerializedField()),

    ]


class AudioIndexPage(RoutablePageMixin, Page):

    subpage_types = ['AudioPage']

    def children(self):
        return AudioPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(AudioIndexPage, self).get_context(request)
        context['posts'] = AudioPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = AudioPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class DocumentoAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'DocumentoPage', related_name='documento_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_socumento_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class DocumentoSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'DocumentoPage', related_name='documento_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_documento_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class DocumentoPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'DocumentoPage', related_name='tagged_items', on_delete=models.CASCADE)


class DocumentoSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Documento URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class DocumentoPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el documento',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen del documento",
        help_text='Imagen de presentación para el documento'
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="Documento",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=DocumentoPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        DocumentChooserPanel('document_file'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'documento_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'documento_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.documento_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.documento_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.documento_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.documento_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['DocumentoIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', DocumentoSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class DocumentoIndexPage(RoutablePageMixin, Page):

    subpage_types = ['DocumentoPage']

    def children(self):
        return DocumentoPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(DocumentoIndexPage, self).get_context(request)
        context['posts'] = DocumentoPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = DocumentoPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class EventoAutorRelationship(Orderable, models.Model):
    page = ParentalKey(
        'EventoPage', related_name='evento_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_evento_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class EventoSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'EventoPage', related_name='evento_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_evento_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class EventoPageTag(TaggedItemBase):

    content_object = ParentalKey(
        'EventoPage', related_name='tagged_items', on_delete=models.CASCADE)


class EventoPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe elvento',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen principal",
        help_text='Solo modo horizontal; ancho horizontal entre 1000px y 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Cuerpo del evento", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=EventoPageTag, blank=False)
    date_published = models.DateField(
        "Fecha del evento", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'evento_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'evento_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):

        authors = [
            n.autor for n in self.evento_autor_relationship.all()
        ]

        return authors

    def sectors(self):

        sectors = [
            n.sector for n in self.evento_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.evento_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.evento_autor_relationship.all()
        ]

    @property
    def get_tags(self):

        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    # Specifies parent to EventoPage as being EventoIndexPages
    parent_page_types = ['EventoIndexPage']

    # Specifies what content types can exist as children of EventoPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),

    ]


class EventoIndexPage(RoutablePageMixin, Page):

    subpage_types = ['EventoPage']

    def children(self):
        return EventoPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(EventoIndexPage, self).get_context(request)
        context['posts'] = EventoPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = EventoPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class prensaPage(Page):

    subpage_types = ['InfografiaIndexPage', 'GaleriaIndexPage', 'NoticiaIndexPage',
                     'VideosIndexPage', 'AudioIndexPage', 'DocumentoIndexPage', 'EventoIndexPage']
    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de noticias',
        verbose_name='Índice de noticias'
    )

    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    gallery_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    gallery_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de galeria',
        verbose_name='Índice de galeria'
    )

    gallery_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    infographics_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    infographics_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de infografías',
        verbose_name='Índice de infografías'
    )

    infographics_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    videos_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    videos_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de videos',
        verbose_name='Índice de videos'
    )

    videos_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    audios_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    audios_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de videos',
        verbose_name='Índice de audios'
    )

    audios_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    documents_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    documents_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de documentos',
        verbose_name='Índice de documentos'
    )

    documents_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    events_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    events_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de eventos',
        verbose_name='Índice de eventos'
    )

    events_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    podcast_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    podcast_iframe_url = models.URLField(
        verbose_name="URL iframe Podcats",
        blank=True,
        max_length=2000,
        help_text='URL iframe Podcats'
    )

    podcast_url = models.URLField(
        verbose_name="Link a página de podcast",
        blank=True,
        help_text='Link a página de podcast'
    )

    podcats_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    social_networks_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    social_networks = StreamField(
        [('Red', SocialNetworksBlock())], blank=True, verbose_name="Redes Sociales")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('news_list_title'), PageChooserPanel('news_list'), FieldPanel('news_button_title'), ]),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('gallery_list_title'), PageChooserPanel('gallery_list'), FieldPanel('gallery_button_title'), ]),
        ], heading="Galeria", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('infographics_list_title'), PageChooserPanel('infographics_list'), FieldPanel('infographics_button_title'), ]),
        ], heading="Infografías", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('videos_list_title'), PageChooserPanel('videos_list'), FieldPanel('videos_button_title'), ]),
        ], heading="Videos", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('audios_list_title'), PageChooserPanel('audios_list'), FieldPanel('audios_button_title'), ]),
        ], heading="Audios", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('documents_list_title'), PageChooserPanel('documents_list'), FieldPanel('documents_button_title'), ]),
        ], heading="Presentaciones", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('events_list_title'), PageChooserPanel('events_list'), FieldPanel('events_button_title'), ]),
        ], heading="Eventos", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('podcast_list_title'), FieldPanel('podcast_iframe_url'), FieldPanel('podcast_url'), FieldPanel('podcats_button_title'), ]),
        ], heading="Podcast", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('social_networks_title'), StreamFieldPanel('social_networks')]),
        ], heading="Redes Sociales", classname="collapsible"),
    ]
