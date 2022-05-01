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
from ..common.blocks import ElementsListStructBlock, TabsListStructBlock, BriefcaseStructBlock, SecondLinkStructBlock, CardsStructBlock, SimpleDocumentCardSliderStructBlock, SimpleBriefcaseStructBlock, SubitemsBriefcaseStructBlock, SimpleBlockIconStructBlock, AccodionRichTextStructBlock, AccordeonRichTextStructBlock, AccordeonIconStructBlock, LinkDocumentCardSliderStructBlock, AccordeonDocumentStructBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailmedia.edit_handlers import MediaChooserPanel
from rest_framework.fields import Field
from wagtail.core.fields import RichTextField, StreamField
from .blocks import EdictosTableStructBlock, GrupoEjecucionTableStructBlock,SubItemseStructBlock, NotiAdminTableStructBlock, TabsListStructBlockDocuments,TabsListStructBlockTable

""" from .blocks import BaseStreamBlock, GalleryStreamBlock, SocialNetworksBlock """
from ..common.models import Autor, Sector, Year


class RepositorioNormativoPage(Page):
    subpage_types = ['ConceptoIndexPage','AgendaNormativaPage',"DefensaJudicialPage",
                    "EstructuraOrganizacionalGrupoRegaliasPage",
                    "InversionesSGRCovid19Page", "NotificacionesAdministrativasPage",
                    "NoticiosoAdministrativoPage","AgendaRegulatoriaPage","DecretosModificatorioDecretoPage", 
                    "NormativaCOVID19Page","NormativaPage", "AcuerdosConciliatoriosPage", 
                    "NotificacionesJudicialesPage", "SistemaRegaliasPage","NotificacionesDisciplinariasPage"
                    ]
                    
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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    decreto_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )


    decreto_description = RichTextField(
        null=True,
        blank=True,
        help_text='Decreto Número',
        verbose_name="Decreto Número"
    )
    book_one = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )


    book_one_description = RichTextField(
        null=True,
        blank=True,
        help_text='Libro 1',
        verbose_name="Libro 1"
    )

    
    
    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    intro_tab = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    book_three = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    book_three_description = RichTextField(
        null=True,
        blank=True,
        help_text='Libro 3',
        verbose_name="Libro 3"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),

        MultiFieldPanel([
            FieldPanel('decreto_title'),
            FieldPanel('decreto_description'),
        ], heading="Decreto Número", classname="collapsible",
            help_text='Decreto Número'),

        MultiFieldPanel([
            FieldPanel('book_one'),
            FieldPanel('book_one_description'),
        ], heading="Libro 1", classname="collapsible",
            help_text='Libro 1'),
        
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('intro_tab'),
            StreamFieldPanel('tab_list'),
        ], heading="Libro 2", classname="collapsible",
            help_text='Libro 2'),
        
        MultiFieldPanel([
            FieldPanel('book_three'),
            FieldPanel('book_three_description'),
        ], heading="Libro 1", classname="collapsible",
            help_text='Libro 1'),
    ]

""" Conceptos Jurídicos """


class ConceptoAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ConceptoPage', related_name='concepto_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_concepto_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ConceptoAnoRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ConceptoPage', related_name='concepto_year_relationship', on_delete=models.CASCADE
    )
    year = models.ForeignKey(
        Year, related_name='year_concepto_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('year')
    ]

    api_fields = [
        APIField('year'),
    ]


class ConceptoSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ConceptoPage', related_name='concepto_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_concepto_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ConceptoPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ConceptoPage', related_name='tagged_items', on_delete=models.CASCADE)


class ConceptoSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Concepto URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ConceptoPage(Page):

    settled_number = models.CharField(
        blank=True, max_length=255, verbose_name="Número de Radicado")
    settled_date = models.DateField(
        "Fecha de radicado", blank=False, null=True
    )
    petitioner = models.TextField(
        help_text='Peticionario',
        blank=True,
        verbose_name="Peticionario",)
    subject = models.TextField(
        help_text='Tema',
        blank=True,
        verbose_name="Tema",)
    summary = models.TextField(
        help_text='Resumen',
        blank=True,
        verbose_name="Resumen",)
    norm = models.TextField(
        help_text='Normas/Jurisprudencia',
        blank=True,
        verbose_name="Normas/Jurisprudencia",)
    norm_abolish = models.TextField(
        help_text='Norma Derogada',
        blank=True,
        verbose_name="Norma Derogada",)
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="Anexos",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tags = ClusterTaggableManager(through=ConceptoPageTag, blank=False)

    content_panels = Page.content_panels + [

        InlinePanel(
            'concepto_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        InlinePanel(
            'concepto_year_relationship', label="Año Concepto",
            panels=None, min_num=1, max_num=1),
        FieldPanel('settled_number'),
        FieldPanel('settled_date'),
        FieldPanel('petitioner'),
        FieldPanel('subject'),
        FieldPanel('summary'),
        FieldPanel('norm'),
        FieldPanel('norm_abolish'),
        DocumentChooserPanel('document_file'),
        FieldPanel('tags'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('settled_number'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.concepto_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.concepto_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.concepto_sector_relationship.all()
        ]

    @property
    def sectors_list_str(self):
        sectors = [
            str(child.sector) for child in self.concepto_sector_relationship.all()
        ]
        return ', '.join(sectors)

    @property
    def year_list(self):
        return [
            str(child.year) for child in self.concepto_year_relationship.all()
        ]
    
    @property
    def year_list_str(self):
        years= [
            str(child.year) for child in self.concepto_year_relationship.all()
        ]
        return ''.join(years)

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

    parent_page_types = ['ConceptoIndexPage']

    subpage_types = []

    api_fields = [
        APIField('settled_number'),
        APIField('settled_date'),
        APIField('petitioner'),
        APIField('subject'),
        APIField('summary'),
        APIField('norm'),
        APIField('norm_abolish'),
        APIField('sectors_list'),
        APIField('year_list'),
        APIField('tags'),
        APIField('document_file', ConceptoSerializedField()),
    ]


class ConceptoIndexPage(RoutablePageMixin, Page):

    subpage_types = ['ConceptoPage']

    def children(self):
        return ConceptoPage.objects.descendant_of(self).live().order_by('-settled_date')

    def get_years(self, posts):
        for post in posts:
            years = post.concepto_year_relationship.filter(
                page_id=post.id)
            post['year'] = years[0].year
        return posts

    def get_context(self, request):
        context = super(ConceptoIndexPage, self).get_context(request)
        context['posts'] = ConceptoPage.objects.descendant_of(
            self).live().order_by('-settled_date')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = ConceptoPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" AgendaRegulatoria """
class AgendaNormativaPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    data_description = RichTextField(
        null=True,
        blank=True,
        help_text='Descripcion agenda normativa',
        verbose_name="Descripcion agenda normativa"
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    items_list = StreamField(
        [('Lista', SubItemseStructBlock())], blank=True, verbose_name="Lista")

    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Proyectos Normativos para Consulta a la Ciudadanía")

    title_list_one = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Proyectos Normativos para Consulta a la Ciudadanía")
    list_one = StreamField(
        [('Lista', AccordeonDocumentStructBlock())], blank=True, verbose_name="Lista")
        

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('data_description'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            StreamFieldPanel('title_list_one'),
            StreamFieldPanel('menu_list'),
        ], heading="Proyectos Normativos para Consulta a la Ciudadanía", classname="collapsible",
            help_text='Proyectos Normativos para Consulta a la Ciudadanía'),

        MultiFieldPanel([
            StreamFieldPanel('items_list'),
        ], heading="Elementos", classname="collapsible",
            help_text="Elementos"),
    ]

class AgendaRegulatoriaPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    data_description = RichTextField(
        null=True,
        blank=True,
        help_text='Descripcion agenda normativa',
        verbose_name="Descripcion agenda normativa"
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    items_list = StreamField(
        [('Lista', SubItemseStructBlock())], blank=True, verbose_name="Lista")

    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Proyectos Normativos para Consulta a la Ciudadanía")

    title_list_one = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Proyectos Normativos para Consulta a la Ciudadanía")
    list_one = StreamField(
        [('Lista', AccordeonDocumentStructBlock())], blank=True, verbose_name="Lista")
        

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('data_description'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            StreamFieldPanel('title_list_one'),
            StreamFieldPanel('menu_list'),
        ], heading="Proyectos Normativos para Consulta a la Ciudadanía", classname="collapsible",
            help_text='Proyectos Normativos para Consulta a la Ciudadanía'),

        MultiFieldPanel([
            StreamFieldPanel('items_list'),
        ], heading="Elementos", classname="collapsible",
            help_text="Elementos"),
    ]

