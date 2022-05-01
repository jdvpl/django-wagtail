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

from ..common.models import Autor, Sector
from ..sala_prensa.blocks import BaseStreamBlock


class CapacidadAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the CapacidadPage below. This allows Autor to be added to a CapacidadPage.
    """
    page = ParentalKey(
        'CapacidadPage', related_name='capacidad_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_capacidad_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class CapacidadSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the CapacidadPage below. This allows Sector to be added to a CapacidadPage.

    """
    page = ParentalKey(
        'CapacidadPage', related_name='capacidad_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_capacidad_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class CapacidadPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the CapacidadPage object and tags.
    """
    content_object = ParentalKey(
        'CapacidadPage', related_name='tagged_items', on_delete=models.CASCADE)


class CapacidadPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la capacidad',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la capacidad", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=CapacidadPageTag, blank=False)
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
            'capacidad_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'capacidad_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the CapacidadAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the capacidad_autor_
        relationship directly we'd print `capacidad.CapacidadAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.capacidad_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the CapacidadPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the CapacidadSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the capacidad_sector_
        relationship directly we'd print `capacidad.CapacidadSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.capacidad_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.capacidad_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.capacidad_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the capacidad post into a list we can access on the template.
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
        return CapacidadPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to CapacidadPage as being CapacidadIndexPages
    parent_page_types = ['CapacidadIndexPage']

    # Specifies what content types can exist as children of CapacidadPage.
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


class CapacidadIndexPage(RoutablePageMixin, Page):

    # Speficies that only CapacidadPage objects can live under this index page
    subpage_types = ['CapacidadPage']

    # Defines a method to access the children of the page (e.g. CapacidadPage
    # objects).
    def children(self):
        return CapacidadPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(CapacidadIndexPage,
                        self).get_context(request)
        context['posts'] = CapacidadPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child CapacidadPage objects for this CapacidadPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = CapacidadPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this CapacidadPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class ConstruccionAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the ConstruccionPage below. This allows Autor to be added to a ConstruccionPage.
    """
    page = ParentalKey(
        'ConstruccionPage', related_name='construccion_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_construccion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ConstruccionSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the ConstruccionPage below. This allows Sector to be added to a ConstruccionPage.

    """
    page = ParentalKey(
        'ConstruccionPage', related_name='construccion_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_construccion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ConstruccionPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the ConstruccionPage object and tags.
    """
    content_object = ParentalKey(
        'ConstruccionPage', related_name='tagged_items', on_delete=models.CASCADE)


class ConstruccionPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la construccion',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la construccion", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=ConstruccionPageTag, blank=False)
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
            'construccion_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'construccion_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the ConstruccionAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the construccion_autor_
        relationship directly we'd print `construccion.ConstruccionAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.construccion_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the ConstruccionPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the ConstruccionSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the construccion_sector_
        relationship directly we'd print `construccion.ConstruccionSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.construccion_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.construccion_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.construccion_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the construccion post into a list we can access on the template.
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
        return ConstruccionPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to ConstruccionPage as being ConstruccionIndexPages
    parent_page_types = ['ConstruccionIndexPage']

    # Specifies what content types can exist as children of ConstruccionPage.
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


class ConstruccionIndexPage(RoutablePageMixin, Page):

    # Speficies that only ConstruccionPage objects can live under this index page
    subpage_types = ['ConstruccionPage']

    # Defines a method to access the children of the page (e.g. ConstruccionPage
    # objects).
    def children(self):
        return ConstruccionPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(ConstruccionIndexPage,
                        self).get_context(request)
        context['posts'] = ConstruccionPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child ConstruccionPage objects for this ConstruccionPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = ConstruccionPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this ConstruccionPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class NuevosHogaresAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the NuevosHogaresPage below. This allows Autor to be added to a NuevosHogaresPage.
    """
    page = ParentalKey(
        'NuevosHogaresPage', related_name='nuevoshogares_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_nuevoshogares_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class NuevosHogaresSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the NuevosHogaresPage below. This allows Sector to be added to a NuevosHogaresPage.

    """
    page = ParentalKey(
        'NuevosHogaresPage', related_name='nuevoshogares_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_nuevoshogares_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class NuevosHogaresPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the NuevosHogaresPage object and tags.
    """
    content_object = ParentalKey(
        'NuevosHogaresPage', related_name='tagged_items', on_delete=models.CASCADE)


class NuevosHogaresPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la nuevoshogares',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la nuevoshogares", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=NuevosHogaresPageTag, blank=False)
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
            'nuevoshogares_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'nuevoshogares_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the NuevosHogaresAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the nuevoshogares_autor_
        relationship directly we'd print `nuevoshogares.NuevosHogaresAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.nuevoshogares_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the NuevosHogaresPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the NuevosHogaresSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the nuevoshogares_sector_
        relationship directly we'd print `nuevoshogares.NuevosHogaresSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.nuevoshogares_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.nuevoshogares_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.nuevoshogares_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the nuevoshogares post into a list we can access on the template.
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
        return NuevosHogaresPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to NuevosHogaresPage as being NuevosHogaresIndexPages
    parent_page_types = ['NuevosHogaresIndexPage']

    # Specifies what content types can exist as children of NuevosHogaresPage.
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


class NuevosHogaresIndexPage(RoutablePageMixin, Page):

    # Speficies that only NuevosHogaresPage objects can live under this index page
    subpage_types = ['NuevosHogaresPage']

    # Defines a method to access the children of the page (e.g. NuevosHogaresPage
    # objects).
    def children(self):
        return NuevosHogaresPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(NuevosHogaresIndexPage,
                        self).get_context(request)
        context['posts'] = NuevosHogaresPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child NuevosHogaresPage objects for this NuevosHogaresPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = NuevosHogaresPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this NuevosHogaresPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class MarcoNormativoAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the MarcoNormativoPage below. This allows Autor to be added to a MarcoNormativoPage.
    """
    page = ParentalKey(
        'MarcoNormativoPage', related_name='marconormativo_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_marconormativo_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class MarcoNormativoSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the MarcoNormativoPage below. This allows Sector to be added to a MarcoNormativoPage.

    """
    page = ParentalKey(
        'MarcoNormativoPage', related_name='marconormativo_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_marconormativo_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class MarcoNormativoPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the MarcoNormativoPage object and tags.
    """
    content_object = ParentalKey(
        'MarcoNormativoPage', related_name='tagged_items', on_delete=models.CASCADE)


class MarcoNormativoPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la marconormativo',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la marconormativo", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=MarcoNormativoPageTag, blank=False)
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
            'marconormativo_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'marconormativo_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the MarcoNormativoAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the marconormativo_autor_
        relationship directly we'd print `marconormativo.MarcoNormativoAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.marconormativo_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the MarcoNormativoPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the MarcoNormativoSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the marconormativo_sector_
        relationship directly we'd print `marconormativo.MarcoNormativoSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.marconormativo_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.marconormativo_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.marconormativo_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the marconormativo post into a list we can access on the template.
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
        return MarcoNormativoPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to MarcoNormativoPage as being MarcoNormativoIndexPages
    parent_page_types = ['MarcoNormativoIndexPage']

    # Specifies what content types can exist as children of MarcoNormativoPage.
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


class MarcoNormativoIndexPage(RoutablePageMixin, Page):

    # Speficies that only MarcoNormativoPage objects can live under this index page
    subpage_types = ['MarcoNormativoPage']

    # Defines a method to access the children of the page (e.g. MarcoNormativoPage
    # objects).
    def children(self):
        return MarcoNormativoPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(MarcoNormativoIndexPage,
                        self).get_context(request)
        context['posts'] = MarcoNormativoPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child MarcoNormativoPage objects for this MarcoNormativoPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = MarcoNormativoPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this MarcoNormativoPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class ImplementacionAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the ImplementacionPage below. This allows Autor to be added to a ImplementacionPage.
    """
    page = ParentalKey(
        'ImplementacionPage', related_name='implementacion_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_implementacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ImplementacionSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the ImplementacionPage below. This allows Sector to be added to a ImplementacionPage.

    """
    page = ParentalKey(
        'ImplementacionPage', related_name='implementacion_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_implementacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ImplementacionPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the ImplementacionPage object and tags.
    """
    content_object = ParentalKey(
        'ImplementacionPage', related_name='tagged_items', on_delete=models.CASCADE)


class ImplementacionPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la implementacion',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la implementacion", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=ImplementacionPageTag, blank=False)
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
            'implementacion_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'implementacion_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the ImplementacionAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the implementacion_autor_
        relationship directly we'd print `implementacion.ImplementacionAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.implementacion_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the ImplementacionPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the ImplementacionSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the implementacion_sector_
        relationship directly we'd print `implementacion.ImplementacionSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.implementacion_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.implementacion_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.implementacion_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the implementacion post into a list we can access on the template.
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
        return ImplementacionPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to ImplementacionPage as being ImplementacionIndexPages
    parent_page_types = ['ImplementacionIndexPage']

    # Specifies what content types can exist as children of ImplementacionPage.
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


class ImplementacionIndexPage(RoutablePageMixin, Page):

    # Speficies that only ImplementacionPage objects can live under this index page
    subpage_types = ['ImplementacionPage']

    # Defines a method to access the children of the page (e.g. ImplementacionPage
    # objects).
    def children(self):
        return ImplementacionPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(ImplementacionIndexPage,
                        self).get_context(request)
        context['posts'] = ImplementacionPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child ImplementacionPage objects for this ImplementacionPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = ImplementacionPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this ImplementacionPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class ReglamentacionAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the ReglamentacionPage below. This allows Autor to be added to a ReglamentacionPage.
    """
    page = ParentalKey(
        'ReglamentacionPage', related_name='reglamentacion_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_reglamentacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ReglamentacionSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the ReglamentacionPage below. This allows Sector to be added to a ReglamentacionPage.

    """
    page = ParentalKey(
        'ReglamentacionPage', related_name='reglamentacion_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_reglamentacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ReglamentacionPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the ReglamentacionPage object and tags.
    """
    content_object = ParentalKey(
        'ReglamentacionPage', related_name='tagged_items', on_delete=models.CASCADE)


class ReglamentacionPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la reglamentacion',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la reglamentacion", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=ReglamentacionPageTag, blank=False)
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
            'reglamentacion_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'reglamentacion_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the ReglamentacionAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the reglamentacion_autor_
        relationship directly we'd print `reglamentacion.ReglamentacionAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.reglamentacion_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the ReglamentacionPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the ReglamentacionSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the reglamentacion_sector_
        relationship directly we'd print `reglamentacion.ReglamentacionSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.reglamentacion_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.reglamentacion_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.reglamentacion_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the reglamentacion post into a list we can access on the template.
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
        return ReglamentacionPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to ReglamentacionPage as being ReglamentacionIndexPages
    parent_page_types = ['ReglamentacionIndexPage']

    # Specifies what content types can exist as children of ReglamentacionPage.
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


class ReglamentacionIndexPage(RoutablePageMixin, Page):

    # Speficies that only ReglamentacionPage objects can live under this index page
    subpage_types = ['ReglamentacionPage']

    # Defines a method to access the children of the page (e.g. ReglamentacionPage
    # objects).
    def children(self):
        return ReglamentacionPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(ReglamentacionIndexPage,
                        self).get_context(request)
        context['posts'] = ReglamentacionPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child ReglamentacionPage objects for this ReglamentacionPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = ReglamentacionPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this ReglamentacionPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class DiversificacionAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the DiversificacionPage below. This allows Autor to be added to a DiversificacionPage.
    """
    page = ParentalKey(
        'DiversificacionPage', related_name='diversificacion_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_diversificacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class DiversificacionSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the DiversificacionPage below. This allows Sector to be added to a DiversificacionPage.

    """
    page = ParentalKey(
        'DiversificacionPage', related_name='diversificacion_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_diversificacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class DiversificacionPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the DiversificacionPage object and tags.
    """
    content_object = ParentalKey(
        'DiversificacionPage', related_name='tagged_items', on_delete=models.CASCADE)


class DiversificacionPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la diversificacion',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la diversificacion", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=DiversificacionPageTag, blank=False)
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
            'diversificacion_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'diversificacion_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the DiversificacionAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the diversificacion_autor_
        relationship directly we'd print `diversificacion.DiversificacionAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.diversificacion_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the DiversificacionPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the DiversificacionSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the diversificacion_sector_
        relationship directly we'd print `diversificacion.DiversificacionSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.diversificacion_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.diversificacion_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.diversificacion_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the diversificacion post into a list we can access on the template.
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
        return DiversificacionPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to DiversificacionPage as being DiversificacionIndexPages
    parent_page_types = ['DiversificacionIndexPage']

    # Specifies what content types can exist as children of DiversificacionPage.
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


class DiversificacionIndexPage(RoutablePageMixin, Page):

    # Speficies that only DiversificacionPage objects can live under this index page
    subpage_types = ['DiversificacionPage']

    # Defines a method to access the children of the page (e.g. DiversificacionPage
    # objects).
    def children(self):
        return DiversificacionPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(DiversificacionIndexPage,
                        self).get_context(request)
        context['posts'] = DiversificacionPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child DiversificacionPage objects for this DiversificacionPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = DiversificacionPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this DiversificacionPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class SubastasEnergiasAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the SubastasEnergiasPage below. This allows Autor to be added to a SubastasEnergiasPage.
    """
    page = ParentalKey(
        'SubastasEnergiasPage', related_name='subastasenergias_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_subastasenergias_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class SubastasEnergiasSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the SubastasEnergiasPage below. This allows Sector to be added to a SubastasEnergiasPage.

    """
    page = ParentalKey(
        'SubastasEnergiasPage', related_name='subastasenergias_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_subastasenergias_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class SubastasEnergiasPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the SubastasEnergiasPage object and tags.
    """
    content_object = ParentalKey(
        'SubastasEnergiasPage', related_name='tagged_items', on_delete=models.CASCADE)


class SubastasEnergiasPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la subastasenergias',
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
        BaseStreamBlock(), verbose_name="Cuerpo de la subastasenergias", blank=False
    )
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=SubastasEnergiasPageTag, blank=False)
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
            'subastasenergias_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'subastasenergias_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the NotiicaPage's related Autor. Again note that we are using
        the ParentalKey's related_name from the SubastasEnergiasAutorRelationship model
        to access these objects. This allows us to access the Autor objects
        with a loop on the template. If we tried to access the subastasenergias_autor_
        relationship directly we'd print `subastasenergias.SubastasEnergiasAutorRelationship.None`
        """
        authors = [
            n.autor for n in self.subastasenergias_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the SubastasEnergiasPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the SubastasEnergiasSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the subastasenergias_sector_
        relationship directly we'd print `subastasenergias.SubastasEnergiasSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.subastasenergias_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.subastasenergias_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.subastasenergias_autor_relationship.all()
        ]

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the subastasenergias post into a list we can access on the template.
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
        return SubastasEnergiasPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to SubastasEnergiasPage as being SubastasEnergiasIndexPages
    parent_page_types = ['SubastasEnergiasIndexPage']

    # Specifies what content types can exist as children of SubastasEnergiasPage.
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


class SubastasEnergiasIndexPage(RoutablePageMixin, Page):

    # Speficies that only SubastasEnergiasPage objects can live under this index page
    subpage_types = ['SubastasEnergiasPage']

    # Defines a method to access the children of the page (e.g. SubastasEnergiasPage
    # objects).
    def children(self):
        return SubastasEnergiasPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(SubastasEnergiasIndexPage,
                        self).get_context(request)
        context['posts'] = SubastasEnergiasPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child SubastasEnergiasPage objects for this SubastasEnergiasPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = SubastasEnergiasPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this SubastasEnergiasPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class SubastasDocumentoUnidadAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'SubastasDocumentoUnidadPage', related_name='subastasdocumentounidad_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_subastasdocumentounidad_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class SubastasDocumentoUnidadSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'SubastasDocumentoUnidadPage', related_name='subastasdocumentounidad_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_subastasdocumentounidad_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class SubastasDocumentoUnidadPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'SubastasDocumentoUnidadPage', related_name='tagged_items', on_delete=models.CASCADE)


class SubastasDocumentoUnidadSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the SubastasDocumentoUnidad URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class SubastasDocumentoUnidadPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el subastasdocumentounidad',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen del subastasdocumentounidad",
        help_text='Imagen de presentación para el subastasdocumentounidad'
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="SubastasDocumentoUnidad",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(
        through=SubastasDocumentoUnidadPageTag, blank=False)
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
            'subastasdocumentounidad_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'subastasdocumentounidad_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.subastasdocumentounidad_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.subastasdocumentounidad_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.subastasdocumentounidad_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.subastasdocumentounidad_autor_relationship.all()
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

    parent_page_types = ['SubastasDocumentoUnidadIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', SubastasDocumentoUnidadSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class SubastasDocumentoUnidadIndexPage(RoutablePageMixin, Page):

    subpage_types = ['SubastasDocumentoUnidadPage']

    def children(self):
        return SubastasDocumentoUnidadPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(SubastasDocumentoUnidadIndexPage,
                        self).get_context(request)
        context['posts'] = SubastasDocumentoUnidadPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = SubastasDocumentoUnidadPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags
