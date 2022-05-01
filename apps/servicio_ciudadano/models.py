from django.db import models
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel
)
from wagtail.search import index
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from taggit.models import Tag, TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from .blocks import SliderStructBlock, ParticipationListStructBlock, IconMenuStructBlock, HeaderMenuBlock
from ..common.blocks import ElementsListStructBlock, TabsListStructBlock, BriefcaseStructBlock
from ..common.models import Autor, Sector
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from rest_framework.fields import Field
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtailsvg.models import Svg
from ..common.models import Autor, Sector
from ..common.blocks import IconDocumentMenuStructBlock, DocumentRetentionTableStructBlock, SimpleBriefcaseStructBlock, AccordeonRichTextStructBlock, SecondLinkStructBlock, AccodionRichTextStructBlock


class servicioCiudanoPage(Page):
    subpage_types = ['planAnticorrucionPage',
                     'eventosPage', 'PlanParticipacionCiudadanaPage', 'rendicionCuentasPage', 'ForosIndexPage', 'CaracterizacionUsuariosPage', 'MecanismosProteccionDerechosCiudadanosPage', 'InformeMecanismosParticipacionPage', 'PqrsPage']

    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Servicio al ciudadano")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    slider = StreamField(
        [('slider', SliderStructBlock())], blank=True, verbose_name="Slider")

    channel_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    channel_list = StreamField(
        [('Canales', ElementsListStructBlock())], blank=True, verbose_name="Canales de atención")

    participation_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    participation_list = StreamField(
        [('Mencanismos', ParticipationListStructBlock())], blank=True, verbose_name="Mecanismos de participación")

    services_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    services_list = StreamField(
        [('Servicios', TabsListStructBlock())], blank=True, verbose_name="Servicios")

    briefcase_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    briefcase_list = StreamField(
        [('Portafolio', BriefcaseStructBlock())], blank=True, verbose_name="Portafolio, políticas y protocolos de servicio")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            StreamFieldPanel('slider'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Servicio al ciudadano'),
        MultiFieldPanel([
            FieldPanel('channel_list_title'),
            StreamFieldPanel('channel_list'),
        ], heading="Canales de atención", classname="collapsible",
            help_text='Canales de atención'),
        MultiFieldPanel([
            FieldPanel('participation_list_title'),
            StreamFieldPanel('participation_list'),
        ], heading="Mecanismos de participación", classname="collapsible",
            help_text='Mecanismos de participación'),
        MultiFieldPanel([
            FieldPanel('services_list_title'),
            StreamFieldPanel('services_list'),
        ], heading="Servicios", classname="collapsible",
            help_text='Servicios'),
        MultiFieldPanel([
            FieldPanel('briefcase_list_title'),
            StreamFieldPanel('briefcase_list'),
        ], heading="Portafolio, políticas y protocolos de servicio", classname="collapsible",
            help_text='Portafolio, políticas y protocolos de servicio'),

    ]


class planAnticorrucionPage(Page):
    subpage_types = ['InstrumentosArchivisticosPage',
                     'InstrumentosGestionInformacionPage', 'TablaRetencionDocumentalPage', 'AcordeonPage']

    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Plan Anticorrupción y atención al ciudadano")

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

    plans_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    plans_list = StreamField(
        [('Planes', TabsListStructBlock())], blank=True, verbose_name="Plan anticorrupción")

    reports_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    reports_list = StreamField(
        [('Informes', TabsListStructBlock())], blank=True, verbose_name="Informes y publicaciones")

    elements_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    elements_list = StreamField(
        [('Estudios', ElementsListStructBlock())], blank=True, verbose_name="Estudios, investigaciones y otras publicaciones")

    management_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    management_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    management_list = StreamField(
        [('Items', TabsListStructBlock())], blank=True, verbose_name="Gestión Documental")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image')
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Plan Anticorrupción y atención al ciudadano'),
        MultiFieldPanel([
            FieldPanel('plans_list_title'),
            StreamFieldPanel('plans_list'),
        ], heading="Plan anticorrupción", classname="collapsible",
            help_text='Plan anticorrupción'),
        MultiFieldPanel([
            FieldPanel('reports_list_title'),
            StreamFieldPanel('reports_list'),
        ], heading="Informes y publicaciones", classname="collapsible",
            help_text='Informes y publicaciones'),
        MultiFieldPanel([
            FieldPanel('elements_list_title'),
            StreamFieldPanel('elements_list'),
        ], heading="Estudios, investigaciones y otras publicaciones", classname="collapsible",
            help_text='Estudios, investigaciones y otras publicaciones'),
        MultiFieldPanel([
            FieldPanel('management_list_title'),
            FieldPanel('management_intro'),
            StreamFieldPanel('management_list'),
        ], heading="Gestión Documental", classname="collapsible",
            help_text='Gestión Documental'),

    ]


class AcordeonPage(Page):
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
        ], heading="Acordeón de elementos", classname="collapsible",
            help_text='Acordeón de elementos'),
    ]