""" Defensa Judicial """
class DefensaJudicialPage(Page):
    subpage_types = []

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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    accordion_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acordeón")
        
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            StreamFieldPanel('accordion_list'),
        ], heading="Fechas", classname="collapsible",
            help_text='Fechas'),
    ]
""" Estructura organizacional grupo de regalias """
class EstructuraOrganizacionalGrupoRegaliasPage(Page):
    subpage_types = []

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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    table_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    table_estructura = StreamField(
        [('Elementos', GrupoEjecucionTableStructBlock())], blank=True, verbose_name="Grupo de ejecución estratégica del sector extractivo")

        
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            FieldPanel('table_title'),
            StreamFieldPanel('table_estructura'),
        ], heading="Grupo de ejecución estratégica del sector extractivo", classname="collapsible",
            help_text='Grupo de ejecución estratégica del sector extractivo'),
    ]


class AcuerdosConciliatoriosPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Título de la sección")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

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

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Acuerdos conciliatorios", classname="collapsible",
            help_text='Acuerdos conciliatorios'),


    ]

class NotificacionesDisciplinariasPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Título de la sección")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

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

    historical_list = StreamField(
        [('Lista', AccordeonIconStructBlock())], blank=True, verbose_name="Lista")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Lista", classname="collapsible",
            help_text='Lista'),


    ]

""" Inversiones SGR COVID 19 """
class InversionesSGRCovid19Page(Page):
    
    subpage_types = []

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Inversiones SGR COVID 19")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tamaño recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripción del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripción"
    )

    button_title = models.CharField(
        "Título del boton", max_length=254, help_text='Título del boton')
    link_mapa = models.URLField(
        "Link del mapa", blank=True)
    document_mapa = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Documento del mapa",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('button_title'),
            FieldPanel('link_mapa'),
            DocumentChooserPanel('document_mapa'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
    ]

    """ Inversiones SGR COVID 19 """
class NotificacionesJudicialesPage(Page):
    
    subpage_types = []

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Titulo")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tamaño recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripción del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripción"
    )

    button_title = models.CharField(
        "Título del boton", max_length=254, help_text='Título del boton')
    link_mapa = models.URLField(
        "Link del mapa", blank=True)
    document_mapa = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Documento del mapa",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('button_title'),
            FieldPanel('link_mapa'),
            DocumentChooserPanel('document_mapa'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
    ]


class SistemaRegaliasPage(Page):
    
    subpage_types = ["EstructuraOrganizacionalGrupoRegaliasPage","InversionesSGRCovid19Page"]

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Titulo")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tamaño recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripción del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripción"
    )

    button_title = models.CharField(
        "Título del boton", max_length=254, help_text='Título del boton')
    link_mapa = models.URLField(
        "Link del mapa", blank=True)
    document_mapa = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Documento del mapa",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('button_title'),
            FieldPanel('link_mapa'),
            DocumentChooserPanel('document_mapa'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
    ]


class EdictosPage(Page):
    subpage_types = []

    # tab_list = StreamField(
    #     [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    # menu_list_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Título que será presentado al publico',
    #     verbose_name='Título de la sección'
    # )
    # menu_list = StreamField(
    #     [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="RETIE Vigente")

    edict_list = StreamField(
        [('Items', EdictosTableStructBlock())], blank=True, verbose_name="Lista Enlaces ")

    content_panels = Page.content_panels + [
        # MultiFieldPanel([
        #     StreamFieldPanel('tab_list'),
        # ], heading="Pestañas", classname="collapsible",
        #     help_text='Pestañas'),
        # MultiFieldPanel([
        #     FieldPanel('menu_list_title'),
        #     StreamFieldPanel('menu_list'),
        # ], heading="Lineamientos y Políticas", classname="collapsible",
        #     help_text='Lineamientos y Políticas'),
        MultiFieldPanel([
            StreamFieldPanel('edict_list'),
        ], heading="Lista Enlaces", classname="collapsible",
            help_text='Lista Enlaces'),
    ]


