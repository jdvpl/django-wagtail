from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel,
    PageChooserPanel,
)

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtailsvg.models import Svg

from wagtail.api import APIField
from rest_framework.fields import Field
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from django.db import models
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page, Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TaggedItemBase
from ..common.models import Autor, Sector

from .blocks import LinkListStructBlock, FeaturedLinkStructBlock, ImageTextStructBlock, SliderStructBlock, TabTableStructBlock, RETIETableStructBlock, HeaderMenuBlockAcordeon
from ..sala_prensa.blocks import BaseStreamBlock
from ..common.blocks import ElementsListStructBlock, TabsListStructBlock, BriefcaseStructBlock, SecondLinkStructBlock, CardsStructBlock, SimpleDocumentCardSliderStructBlock, SimpleBriefcaseStructBlock, SubitemsBriefcaseStructBlock, SimpleBlockIconStructBlock, AccodionRichTextStructBlock, AccordeonRichTextStructBlock, LinkDocumentCardSliderStructBlock,HeaderStructBlock,ElementsListStructMenuBlock
from .unidad_resultados_subpages import CapacidadIndexPage, ConstruccionIndexPage, NuevosHogaresIndexPage, MarcoNormativoIndexPage, ImplementacionIndexPage, SubastasEnergiasIndexPage
from .blocksnoticias import BaseStreamBlock, GalleryStreamBlock, SocialNetworksBlock


class GestionSocialAmbientalPage(Page):

        subpage_types = ['OficinaAsuntosAmbientalesSosteniblesPage','VideosSosIndexPage','DocumentoSosIndexPage','InfografiaSosIndexPage','CambioClimaticoPage','EstrategiaDesarrolloRelTerrPage']

        intro_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Gestion Social y Ambiental")
        intro = RichTextField(
            null=True,
            blank=True,
            help_text='Introducción de la sección',
            verbose_name="Introducción"
        )
        image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            verbose_name="Imagen",
            help_text='Imagen que representa la sección',
            on_delete=models.SET_NULL,
            related_name='+'
        )
        alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")


        sostenib_list = StreamField(
        [('Sostenibilidad', ElementsListStructBlock())], blank=True, verbose_name="Sostenibilidad")

        content_panels = Page.content_panels + [
            MultiFieldPanel([
                FieldPanel('intro_title'),
                FieldPanel('intro'),
                ImageChooserPanel('image'),
                FieldPanel('alt_text'),
            ], heading="Introducción", classname="collapsible",
                help_text='Introducción de la sección'),
            MultiFieldPanel([
                StreamFieldPanel('sostenib_list'),
            ], heading="Sostenibilidad iconos", classname="collapsible",
                help_text='Sostenibilidad'),
        ]

class OficinaAsuntosAmbientalesSosteniblesPage(Page):
        subpage_types = []

        intro_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Gestion Social y Ambiental")

        intro = RichTextField(
            null=True,
            blank=True,
            help_text='Introducción de la sección',
            verbose_name="Introducción"
        )

        image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            verbose_name="Imagen",
            help_text='Imagen que representa la sección',
            on_delete=models.SET_NULL,
            related_name='+'
        )
        alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
        #links decretos
        first_links = StreamField(
            [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Decreto")

        #segundo titulo
        second_title = models.CharField(
             "Título de la sección", max_length=254, null=False, blank=False, default="Historia")
        second_text = RichTextField(
             null=True,
             blank=True,
             help_text='Texto de de la sección',
             verbose_name="Historia"
         )

         #tercer titulo
        third_title = models.CharField(
              "Título de la sección", max_length=254, null=False, blank=False, default="Funciones")
        third_text = RichTextField(
              null=True,
              blank=True,
              help_text='Texto de de la sección',
              verbose_name="Funciones"
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
         #PANELES
        content_panels = Page.content_panels + [
            MultiFieldPanel([
                FieldPanel('intro_title'),
                FieldPanel('intro'),
                ImageChooserPanel('image'),
                FieldPanel('alt_text'),
            ], heading="Introducción", classname="collapsible",
                help_text='Introducción de la sección'),

         MultiFieldPanel([
            StreamFieldPanel('first_links'),
           ], heading="Decreto", classname="collapsible",
            help_text='Decretos'),
         #titulo y texto enriquecido
         MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_text'),
                ], heading="Historia", classname="collapsible",
            help_text='Introducción de la sección'),
         MultiFieldPanel([
            FieldPanel('third_title'),
            FieldPanel('third_text'),
                ], heading="Funciones", classname="collapsible",
            help_text='Introducción de la sección'),
        #lista de videos
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('videos_list_title'), PageChooserPanel('videos_list'), FieldPanel('videos_button_title'), ]),
        ], heading="Videos", classname="collapsible"),
        ]

