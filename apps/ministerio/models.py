
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    StreamFieldPanel,
    FieldPanel,
    PageChooserPanel,
    InlinePanel
)

import os
from wagtail.api import APIField
from rest_framework.fields import Field
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from django.db import models
from wagtailsvg.models import Svg
from wagtail.snippets.models import register_snippet
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from .blocks import MinistrosBlock, EntitiesBlock, IntroSectionBlock, SubsectionsBlock,  AcordionBlock, CurrentMinisterBlock, CorporateCultureObjetivesBlock, FunctionaryListStructBlock, ProcessBlock,  InformationManagementBlock, AccordeonSheetsCVStructBlock, AdministrativeCareerTableStructBlock
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
from wagtail.documents.edit_handlers import DocumentChooserPanel
from ..common.blocks import SecondLinkStructBlock, ElementsListStructBlock, SimpleBriefcaseStructBlock1, TabsListStructBlock, BriefcaseStructBlock, TabTableStructBlock, BudgetExecutionTabStructBlock, DocumentBriefcaseStructBlock, AlienationTabStructBlock, CorporateCultureBlock, SubitemsBriefcaseStructBlock, IconDocumentBriefcaseStructBlock, IconDocumentListStructBlock, DocumentListStructBlock, DocumentSimpleListStructBlock, SimpleBriefcaseStructBlock, IconDocumentListTabStructBlock, BriefcaseMenuAccodeonStructBlock, AccordeonRichTextStructBlock, SecondLinkDocuemntStructBlock, SimpleIconBriefcaseStructBlock, AccodionRichTextStructBlock, SimpleDocumentCardSliderStructBlock


class MinisterioPage(Page):
    subpage_types = ['EstructuraOrganizacionalPage',
                     'EstrategicoPage', 'GestionPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Ministerio")
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

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),
    ]


class EstructuraOrganizacionalPage(Page):
    subpage_types = ['EstructuraSectorPage',
                     'OrganigramaInteractivoPage', 'GestionTalentoHumanoPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Estructura Organizacional")
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

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),
    ]


class EstructuraSectorPage(Page):
    subpage_types = []
    sector_entities_title = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        help_text='Título del componente',
        verbose_name="Título del componente"
    )

    sector_entities_logo = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del componente en formato SVG',
        verbose_name="Icono del componente"
    )

    related_entities_title = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        help_text='Título del componente',
        verbose_name="Título del componente"
    )

    related_entities_logo = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del componente en formato SVG',
        verbose_name="Icono del componente"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sector_entities_title'),
            SvgChooserPanel('sector_entities_logo'),
        ], heading="Entidades Adscritas", classname="collapsible",
            help_text="Entidades adscritas al sector."),
        MultiFieldPanel([
            FieldPanel('related_entities_title'),
            SvgChooserPanel('related_entities_logo'),
        ], heading="Entidades Vinculadas", classname="collapsible",
            help_text="Entidades vinculadas al sector."),
    ]


class FuncionarioPage(Page):
    subpage_types = []
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Imagen de perfil del funcionario.',
        verbose_name="Imagen de perfil del funcionario"
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        help_text='Nombre del funcionario.',
        verbose_name="Nombre del funcionario"
    )
    position = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        help_text='Cargo del funcionario.',
        verbose_name="Cargo del funcionario"
    )

    staff_list = StreamField(
        [('Personal', FunctionaryListStructBlock())], blank=True, verbose_name="Grupos y Personas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('name', classname="full"),
        ], heading="Información del funcionario", classname="collapsible",
            help_text='Información del funcionario'),

        MultiFieldPanel([
            StreamFieldPanel('staff_list'),
        ], heading="Grupos y Personas", classname="collapsible",
            help_text='Listado de grupos y personas'),

    ]

    # Specifies parent to FuncionarioPage as being OrganigramaInteractivoPage
    parent_page_types = ['OrganigramaInteractivoPage']


class OrganigramaInteractivoPage(Page):
    subpage_types = []
    despacho_ministerio_minas_energia = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Despacho Ministerio de Minas y Energía'
    )

    despacho_viceministro_minas = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Despacho Viceministro de Minas'
    )

    despacho_viceministro_energia = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Despacho Viceministro de Energía'
    )
    despacho_secretario_general = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Despacho del Secretario General'
    )
    grupo_unidad_resultados = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Grupo Unidad de Resultados'
    )
    grupo_gestion_estrategica_sector_extractivo = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Grupo de Gestión Estratégica del Sector Extractivo'
    )
    oficina_asuntos_ambientales_sociales = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Oficina de Asuntos Ambientales y Sociales'
    )
    oficina_asesora_juridica = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Oficina Asesora de Jurídica'
    )
    oficina_planeacion_gestion_internacional = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Oficina de Planeación y Gestión Internacional'
    )
    grupo_comunicacion_prensa = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Grupo de Comunicación y Prensa'
    )
    grupo_asuntos_legislativos = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Grupo de Asuntos Legislativos'
    )
    oficina_asuntos_regulatorios_empresariales = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Oficina de Asuntos Regulatorios y Empresariales'
    )
    oficina_control_interno = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione el funcionario correspondiente para este cargo.',
        verbose_name='Oficina de Control Interno'
    )

    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="Documento",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            MultiFieldPanel(
                [PageChooserPanel('despacho_ministerio_minas_energia'), ]),
            MultiFieldPanel(
                [PageChooserPanel('despacho_viceministro_minas'), ]),
            MultiFieldPanel(
                [PageChooserPanel('despacho_viceministro_energia'), ]),
            MultiFieldPanel(
                [PageChooserPanel('despacho_secretario_general'), ]),
            MultiFieldPanel([PageChooserPanel('grupo_unidad_resultados'), ]),
            MultiFieldPanel(
                [PageChooserPanel('grupo_gestion_estrategica_sector_extractivo'), ]),
            MultiFieldPanel(
                [PageChooserPanel('oficina_asuntos_ambientales_sociales'), ]),
            MultiFieldPanel([PageChooserPanel('oficina_asesora_juridica'), ]),
            MultiFieldPanel(
                [PageChooserPanel('oficina_planeacion_gestion_internacional'), ]),
            MultiFieldPanel([PageChooserPanel('grupo_comunicacion_prensa'), ]),
            MultiFieldPanel(
                [PageChooserPanel('grupo_asuntos_legislativos'), ]),
            MultiFieldPanel(
                [PageChooserPanel('oficina_asuntos_regulatorios_empresariales'), ]),
            MultiFieldPanel([PageChooserPanel('oficina_control_interno'), ]),
            MultiFieldPanel([
                DocumentChooserPanel('document_file'),
            ], heading="Documento Organigrama", classname="collapsible",
                help_text='Documento Organigrama'),

        ], heading="Funcionarios", classname="collapsible")
    ]

    # Speficies that only FuncionarioPage objects can live under this index page
    subpage_types = ['FuncionarioPage']


class GestionTalentoHumanoPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Gestión de Talento Humano")
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

    menu_list = StreamField(
        [('Elementos', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Menú")

    cards_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    cards_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    cards_list = StreamField(
        [('Documentos', SimpleDocumentCardSliderStructBlock())], blank=True, verbose_name="Documentos")

    manual_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    manual_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    manual_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Manual de Funciones")

    salary_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    salary_links = StreamField(
        [('Salario', SecondLinkStructBlock())], blank=True, verbose_name="Salarios")

    post_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Publicación de la declaración de renta y complementarios de funcionarios públicos")
    post_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    post_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acordeón")

    job_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Oferta de empleo")
    job_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    sheets_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Hojas de Vida Aspirantes")
    sheets_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    sheets_list = StreamField(
        [('Elementos', AccordeonSheetsCVStructBlock())], blank=True, verbose_name="Hojas de Vida Aspirantes")

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
    featured_link = models.URLField("Link", blank=True)

    sheets_title2 = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Vinculación a Terceros – Cancelación del Registro Público de Carrera Administrativa ")
    sheets_intro2 = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    sheets_list2 = StreamField(
        [('Elementos', AdministrativeCareerTableStructBlock())], blank=True, verbose_name="Vinculación a Terceros – Cancelación del Registro Público de Carrera Administrativa:")

    

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
            StreamFieldPanel('menu_list')
        ], heading="Menu", classname="collapsible",
            help_text='mneu'),
        MultiFieldPanel([
            FieldPanel('cards_list_title'),
            FieldPanel('cards_intro'),
            StreamFieldPanel('cards_list'),
        ], heading="Planta de Personal – Organización Interna", classname="collapsible",
            help_text='Planta de Personal – Organización Interna'),
        MultiFieldPanel([
            FieldPanel('manual_links_title'),
            FieldPanel('manual_intro'),
            StreamFieldPanel('manual_links')
        ], heading="Manual de Funciones", classname="collapsible",
            help_text='Manual de Funciones'),
        MultiFieldPanel([
            FieldPanel('salary_links_title'),
            StreamFieldPanel('salary_links')
        ], heading="Salarios", classname="collapsible",
            help_text='Salarios'),
        MultiFieldPanel([
            FieldPanel('post_title'),
            FieldPanel('post_intro'),
            StreamFieldPanel('post_list')
        ], heading="Publicación de la declaración de renta y complementarios de funcionarios públicos", classname="collapsible",
            help_text='Publicación de la declaración de renta y complementarios de funcionarios públicos'),
        MultiFieldPanel([
            FieldPanel('job_title'),
            FieldPanel('job_intro'),
        ], heading="Oferta de empleo", classname="collapsible",
            help_text='Oferta de empleo'),
        MultiFieldPanel([
            FieldPanel('sheets_title'),
            FieldPanel('sheets_intro'),
            StreamFieldPanel('sheets_list'),
        ], heading="Hojas de Vida Aspirantes", classname="collapsible",
            help_text='Hojas de Vida Aspirantes'),
        MultiFieldPanel([
            FieldPanel('text_link'),
            ImageChooserPanel('image_link'),
            StreamFieldPanel('featured_link'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la sección'),
        MultiFieldPanel([
            FieldPanel('sheets_title2'),
            FieldPanel('sheets_intro2'),
            StreamFieldPanel('sheets_list2'),
        ], heading="Vinculación a Terceros – Cancelación del Registro Público de Carrera Administrativa", classname="collapsible",
            help_text='Vinculación a Terceros – Cancelación del Registro Público de Carrera Administrativa'),
        
    ]


class EstrategicoPage(Page):
    subpage_types = ['CulturaCorporativaPage',
                     'HistoriaPage', 'PlanesProgramasPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Estratégico")
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

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),
    ]


class CulturaCorporativaPage(Page):
    subpage_types = []
    corporate_culture = StreamField(
        [('Cultura_Corporativa', CorporateCultureBlock())], blank=True, verbose_name="Cultura Corporativa")

    section_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Objetivos de calidad")

    corporate_culture_objetives = StreamField(
        [('Objetivos_de_Calidad', CorporateCultureObjetivesBlock())], blank=True, verbose_name="Objetivos de Calidad")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('corporate_culture'),
        ], heading="Cultura Corporativa", classname="collapsible",
            help_text="Usted puede crear, modificar, eliminar y organizar los elementos de cultura corporativa del Ministerio de Minas y Energía"),
        MultiFieldPanel([
            FieldPanel('section_title'),
            StreamFieldPanel('corporate_culture_objetives'),
        ], heading="Objetivos de calidad", classname="collapsible",
            help_text="Usted puede crear, modificar, eliminar y organizar los elementos de objetivos de calidad de la cultura corporativa del Ministerio de Minas y Energía"),
    ]


class HistoriaPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Historia")
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

    time_period = StreamField(
        [('Periodo', MinistrosBlock())], blank=True, verbose_name="Ministros de la entidad")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image')
        ], heading="Historia", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel('time_period'),
        ], heading="Ministros de la entidad", classname="collapsible ",
            help_text='Ministros de la entidad'),

    ]


class DocumentoSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def get_document(self, docs, id):
        for i in docs:
            if i.id == id:
                return "/documents/%s/%s" % (id, i.title.replace(' ', '_'))

    def to_representation(self, value):
        """Return the Documento URL and title """
        docs = Document.objects.all()
        data = value.stream_block.get_api_representation(value, self.context)

        for i in data:
            subitems = i['value']['subitems']
            for j in subitems:
                documents_block = j['documents_block']
                #documents = j['documents_block']['documents']
                for k in documents_block:
                    documents = k['documents']
                    for l in documents:
                        l['document'] = self.get_document(docs, l['document'])

        return data


class PlanesProgramasPage(Page):
    subpage_types = ['HistoricoPlaneacionEstrategicaSectorialPage',
                     'HistoricoPlanesAccionAnualPage', 'PlanInstitucionalArchivosEntidadPINARPage', 'PlanAnualAdquisicionesPage', 'PlanAnualVacantesPage', 'PlanPrevisionRecursoHumanosPage', 'PlanEstrategicoTalentoHumanoPage', 'PlanEstrategicoTecnologiaInformacionComunicacionesPage', 'PlanTratamientoRiesgosSeguridadPrivacidadInformacionPage', 'PlanSeguridadPrivacidadInformacionPage', 'PlanInstitucionalCapacitacionPage', 'PlanBienestarSocialIncentivosInstitucionalesPage', 'PlanAnualSeguridadSaludTrabajoPage', 'PlanAnticorrupcionAtencionCiudadanoPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Planes y programas")

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

    objetive_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Planeación Estratégica")

    objetive_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    objetive_list = StreamField(
        [('Objetivos', ElementsListStructBlock())], blank=True, verbose_name="Lista de objetivos")

    plans_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Planes y Programas")

    plans_list = StreamField(
        [('Objetivos', BriefcaseMenuAccodeonStructBlock())], blank=True, verbose_name="Lista de objetivos")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),

        MultiFieldPanel([
            FieldPanel('objetive_title'),
            FieldPanel('objetive_intro'),
            StreamFieldPanel('objetive_list'),
        ], heading="Planeación Estratégica", classname="collapsible",
            help_text='Planeación Estratégica'),

        MultiFieldPanel([
            FieldPanel('plans_title'),
            StreamFieldPanel('plans_list'),
        ], heading="Planes y Programas", classname="collapsible",
            help_text='Planes y Programas'),
    ]

    api_fields = [
        APIField('plans_list', DocumentoSerializedField()),

    ]


class HistoricoPlaneacionEstrategicaSectorialPage(Page):
    subpage_types = []

    data_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Planeación Estratégica Sectorial", classname="collapsible",
            help_text='Histórico Planeación Estratégica Sectorial'),
    ]


class HistoricoPlanesAccionAnualPage(Page):
    subpage_types = []

    data_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Planes de Acción Anual", classname="collapsible",
            help_text='Histórico Planes de Acción Anual'),
    ]


class PlanInstitucionalArchivosEntidadPINARPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Plan Anual de Abastecimiento Estratégico", classname="collapsible",
            help_text='Plan Anual de Abastecimiento Estratégico'),
    ]


class PlanAnualAdquisicionesPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la sección")

    data_list = StreamField(
        [('Planes', SimpleIconBriefcaseStructBlock())], blank=True, verbose_name="Planes")

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('intro'),
            StreamFieldPanel('link_list'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción'),

        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Plan Anual de Abastecimiento Estratégico", classname="collapsible",
            help_text='Plan Anual de Abastecimiento Estratégico'),

        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Planes de Adquisiciones", classname="collapsible",
            help_text='Histórico Planes de Adquisiciones'),
    ]


class PlanAnualVacantesPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan Anual de Vacantes", classname="collapsible",
            help_text='Histórico Plan Anual de Vacantes'),
    ]


class PlanPrevisionRecursoHumanosPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan de Previsión de Recursos Humanos", classname="collapsible",
            help_text='Histórico Plan de Previsión de Recursos Humanos'),
    ]


class PlanEstrategicoTalentoHumanoPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan Estratégico de Talento Humano", classname="collapsible",
            help_text='Histórico Plan Estratégico de Talento Humano'),
    ]


class PlanEstrategicoTecnologiaInformacionComunicacionesPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan Estratégico", classname="collapsible",
            help_text='Histórico Plan Estratégico'),
    ]


class PlanTratamientoRiesgosSeguridadPrivacidadInformacionPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan de Tratamiento de Riesgos de Seguridad y PI", classname="collapsible",
            help_text='Histórico Plan de Tratamiento de Riesgos de Seguridad y PI'),
    ]


class PlanSeguridadPrivacidadInformacionPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    data_list = StreamField(
        [('Lista', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Histórico Plan de Seguridad y Privacidad de la Información", classname="collapsible",
            help_text='Histórico Plan de Seguridad y Privacidad de la Información'),
    ]


class PlanInstitucionalCapacitacionPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Plan Institucional de Capacitación - PIC", classname="collapsible",
            help_text='Histórico Plan Institucional de Capacitación - PIC'),
    ]


class PlanBienestarSocialIncentivosInstitucionalesPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Plan de Bienestar Social e Incentivos Institucionales", classname="collapsible",
            help_text='Histórico Plan de Bienestar Social e Incentivos Institucionales'),
    ]


class PlanAnualSeguridadSaludTrabajoPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Plan Anual en Seguridad y Salud en el Trabajo", classname="collapsible",
            help_text='Histórico Plan Anual en Seguridad y Salud en el Trabajo'),
    ]


class PlanAnticorrupcionAtencionCiudadanoPage(Page):
    subpage_types = []

    plans_list = StreamField(
        [('Planes', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Planes")
    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('plans_list'),
        ], heading="Planes", classname="collapsible",
            help_text='Lista de planes'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Plan Anticorrupción y de Atención al Ciudadano", classname="collapsible",
            help_text='Histórico Plan Anticorrupción y de Atención al Ciudadano'),
    ]


class GestionPage(Page):
    subpage_types = ['GestionDeLaInformacionPage',
                     'MipgPage', 'ContratacionPage', 'presupuestoPage', 'ControlInternoPage', 'ProyectosInversionPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Gestión")
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

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),
    ]


class GestionDeLaInformacionPage(Page):
    subpage_types = ['TransformacionDigitalPage', 'DatosAbiertosPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Gestión de la Información")
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

    elements_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Sistemas de información misional")
    elements = StreamField(
        [('Elementos', InformationManagementBlock())], blank=True, verbose_name="Sistemas de información")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Gestión de la Información", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('elements_title'),
            StreamFieldPanel('elements'),
        ], heading="Elementos de información", classname="collapsible",
            help_text="Ingrese los elementos informativos"),
    ]


class ProyectosInversionPage(Page):
    subpage_types = []
    """ First section """
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Proyectos de Inversión")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+')

    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    """ First section """

    """ Second section """
    assignment_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Informes de Asignación Presupuestal")

    assignment_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    assignment_list = StreamField(
        [('Documento', DocumentSimpleListStructBlock())], blank=True, verbose_name="Documentos")

    """ Second section """

    """ Third section """
    follow_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Informes de Seguimiento - Proyectos de Inversión")

    follow_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Acordeón")

    """ Third section """
    execution_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Ejecución Presupuestal de Inversión Sector Minas y Energía")

    execution_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    execution_list = StreamField(
        [('Elementos', IconDocumentListTabStructBlock())], blank=True, verbose_name="Elementos")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Control Interno", classname="collapsible",
            help_text='Control Interno'),
        MultiFieldPanel([
            FieldPanel('assignment_title'),
            FieldPanel('assignment_intro'),
            StreamFieldPanel('assignment_list'),
        ], heading="Informes de Asignación Presupuestal", classname="collapsible",
            help_text='Informes de Asignación Presupuestal'),
        MultiFieldPanel([
            FieldPanel('follow_title'),
            StreamFieldPanel('follow_list'),
        ], heading="Informes de Seguimiento - Proyectos de Inversión", classname="collapsible",
            help_text='Informes de Seguimiento - Proyectos de Inversión'),
        MultiFieldPanel([
            FieldPanel('execution_title'),
            FieldPanel('execution_intro'),
            StreamFieldPanel('execution_list'),
        ], heading="Ejecución Presupuestal de Inversión Sector Minas y Energía", classname="collapsible",
            help_text='Ejecución Presupuestal de Inversión Sector Minas y Energía'),

    ]