class NotificacionesAdministrativasPage(Page):
    subpage_types = ["EdictosPage"]

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Notificaciones Administrativas")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    edics_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    edics_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )


    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la sección")

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),

        MultiFieldPanel([
            FieldPanel('edics_list_title'),
            FieldPanel('edics_intro'),
        ], heading="Edictos", classname="collapsible",
            help_text='Edictos'),

        MultiFieldPanel([
            StreamFieldPanel('link_list'),
        ], heading="Enlaces", classname="collapsible",
            help_text='Listas de enlaces'),

        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Enlaces de la sección", classname="collapsible",
            help_text='Listado de enlaces de la sección'),

    ]


class NoticiosoAdministrativoPage(Page):
    subpage_types = []

    # tab_list = StreamField(
    #     [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    # menu_list_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Título que será presentado al publico',
    #     verbose_name='Título de la sección'
    # )
    # menu_list = StreamField(
    #     [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="RETIE Vigente")

    noti_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    notiadmin_list = StreamField(
        [('Items', NotiAdminTableStructBlock())], blank=True, verbose_name="Lista Enlaces")

    content_panels = Page.content_panels + [
        # MultiFieldPanel([
        #     StreamFieldPanel('tab_list'),
        # ], heading="Pestañas", classname="collapsible",
        #     help_text='Pestañas'),
        # MultiFieldPanel([
        #     FieldPanel('menu_list_title'),
        #     StreamFieldPanel('menu_list'),
        # ], heading="Lineamientos y Políticas", classname="collapsible",
        #     help_text='Lineamientos y Políticas'),
        MultiFieldPanel([
            FieldPanel('noti_intro'),
            StreamFieldPanel('notiadmin_list'),
        ], heading="Lista Enlaces", classname="collapsible",
            help_text='Lista Enlaces'),
    ]



""" Decretos """
class DecretosModificatorioDecretoPage(Page):
    subpage_types = []

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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    consolidado_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    consolidado_list = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Consolidado")
    
    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    intro_tab = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlockTable())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            FieldPanel('consolidado_list_title'),
            StreamFieldPanel('consolidado_list'),
        ], heading="Consolidado", classname="collapsible",
            help_text='Consolidado'),
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('intro_tab'),
            StreamFieldPanel('tab_list'),
        ], heading="Decretos modificatorios", classname="collapsible",
            help_text='Decretos modificatorios'),
    ]
""" Normativa covid 19 """
class NormativaCOVID19Page(Page):
    subpage_types = []

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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )


    
    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    intro_tab = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlockDocuments())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('intro_tab'),
            StreamFieldPanel('tab_list'),
        ], heading="Decretos modificatorios", classname="collapsible",
            help_text='Decretos modificatorios'),
    ]

""" Decretos """
class NormativaPage(Page):
    subpage_types = ["NormativaDetallePage"]

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
        help_text='Imagen que representa la sección.',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    decreto_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )


    decreto_description = RichTextField(
        null=True,
        blank=True,
        help_text='Decreto Número',
        verbose_name="Decreto Número"
    )
    book_one = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )


    book_one_description = RichTextField(
        null=True,
        blank=True,
        help_text='Libro 1',
        verbose_name="Libro 1"
    )

    
    
    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    intro_tab = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    book_three = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    book_three_description = RichTextField(
        null=True,
        blank=True,
        help_text='Libro 3',
        verbose_name="Libro 3"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('image'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),

        MultiFieldPanel([
            FieldPanel('decreto_title'),
            FieldPanel('decreto_description'),
        ], heading="Decreto Número", classname="collapsible",
            help_text='Decreto Número'),

        MultiFieldPanel([
            FieldPanel('book_one'),
            FieldPanel('book_one_description'),
        ], heading="Libro 1", classname="collapsible",
            help_text='Libro 1'),
        
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('intro_tab'),
            StreamFieldPanel('tab_list'),
        ], heading="Libro 2", classname="collapsible",
            help_text='Libro 2'),
        
        MultiFieldPanel([
            FieldPanel('book_three'),
            FieldPanel('book_three_description'),
        ], heading="Libro 1", classname="collapsible",
            help_text='Libro 1'),
    ]

class NormativaDetallePage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Titulo")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    # documents_list = StreamField(
    #     [('Documentos', DeclarationStructBlock())], blank=True, verbose_name="Documentos de la sección")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        # MultiFieldPanel([
        #     StreamFieldPanel('documents_list'),
        # ], heading="Documentos de la sección", classname="collapsible",
        #     help_text='Listado de enlaces de la sección'),
    ]