# paginas de infografias

class InfografiaSosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaSosPage', related_name='infografiasos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_infografiasos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class InfografiaSosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaSosPage', related_name='infografiasos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_infografiasos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class InfografiaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'InfografiaSosPage', related_name='tagged_items', on_delete=models.CASCADE)


class InfografiaSosPage(Page):
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
            'infografiasos_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'infografiasos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.infografiasos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.infografiasos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.infografiasos_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.infografiasos_autor_relationship.all()
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

    parent_page_types = ['InfografiaSosIndexPage']

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


class InfografiaSosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['InfografiaSosPage']

    def children(self):
        return InfografiaSosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(InfografiaSosIndexPage, self).get_context(request)
        context['posts'] = InfografiaSosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = InfografiaSosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags




#pagina de videos
class VideosSosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'VideosSosPage', related_name='videosos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_videosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class VideosSosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'VideosSosPage', related_name='videosos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_videosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class VideosSosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'VideosSosPage', related_name='tagged_items', on_delete=models.CASCADE)


class VideosSosPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el video',
        blank=False,
        verbose_name="Introducción",)
    link_video = models.URLField(
        "Video", blank=False, help_text='El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=VideosSosPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        FieldPanel('link_video'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'videosos_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'videosos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.videosos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.videosos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.videosos_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.videosos_autor_relationship.all()
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
    parent_page_types = ['VideosSosIndexPage']

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


class VideosSosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['VideosSosPage']

    def children(self):
        return VideosSosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(VideosSosIndexPage, self).get_context(request)
        context['posts'] = VideosSosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = VideosSosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags

# audios

class AudioSosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'AudioSosPage', related_name='audiosos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_audiosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class AudioSosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'AudioSosPage', related_name='audiosos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_audiosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class AudioSosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'AudioSosPage', related_name='tagged_items', on_delete=models.CASCADE)


class AudioSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the audio URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class AudioSosPage(Page):
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
    tags = ClusterTaggableManager(through=AudioSosPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        MediaChooserPanel('audio'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel('audiosos_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel('audiosos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.audiosos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.audiosos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.audiosos_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.audiosos_autor_relationship.all()
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

    parent_page_types = ['AudioSosIndexPage']

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


class AudioSosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['AudioSosPage']

    def children(self):
        return AudioSosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(AudioSosIndexPage, self).get_context(request)
        context['posts'] = AudioSosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = AudioSosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags

# paginas de documentos

class DocumentoSosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'DocumentoSosPage', related_name='documentosos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_documentosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class DocumentoSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'DocumentoSosPage', related_name='documentosos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_documentosos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class DocumentoSosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'DocumentoSosPage', related_name='tagged_items', on_delete=models.CASCADE)


class DocumentoSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Documento URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class DocumentoSosPage(Page):
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
    tags = ClusterTaggableManager(through=DocumentoSosPageTag, blank=False)
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
            'documentosos_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'documentosos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.documentosos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.documentosos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.documentosos_sector_relationship.all()
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

    parent_page_types = ['DocumentoSosIndexPage']

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


class DocumentoSosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['DocumentoSosPage']

    def children(self):
        return DocumentoSosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(DocumentoSosIndexPage, self).get_context(request)
        context['posts'] = DocumentoSosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = DocumentoSosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags




# cambio climatico
class CambioClimaticoPage(Page):
       subpage_types = []

       intro_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Cambio Climatico")

       intro = RichTextField(
            null=True,
            blank=True,
            help_text='Introducción de la sección',
            verbose_name="Introducción"
        )

       slider = StreamField(
           [('slider', SliderStructBlock())], blank=True, verbose_name="Slider")

       alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

       #segundo titulo
       second_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="PIGCCme")
       second_text = RichTextField(
            null=True,
            blank=True,
            help_text='Texto de de la sección',
            verbose_name="Historia")

       first_links = StreamField(
            [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Activo")
       #pestañas
       first_tabs = StreamField(
           [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

        #links Activos de conocimiento
       third_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="")
        #texto intruductorio links
       intro_linkstxt = models.TextField(verbose_name="Texto introductorio", blank=True,
                                    help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

       #multimedia

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
         #PANELES
       content_panels = Page.content_panels + [
        #encabezado
            MultiFieldPanel([
                FieldPanel('intro_title'),
                FieldPanel('intro'),
                StreamFieldPanel('slider'),
                FieldPanel('alt_text'),
            ], heading="Introducción", classname="collapsible",
                help_text='Introducción de la sección'),

         #titulo y texto enriquecido
         MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_text'),
            StreamFieldPanel('first_tabs'),
                ], heading="Plan integral", classname="collapsible",
            help_text='Introducción de la sección'),
         #Links activos de Conocimiento
         MultiFieldPanel([
            FieldPanel('third_title'),
            FieldPanel('intro_linkstxt'),
            StreamFieldPanel('first_links'),
            
            
           ], heading="Plan Integral de Gestión de Cambio Climático", classname="collapsible",
            help_text='PIGCCme'),

        #lista de videos
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('videos_list_title'), PageChooserPanel('videos_list'), FieldPanel('videos_button_title'), ]),
        ], heading="Videos", classname="collapsible"),
        ]