class InstrumentosArchivisticosPage(Page):
    subpage_types = []
    menu_list = StreamField(
        [('Elementos', IconDocumentMenuStructBlock())], blank=True, verbose_name="Instrumentos archivísticos")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Instrumentos archivísticos'),
    ]


class InstrumentosGestionInformacionPage(Page):
    subpage_types = []
    menu_list = StreamField(
        [('Elementos', IconDocumentMenuStructBlock())], blank=True, verbose_name="Instrumentos Gestión de la Información")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Instrumentos archivísticos'),
    ]


class TablaRetencionDocumentalPage(Page):
    subpage_types = []
    table_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Codificación Estructura Organizacional del Ministerio de Minas y Energía")

    table = StreamField(
        [('Elementos', DocumentRetentionTableStructBlock())], blank=True, verbose_name="Codificación Estructura Organizacional")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('table_title'),
            StreamFieldPanel('table'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Codificación Estructura Organizacional'),
    ]


class eventosPage(Page):
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

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    history_icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono',
        verbose_name="Icono"
    )
    history = RichTextField(
        null=True,
        blank=True,
        help_text='Historico de cronogramas',
        verbose_name="Historico de cronogramas"
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('events_list_title'), PageChooserPanel('events_list'), FieldPanel('events_button_title'), ]),
        ], heading="Eventos", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Cronogramas", classname="collapsible",
            help_text='Cronogramas'),
        MultiFieldPanel([
            SvgChooserPanel('history_icon'),
            FieldPanel('history'),
        ], heading="Historico de cronogramas", classname="collapsible",
            help_text='Historico de cronogramas'),

    ]
class PlanParticipacionCiudadanaPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
   
    assigned_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acordeón")
       
    content_panels = Page.content_panels + [
        
        MultiFieldPanel([            
            StreamFieldPanel('assigned_tabs_list'),
        ], heading="Plan de Participación Ciudadana", classname="collapsible",
            help_text='Plan de Participacón Ciudadana'),
        
    ]

class CaracterizacionUsuariosPage(Page):
    subpage_types = []
    elements_list = StreamField(
        [('Items', IconMenuStructBlock())], blank=True, verbose_name="Items")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('elements_list'),
        ], heading="Items", classname="collapsible",
            help_text='Elementos de la página'),
    ]


class rendicionCuentasPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Rendición de cuentas")

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

    tab_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    plans_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    current_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Rendición de Cuentas")

    current_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la sección',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    current_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                        help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    current_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    questions_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Preguntas y respuestas")

    questions_list = StreamField(
        [('Preguntas', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Preguntas")

    general_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Rendición de Cuentas")

    general_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    general_block_one = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Uno',
        verbose_name="Bloque Uno"
    )
    general_block_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Dos',
        verbose_name="Bloque Dos"
    )

    historical_list = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Histórico Rendición de cuentas")

    control_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Control Social")

    control_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Dos',
        verbose_name="Bloque Dos"
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
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('tab_intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Rendición de cuentas'),
        MultiFieldPanel([
            FieldPanel('tab_intro'),
            StreamFieldPanel('plans_list'),
        ], heading="Pestañas", classname="collapsible",
            help_text='Pestañas de elementos'),
        MultiFieldPanel([
            FieldPanel('current_title'),
            ImageChooserPanel('current_image'),
            FieldPanel('current_alt_text'),
            FieldPanel('current_intro'),
        ], heading="Rendición de Cuentas Actual", classname="collapsible",
            help_text='Rendición de Cuentas Actual'),
        MultiFieldPanel([
            FieldPanel('questions_title'),
            StreamFieldPanel('questions_list'),
        ], heading="Preguntas", classname="collapsible",
            help_text='Preguntas'),
        MultiFieldPanel([
            FieldPanel('general_title'),
            FieldPanel('general_video'),
            FieldPanel('general_block_one'),
            FieldPanel('general_block_two'),
        ], heading="Rendición de Cuentas General", classname="collapsible",
            help_text='Rendición de Cuentas Actual General'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Rendición de cuentas", classname="collapsible",
            help_text='Histórico Rendición de cuentas'),
        MultiFieldPanel([
            FieldPanel('control_title'),
            FieldPanel('control_intro'),
            DocumentChooserPanel('document_file'),
        ], heading="Histórico Rendición de cuentas", classname="collapsible",
            help_text='Histórico Rendición de cuentas'),

    ]


class ForosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ForosPage', related_name='foros_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_foros_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ForosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ForosPage', related_name='foros_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_foros_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ForosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ForosPage', related_name='tagged_items', on_delete=models.CASCADE)


class ForosSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Foros URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ForosPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe foro',
        blank=False,
        verbose_name="Introducción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen del foro",
        help_text='Imagen de presentación para el foro'
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Documento del foro",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=ForosPageTag, blank=False)
    start_date = models.DateField(
        "Fecha Inicio", blank=False, null=False
    )
    end_date = models.DateField(
        "Fecha Fin", blank=False, null=False
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        DocumentChooserPanel('document_file'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'foros_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'foros_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.foros_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.foros_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.foros_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.foros_autor_relationship.all()
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

    parent_page_types = ['ForosIndexPage']

    subpage_types = []

    api_fields = [
        APIField('start_date'),
        APIField('end_date'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', ForosSerializedField()),
    ]


class ForosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['ForosPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Foros")
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

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image')
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
    ]

    def children(self):
        return ForosPage.objects.descendant_of(self).live().order_by('-start_date')

    def get_context(self, request):
        context = super(ForosIndexPage, self).get_context(request)
        context['posts'] = ForosPage.objects.descendant_of(
            self).live().order_by(
            '-start_date')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = ForosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class MecanismosProteccionDerechosCiudadanosPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Mecanismos para la protección de los Derechos Ciudadanos")

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

    request_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Peticiones, Quejas, Reclamos y Denuncias - PQRD")
    request_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    request_list = StreamField(
        [('Elementos', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Elemento")

    others_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Otros mecanismos constitucionales para la protección de los derechos ciudadanos")
    others_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    mechanisms_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Mecanismos de participación")

    mechanisms_list = StreamField(
        [('Mecanismos', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Mecanismos de participación")

    control_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Mecanismos de Control Ciudadano para la Vigilancia de la Gestión Pública")

    control_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    control_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pestañas")

    spaces_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Espacios para la Intervención de las Veedurías Ciudadanas en el Control Social de la Gestión del Ministerio de Minas y Energía")

    spaces_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    spaces_block_one = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Uno',
        verbose_name="Bloque Uno"
    )
    spaces_block_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Dos',
        verbose_name="Bloque Dos"
    )
    spaces_block_three = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque tres',
        verbose_name="Bloque tres"
    )
    spaces_block_four = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque Cuatro',
        verbose_name="Bloque Cuatro"
    )

    minister_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="El Ministerio de Minas y Energía en su compromiso con la ciudadanía declara")

    minister_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Rendición de cuentas'),
        MultiFieldPanel([
            FieldPanel('request_title'),
            FieldPanel('request_intro'),
            StreamFieldPanel('request_list'),
        ], heading="Peticiones, Quejas, Reclamos y Denuncias - PQRD", classname="collapsible",
            help_text='Peticiones, Quejas, Reclamos y Denuncias - PQRD'),
        MultiFieldPanel([
            FieldPanel('others_title'),
            StreamFieldPanel('others_list'),
        ], heading="Otros mecanismos constitucionales para la protección de los derechos ciudadanos", classname="collapsible",
            help_text='Otros mecanismos constitucionales para la protección de los derechos ciudadanos'),
        MultiFieldPanel([
            FieldPanel('mechanisms_title'),
            StreamFieldPanel('mechanisms_list'),
        ], heading="Mecanismos de participación", classname="collapsible",
            help_text='Mecanismos de participación'),
        MultiFieldPanel([
            FieldPanel('control_title'),
            FieldPanel('control_intro'),
            StreamFieldPanel('control_list'),
        ], heading="Mecanismos de Control Ciudadano para la Vigilancia de la Gestión Pública", classname="collapsible",
            help_text='Mecanismos de Control Ciudadano para la Vigilancia de la Gestión Pública'),
        MultiFieldPanel([
            FieldPanel('spaces_title'),
            FieldPanel('spaces_intro'),
            FieldPanel('spaces_block_one'),
            FieldPanel('spaces_block_two'),
            FieldPanel('spaces_block_three'),
            FieldPanel('spaces_block_four'),
        ], heading="Espacios para la Intervención de las Veedurías Ciudadanas en el Control Social de la Gestión del Ministerio de Minas y Energía", classname="collapsible",
            help_text='Espacios para la Intervención de las Veedurías Ciudadanas en el Control Social de la Gestión del Ministerio de Minas y Energía'),
        MultiFieldPanel([
            FieldPanel('minister_title'),
            FieldPanel('minister_intro'),
        ], heading="El Ministerio de Minas y Energía en su compromiso con la ciudadanía declara", classname="collapsible",
            help_text='El Ministerio de Minas y Energía en su compromiso con la ciudadanía declara'),

    ]


class InformeMecanismosParticipacionPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Informe de mecanismos de participación")

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
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Histórico Informe de mecanismos de participación")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducción", classname="collapsible",
            help_text='Introducción Rendición de cuentas'),
        MultiFieldPanel([
            StreamFieldPanel('historical_list'),
        ], heading="Histórico Informe de mecanismos de participación", classname="collapsible",
            help_text='Histórico Informe de mecanismos de participación'),


    ]


class PqrsPage(Page):
    subpage_types = []

    element_list = StreamField(
        [('Lista', HeaderMenuBlock())], blank=True, verbose_name="Eventos y Espacios Ciudadanos")

    second_links_title = models.CharField(
        "Título de la sección",
        max_length=254,
        null=False,
        blank=False,
        default="Registre y consulte su PQRS")

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('element_list'),
        ], heading="Eventos y Espacios Ciudadanos", classname="collapsible",
            help_text='Eventos y Espacios Ciudadanos'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Registre y consulte su PQRS", classname="collapsible",
            help_text='Registre y consulte su PQRS'),


    ]