class ControlInternoPage(Page):
    subpage_types = ['AuditoriaInternaIndependientePage',
                     'AuditoriaIndependientePage', 'ComiteCoordinacionControInternoMinisterioPage', 'ComiteCoordinacionControInternoSectorMineroEnergeticoPage', 'DocumentosSeguimientoPage', 'PlanAccionAnualPage', 'ProgramaAuditoriaInternaIndependientePage']
    """ First section """
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Control Interno")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+')

    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    """ First section """

    """ Second section """
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    management_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    management_list = StreamField(
        [('Gestion', TabsListStructBlock())], blank=True, verbose_name="Gestión del Control Interno")

    """ Second section """

    """ Third section """
    planning_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Planeación de la Gestión Independiente")

    planning_cards = StreamField(
        [('Tarjetas', SecondLinkStructBlock())], blank=True, verbose_name="Planeación de la Gestión Independiente")

    code_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    code_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="Documento",
        on_delete=models.SET_NULL,
        related_name='+'
    )
    """ Third section """

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Control Interno", classname="collapsible",
            help_text='Control Interno'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios'),

        MultiFieldPanel([
            FieldPanel('management_list_title'),
            StreamFieldPanel('management_list'),
        ], heading="Gestión del Control Interno", classname="collapsible",
            help_text='Gestión del Control Interno'),

        MultiFieldPanel([
            FieldPanel('planning_title'),
            StreamFieldPanel('planning_cards'),
        ], heading="Planeación de la Gestión Independiente", classname="collapsible",
            help_text='Planeación de la Gestión Independiente'),

        MultiFieldPanel([
            FieldPanel('code_list_title'),
            FieldPanel('code_intro'),
            DocumentChooserPanel('document_file'),
        ], heading="Código de Ética y Estatuto de la Oficina de Control Interno", classname="collapsible",
            help_text='Código de Ética y Estatuto de la Oficina de Control Interno'),

    ]


class AuditoriaInternaIndependientePage(Page):
    subpage_types = []
    general_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    general_tabs_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Pestañas")

    assigned_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    assigned_tabs_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Acordeón")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('general_tabs_list_title'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Auditoría Interna Independiente", classname="collapsible",
            help_text='Auditoría Interna Independiente'),
        MultiFieldPanel([
            FieldPanel('assigned_tabs_list_title'),
            StreamFieldPanel('assigned_tabs_list'),
        ], heading="Histórico de Auditorías Interna Independientes y un nuevo acordeón", classname="collapsible",
            help_text='Histórico de Auditorías Interna Independientes y un nuevo acordeón'),

    ]


class DocumentosSeguimientoPage(Page):
    subpage_types = []
    general_tabs_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('general_tabs_list'),
        ], heading="Documentos de Seguimiento", classname="collapsible",
            help_text='Documentos de Seguimiento'),
    ]


class AuditoriaIndependientePage(Page):
    subpage_types = []
    general_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    general_tabs_list = StreamField(
        [('Elementos', IconDocumentBriefcaseStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('general_tabs_list_title'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Auditoría Independiente", classname="collapsible",
            help_text='Actas de Reunión'),

    ]


class ComiteCoordinacionControInternoMinisterioPage(Page):
    subpage_types = []
    general_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    general_tabs_list = StreamField(
        [('Elementos', IconDocumentListStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('general_tabs_list_title'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Lista de elementos", classname="collapsible",
            help_text='Actas de Reunión'),

    ]


class ComiteCoordinacionControInternoSectorMineroEnergeticoPage(Page):
    subpage_types = []
    general_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    general_tabs_list = StreamField(
        [('Elementos', IconDocumentListStructBlock())], blank=True, verbose_name="Pestañas")

    second_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    second_tabs_list = StreamField(
        [('Elementos', IconDocumentListStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('general_tabs_list_title'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Lista de elementos", classname="collapsible",
            help_text='Actas de Reunión'),
        MultiFieldPanel([
            FieldPanel('second_tabs_list_title'),
            StreamFieldPanel('second_tabs_list'),
        ], heading="Lista de elementos", classname="collapsible",
            help_text='Actas de Reunión'),

    ]


class PlanAccionAnualPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    data_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('intro'),
            StreamFieldPanel('data_list'),
        ], heading="Plan de Acción Anual - PAA", classname="collapsible",
            help_text='Plan de Acción Anual - PAA'),
    ]


class ProgramaAuditoriaInternaIndependientePage(Page):
    subpage_types = []

    data_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('data_list'),
        ], heading="Programa de Auditoría Interna Independiente - PAII", classname="collapsible",
            help_text='Programa de Auditoría Interna Independiente - PAII'),
    ]