# Estrategia de desarrollo y relacionamiento territorial
class EstrategiaDesarrolloRelTerrPage(Page):
       subpage_types = []

       intro_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Titulo Seccion")

       intro = RichTextField(
            null=True,
            blank=True,
            help_text='Introducción de la sección',
            verbose_name="Introducción"
        )

       slider = StreamField(
           [('slider', SliderStructBlock())], blank=True, verbose_name="Slider")

       second_text = RichTextField(
            null=True,
            blank=True,
            help_text='Introducción de la sección',
            verbose_name="Introducción"
        )

       #Segundo Titulo - Mesa Técnica de Articulación Intersectorial
       second_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Mesa Técnica de Articulación Intersectorial")
        #links    
       first_links = StreamField(
            [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Activo")
       
       third_text = RichTextField(
            null=True,
            blank=True,
            help_text='Texto de la sección itro',
            verbose_name="Texto complementario de seccion"
        )
        #pestañas
       first_tabs = StreamField(
           [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")


        #Tercer  titulo -Territorios priorizados
       third_title = models.CharField(
            "Título de la sección", max_length=254, null=False, blank=False, default="Territorios priorizados")
        #texto intruductorio links
       fourth_text = RichTextField(
            null=True,
            blank=True,
            help_text='Texto de territorios',
            verbose_name="Texto complementario de seccion"
        )
       #panel con botones
       menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="menu con botones")

        #multimedia

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

        #seccion documentos, infografias y  podcast   
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


         #PANELES
       content_panels = Page.content_panels + [
        #encabezado
        MultiFieldPanel([
                FieldPanel('intro_title'),
                FieldPanel('intro'),
                StreamFieldPanel('slider'),
                FieldPanel('second_text'),
            ], heading="Introducción", classname="collapsible",
                help_text='Introducción de la sección'),

         #titulo y texto enriquecido
         MultiFieldPanel([
            FieldPanel('second_title'),
            StreamFieldPanel('first_links'),      
            FieldPanel('second_text'),
            StreamFieldPanel('first_tabs'),
                ], heading="Mesa Técnica de Articulación Intersectorial", classname="collapsible",
            help_text='Introducción de la sección'),
         # Territorios priorizados
         MultiFieldPanel([
            FieldPanel('third_title'),
            FieldPanel('fourth_text'),
            StreamFieldPanel('menu_list'),
            ], heading="Territorios", classname="collapsible",
            help_text='Territorios Priorizados'),

        #lista de videos
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('videos_list_title'), PageChooserPanel('videos_list'), FieldPanel('videos_button_title'), ]),
        ], heading="Videos", classname="collapsible"),
        
        #documentos
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('documents_list_title'), PageChooserPanel('documents_list'), FieldPanel('documents_button_title'), ]),
        ], heading="Presentaciones", classname="collapsible"),
                
        #infografias
        
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('infographics_list_title'), PageChooserPanel('infographics_list'), FieldPanel('infographics_button_title'), ]),
        ], heading="Infografías", classname="collapsible"),
        #podscast
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('podcast_list_title'), FieldPanel('podcast_iframe_url'), FieldPanel('podcast_url'), FieldPanel('podcats_button_title'), ]),
        ], heading="Podcast", classname="collapsible"),
                   

        ]