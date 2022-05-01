import os
from django.db import models
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    StreamFieldPanel,
    FieldPanel,
    PageChooserPanel,
    InlinePanel
)
from wagtailsvg.models import Svg
from wagtail.core.models import Page, Orderable
from .blocks import InformationSystemsStructBlock, InterestPlacesStructBlock
from .blocks import BaseStreamBlock, GalleryStreamBlock
from wagtailseo.models import SeoMixin
from wagtailsvg.blocks import SvgChooserBlock
from ..common.blocks import HeaderStructBlock, NewsMissionaryBlock, CorporateCultureBlock,CardsHomePageBlock
from ..common.models import Autor, Sector


from wagtail.api import APIField
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager


from taggit.models import Tag, TaggedItemBase



# ----------------------------------------------------------------------------
# -------------------Inicio seccion Noticias ---------------------------------
# ----------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------
# -------------------Inicio seccion Noticias ---------------------------------
# ----------------------------------------------------------------------------

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


class HomePage(SeoMixin, Page):
    subpage_types = ['vivo.InfografiaIndexPage', 
                    'NoticiaIndexPage',
                    'GaleriaIndexPage',
                    'solicitudes.SolicitudesEspecialesPage','LoginPage','ClasificadosPage','SolicitudesPage','AgendaPage'
    ]

    board_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Título del la sección',
        verbose_name='Título del la sección'
    )

    interest_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Título del la sección',
        verbose_name='Título del la sección de sitios de interes'
    )

    interest_places  = StreamField(
        [('Sistema', InterestPlacesStructBlock())], blank=True, verbose_name="Sitios de interés")

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Título del la sección',
        verbose_name='Título del la sección'
    )

    information_systems = StreamField(
        [('Sistema', InformationSystemsStructBlock())], blank=True, verbose_name="Sistemas de información")

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título de la sección que será presentado al publico',
        verbose_name='Título de la sección de noticias'
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


    content_panels = Page.content_panels + [
   
        MultiFieldPanel([
            FieldPanel('board_title'),            
        ], heading="Enlaces de interés", classname="collapsible",
            help_text="Enlaces de interés que serán presentados en el home."),
  
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('news_list_title'), PageChooserPanel('news_list'), FieldPanel('news_button_title'), ]),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('interest_title'),
                 StreamFieldPanel('interest_places'), ]),
        ], heading="Sitios de interes", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('systems_title'),
                 StreamFieldPanel('information_systems'), ]),
        ], heading="Nuestras plataformas", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('gallery_list_title'), PageChooserPanel('gallery_list'), FieldPanel('gallery_button_title'), ]),
        ], heading="Galeria", classname="collapsible"),
    ]

    promote_panels = SeoMixin.seo_panels

class LoginPage(Page):
    subpage_types = []

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Login',
        verbose_name='Login'
    )

    content_panels = Page.content_panels + [
           
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('systems_title'), ]),
        ], heading="Login", classname="collapsible"),
    ]

class SolicitudesPage(Page):
    subpage_types = []

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Titulo',
        verbose_name='Titulo'
    )

    content_panels = Page.content_panels + [
           
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('systems_title'), ]),
        ], heading="Titulo", classname="collapsible"),
    ]

class ClasificadosPage(Page):
    subpage_types = []

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Titulo',
        verbose_name='Titulo'
    )

    content_panels = Page.content_panels + [
           
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('systems_title'), ]),
        ], heading="Titulo", classname="collapsible"),
    ]

class AgendaPage(Page):
    subpage_types = []

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text='Titulo',
        verbose_name='Titulo'
    )

    content_panels = Page.content_panels + [
           
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('systems_title'), ]),
        ], heading="Titulo", classname="collapsible"),
    ]   


class StandardPage(Page):
    subpage_types = []
    """Define el modelo de la seccion de estandar. 

    ...

    Methods
    -------
    None
    """
    pass


class SiteMapPage(Page):
    subpage_types = []
    """Página base para el mapa del sitio, no requiere campos. 

    ...

    Methods
    -------
    None
    """
    pass