# Modelo Integrado de Planeación y Gestión
class MipgPage(Page):
    subpage_types = [
        'ComiteInstitucionalGestionDesempenoPage', 'ComiteSectorialPage', 'PoliticasObjetivosCalidadPage', 'AvanceSeguimientoMipgPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Procesos")
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
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Procesos")
    items_list = StreamField(
        [('Lista', SubitemsBriefcaseStructBlock())], blank=True, verbose_name="Lista")
    systems = StreamField(
        [('sistemas', ProcessBlock())], blank=True, verbose_name="Sistemas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('button_title'),
            FieldPanel('link_mapa'),
            DocumentChooserPanel('document_mapa'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Modelo Integrado de Planeación y Gestión", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel('items_list'),
        ], heading="Elementos", classname="collapsible",
            help_text="Elementos"),
        MultiFieldPanel([
            StreamFieldPanel('systems'),
        ], heading="Procesos", classname="collapsible",
            help_text="Sistemas externos")
    ]


class ComiteInstitucionalGestionDesempenoPage(Page):
    subpage_types = []

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [


        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Comité Institucional de Gestión y Desempeño", classname="collapsible",
            help_text='Comité Institucional de Gestión y Desempeño'),
    ]


class ComiteSectorialPage(Page):
    subpage_types = []

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [


        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Comité Sectorial", classname="collapsible",
            help_text='Comité Sectorial'),
    ]


class AvanceSeguimientoMipgPage(Page):
    subpage_types = ['PresentacionIndexPage', 'ResultadosIndexPage']

    presentations_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    presentations_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de presentaciones',
        verbose_name='Índice de presentacion'
    )

    presentations_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    results_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    results_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la página del índice de resultados',
        verbose_name='Índice de presentacion'
    )

    results_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
        verbose_name='Título botón más información'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('presentations_title'),
            PageChooserPanel('presentations_list'),
            FieldPanel('presentations_button_title')
        ], heading="Presentaciones", classname="collapsible",
            help_text='Presentaciones'),
        MultiFieldPanel([
            FieldPanel('results_title'),
            PageChooserPanel('results_list'),
            FieldPanel('results_button_title')
        ], heading="Resultados", classname="collapsible",
            help_text='Resultados'),
    ]


class PoliticasObjetivosCalidadPage(Page):
    subpage_types = []

    politics_title = models.CharField(
        "Subtítulo de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Política de Calidad")

    politics_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción")

    quality_objectives_title = models.CharField(
        "Subtítulo de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Política de Calidad")

    quality_objectives = StreamField(
        [('Objetivos', TabsListStructBlock())], blank=True, verbose_name="Objetivos de calidad")

    process_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Procesos y Procedimientos")

    process_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    process_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    process_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                        help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    manual_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Manual de Calidad ")

    manual_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    manual_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    manual_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    risk_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Riesgos")

    risk_list = StreamField(
        [('Documentos', SecondLinkDocuemntStructBlock())], blank=True, verbose_name="Documentos")

    risk_block_one = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección uno',
        verbose_name="Introducción uno"
    )
    risk_block_two = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección dos',
        verbose_name="Introducción dos"
    )

    risk_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    risk_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                     help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    monitoring_list = StreamField(
        [('Seguimiento', AccordeonRichTextStructBlock())], blank=True, verbose_name="Seguimiento Mapa de Riesgos")

    monitoring_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Seguimiento Mapa de Riesgos")

    monitoring_main = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección uno',
        verbose_name="Introducción uno"
    )
    monitoring_second = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección dos',
        verbose_name="Introducción dos"
    )

    plan_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Plan de Mejoramiento por Procesos")

    plan_main_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección uno',
        verbose_name="Introducción uno"
    )
    plan_second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección dos',
        verbose_name="Introducción dos"
    )

    plan_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    plan_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                     help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    plan_link = models.URLField(
        "Enlace", blank=True, help_text='Enlace aplicativo',)

    plan_list = StreamField(
        [('Planes', AccordeonRichTextStructBlock())], blank=True, verbose_name="Plan de Mejoramiento por Procesos")

    plan_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    audit_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Auditorías")

    audit_list = StreamField(
        [('Auditoria', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Auditoías")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('politics_title'),
            FieldPanel('politics_intro'),
        ], heading="Política de Calidad", classname="collapsible",
            help_text='Política de Calidad'),
        MultiFieldPanel([
            FieldPanel('quality_objectives_title'),
            StreamFieldPanel('quality_objectives'),
        ], heading="Objetivos de calidad", classname="collapsible",
            help_text='Objetivos de calidad'),
        MultiFieldPanel([
            FieldPanel('process_intro_title'),
            FieldPanel('process_intro'),
            ImageChooserPanel('process_image'),
            FieldPanel('process_alt_text'),
        ], heading="Procesos y Procedimientos", classname="collapsible",
            help_text='Procesos y Procedimientos'),
        MultiFieldPanel([
            FieldPanel('manual_intro_title'),
            FieldPanel('manual_intro'),
            ImageChooserPanel('manual_image'),
            FieldPanel('manual_alt_text'),
        ], heading="Manual de Calidad ", classname="collapsible",
            help_text='Manual de Calidad '),
        MultiFieldPanel([
            FieldPanel('risk_intro_title'),
            FieldPanel('risk_block_one'),
            StreamFieldPanel('risk_list'),
            FieldPanel('risk_block_two'),
            ImageChooserPanel('risk_image'),
            FieldPanel('risk_alt_text'),
        ], heading="Riesgos", classname="collapsible",
            help_text='Riesgos'),
        MultiFieldPanel([
            StreamFieldPanel('monitoring_list'),
            FieldPanel('monitoring_title'),
            FieldPanel('monitoring_main'),
            FieldPanel('monitoring_second'),
        ], heading="Seguimiento Mapa de Riesgos", classname="collapsible",
            help_text='Seguimiento Mapa de Riesgos'),
        MultiFieldPanel([
            FieldPanel('plan_title'),
            FieldPanel('plan_main_intro'),
            FieldPanel('plan_second_intro'),
            ImageChooserPanel('plan_image'),
            FieldPanel('plan_alt_text'),
            FieldPanel('plan_link'),
            StreamFieldPanel('plan_list'),
            FieldPanel('plan_video'),
        ], heading="Plan de Mejoramiento por Procesos", classname="collapsible",
            help_text='Plan de Mejoramiento por Procesos'),
        MultiFieldPanel([
            FieldPanel('audit_title'),
            StreamFieldPanel('audit_list')
        ], heading="Auditorías", classname="collapsible",
            help_text='Auditorías'),
    ]


class ContratacionPage(Page):
    subpage_types = ["HistoricoContratacionPage"]
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Contratación")
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

    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la sección")

    """ Second section """
    second_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Proceso de contratación")

    second_subtitle = models.CharField(
        "Subtítulo de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Gestión por Estructuración")

    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    """ Second section """

    """ Third section """
    third_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Plan Anual de Adquisiciones")

    third_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    third_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    third_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    external_link = models.URLField(
        "Link_página_externa", blank=True, help_text='Enlace a página externa',)
    """ Third section """

    """ Fourth section """
    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    tab_list = StreamField(
        [('Planes', TabsListStructBlock())], blank=True, verbose_name="Plan Anual de Abastecimiento Estratégico")

    accordion_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    accordion_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acordeón")

    """ Fifth section """
    amounts_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    amounts_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    amounts_logo = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del componente en formato SVG',
        verbose_name="Icono"
    )
    amounts_list = StreamField(
        [('Documento', DocumentSimpleListStructBlock())], blank=True, verbose_name="Documentos")

    """ Fifth section """

    """ PBI section """
    pbi_intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Procesos adjudicados y convocados")

    pbi_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    pbi_endpoint = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)

    pbi_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    pbi_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    """ PBI section """

    """ Menu section """
    menu_list = StreamField(
        [('Menu', SimpleBriefcaseStructBlock1())], blank=True, verbose_name="Items")
    """ Menu section """

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Contratación", classname="collapsible",
            help_text='Indroducción Contratación'),

        MultiFieldPanel([
            StreamFieldPanel('link_list'),
        ], heading="Enlaces", classname="collapsible",
            help_text='Listas de enlaces'),

        MultiFieldPanel([
            FieldPanel('second_intro_title'),
            FieldPanel('second_subtitle'),
            FieldPanel('second_intro'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Proceso de contratación", classname="collapsible",
            help_text='Indroducción Proceso de contratación'),

        MultiFieldPanel([
            FieldPanel('third_intro_title'),
            FieldPanel('third_intro'),
            ImageChooserPanel('third_image'),
            FieldPanel('third_alt_text'),
            FieldPanel('external_link'),
        ], heading="Plan Anual de Adquisiciones", classname="collapsible",
            help_text='Indroducción Plan Anual de Adquisiciones'),

        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            StreamFieldPanel('tab_list'),
        ], heading="Plan Anual de Abastecimiento Estratégico", classname="collapsible",
            help_text='Plan Anual de Abastecimiento Estratégico'),

        MultiFieldPanel([
            FieldPanel('accordion_list_title'),
            StreamFieldPanel('accordion_list'),
        ], heading="Histórico Plan Anual de Adquisiciones por Vigencias", classname="collapsible",
            help_text='Histórico Plan Anual de Adquisiciones por Vigencias'),

        MultiFieldPanel([
            FieldPanel('amounts_list_title'),
            SvgChooserPanel('amounts_logo'),
            FieldPanel('amounts_intro'),
            StreamFieldPanel('amounts_list'),
        ], heading="Cuantías de contratación", classname="collapsible",
            help_text='Cuantías de contratación'),

        MultiFieldPanel([
            FieldPanel('pbi_intro_title'),
            FieldPanel('pbi_intro'),
            FieldPanel('pbi_endpoint'),
            ImageChooserPanel('pbi_image'),
            FieldPanel('pbi_alt_text'),
        ], heading="Procesos adjudicados y convocados", classname="collapsible",
            help_text='Procesos adjudicados y convocados'),

        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Lista de elementos", classname="collapsible",
            help_text='Lista de elementos'),

    ]


class presupuestoPage(Page):

    subpage_types = ['presupuestoGeneralAsignadoPage',
                     'ejecucionPresupuestalPage', 'EstadosFinancierosPage', 'BajaEnajenacionBienesPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Presupuesto")
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

    card_list = StreamField(
        [('Tarjetas', SecondLinkStructBlock())], blank=True, verbose_name="Lista de tarjetas")

    tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    tabs_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Gestión Financiera y Contable")

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
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('card_list'),
        ], heading="Tarjetas", classname="collapsible",
            help_text='Tarjetas'),
        MultiFieldPanel([
            FieldPanel('tabs_list_title'),
            StreamFieldPanel('tabs_list'),
        ], heading="Gestión Financiera y Contable", classname="collapsible",
            help_text='Gestión Financiera y Contableicios'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Baja y Enajenación de Bienes", classname="collapsible",
            help_text='Baja y Enajenación de Bienes'),
    ]


class presupuestoGeneralAsignadoPage(Page):
    subpage_types = []
    general_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    general_tabs_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Pestañas")

    assigned_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    assigned_tabs_list = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('general_tabs_list_title'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Gestión Financiera y Contable", classname="collapsible",
            help_text='Presupuesto General Asignado del Ministerio de Minas y Energía'),
        MultiFieldPanel([
            FieldPanel('assigned_tabs_list_title'),
            StreamFieldPanel('assigned_tabs_list'),
        ], heading="Gestión Financiera y Contable", classname="collapsible",
            help_text='Presupuesto Asignado del Sistema General de Regalías'),

    ]


class ejecucionPresupuestalPage(Page):
    subpage_types = []
    reports_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    reports_tabs_list = StreamField(
        [('Elementos', BudgetExecutionTabStructBlock())], blank=True, verbose_name="Pestañas")

    system_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    system_list = StreamField(
        [('Elementos', DocumentBriefcaseStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('reports_tabs_list_title'),
            StreamFieldPanel('reports_tabs_list'),
        ], heading="Informes de Ejecución Presupuestal", classname="collapsible",
            help_text='Informes de Ejecución Presupuestal'),
        MultiFieldPanel([
            FieldPanel('system_list_title'),
            StreamFieldPanel('system_list'),
        ], heading="Sistema General de Regalías", classname="collapsible",
            help_text='Sistema General de Regalías - Ministerio de Minas y Energía'),

    ]


class EstadosFinancierosPage(Page):
    subpage_types = []
    reports_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    reports_tabs_list = StreamField(
        [('Elementos', DocumentBriefcaseStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('reports_tabs_list_title'),
            StreamFieldPanel('reports_tabs_list'),
        ], heading="Balances de Gestión Financiera", classname="collapsible",
            help_text='Balances de Gestión Financiera'),
    ]


class BajaEnajenacionBienesPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Baja y enajenación de bienes")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    tabs_list = StreamField(
        [('Elementos', AlienationTabStructBlock())], blank=True, verbose_name="Pestañas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            StreamFieldPanel('tabs_list'),
        ], heading="Baja y enajenación de bienes", classname="collapsible",
            help_text='Baja y enajenación de bienes'),
    ]


""" Presentaciones y resultados MIPG """


class PresentacionAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'PresentacionPage', related_name='presentacion_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_presentacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class PresentacionSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'PresentacionPage', related_name='presentacion_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_presentacion_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class PresentacionPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'PresentacionPage', related_name='tagged_items', on_delete=models.CASCADE)


class PresentacionSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Presentacion URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class PresentacionPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la presentación',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen de la presentación",
        help_text='Imagen de presentación para la presentación'
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
    tags = ClusterTaggableManager(through=PresentacionPageTag, blank=False)
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
            'presentacion_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'presentacion_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.presentacion_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.presentacion_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.presentacion_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.presentacion_autor_relationship.all()
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

    parent_page_types = ['PresentacionIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', PresentacionSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class PresentacionIndexPage(RoutablePageMixin, Page):

    subpage_types = ['PresentacionPage']

    def children(self):
        return PresentacionPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(PresentacionIndexPage, self).get_context(request)
        context['posts'] = PresentacionPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = PresentacionPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class ResultadosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ResultadosPage', related_name='resultados_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_resultados_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ResultadosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ResultadosPage', related_name='resultados_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_resultados_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ResultadosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ResultadosPage', related_name='tagged_items', on_delete=models.CASCADE)


class ResultadosSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Resultados URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ResultadosPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe el resultado',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen de la presentación",
        help_text='Imagen de presentación para del resultado'
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
    tags = ClusterTaggableManager(through=ResultadosPageTag, blank=False)
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
            'resultados_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'resultados_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.resultados_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.resultados_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.resultados_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.resultados_autor_relationship.all()
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

    parent_page_types = ['ResultadosIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', ResultadosSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class ResultadosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['ResultadosPage']

    def children(self):
        return ResultadosPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(ResultadosIndexPage, self).get_context(request)
        context['posts'] = ResultadosPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = ResultadosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Presentaciones y resultados MIPG """



class TransformacionDigitalPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Transformación Digital")
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

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),

    ]


class DatosAbiertosPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Datos abiertos")
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

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            FieldPanel('second_intro'),
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),

    ]

class HistoricoContratacionPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Titulo")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    # link_video = models.URLField(
    #     "Video", blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     verbose_name="Imagen",
    #     help_text='Imagen que representa la sección',
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )
    # alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
    #                             help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Historico")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            # FieldPanel('link_video'),
            # ImageChooserPanel('image'),
            # FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Rendición de cuentas'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Historico", classname="collapsible",
            help_text='Historico'),


    ]