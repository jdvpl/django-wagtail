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

from .blocks import LinkListStructBlock, FeaturedLinkStructBlock, ImageTextStructBlock, SliderStructBlock, TabTableStructBlock
from ..sala_prensa.blocks import BaseStreamBlock
from ..common.blocks import ElementsListStructBlock, TabsListStructBlock, BriefcaseStructBlock, SecondLinkStructBlock, CardsStructBlock, SimpleDocumentCardSliderStructBlock, SimpleBriefcaseStructBlock, SubitemsBriefcaseStructBlock, SimpleBlockIconStructBlock, AccodionRichTextStructBlock, AccordeonRichTextStructBlock


class CierreBrechasPage(Page):

    subpage_types = ['AccesoEnergiaPage', 'EnergiaIndexPage',
                     'ProyectosHidrocarburosIndexPage', 'ProyectosMineriaIndexPage']

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Cierre de brechas")
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

    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        verbose_name="Documento",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    cards_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    cards = StreamField(
        [('Brechas', CardsStructBlock())], blank=True, verbose_name="¿En qué consiste el Cierre de brechas?")

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
            FieldPanel('text_link'),
            ImageChooserPanel('image_link'),
            DocumentChooserPanel('document_file'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la sección'),
        MultiFieldPanel([
            FieldPanel('cards_title'),
            StreamFieldPanel('cards'),
        ], heading="¿En qué consiste el Cierre de brechas?", classname="collapsible",
            help_text='¿En qué consiste el Cierre de brechas?'),
    ]


class AccesoEnergiaPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Acceso a energía")
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

    second_title = models.CharField(
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
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    third_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )
    third_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    third_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
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

    cards_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Título que será presentado al publico',
        verbose_name='Título de la sección'
    )

    cards_list = StreamField(
        [('Documentos', SimpleDocumentCardSliderStructBlock())], blank=True, verbose_name="Documentos")

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
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Inversión realizada en proyectos por Departamento", classname="collapsible",
            help_text='Inversión realizada en proyectos por Departamento'),

        MultiFieldPanel([
            FieldPanel('third_title'),
            FieldPanel('third_intro'),
            FieldPanel('third_link_pbi'),
            ImageChooserPanel('third_image'),
            FieldPanel('third_alt_text'),
        ], heading="Información de interés", classname="collapsible",
            help_text='Información de interés'),

        MultiFieldPanel([
            FieldPanel('cards_list_title'),
            StreamFieldPanel('cards_list'),
        ], heading="Documentos Meta 100 K", classname="collapsible",
            help_text='Documentos Meta 100 K'),
    ]


""" Proyectos de Mineria """


class ProyectosMineriaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ProyectosMineriaPage', related_name='proyectosmineria_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_proyectosmineria_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ProyectosMineriaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ProyectosMineriaPage', related_name='proyectosmineria_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_proyectosmineria_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ProyectosMineriaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProyectosMineriaPage', related_name='tagged_items', on_delete=models.CASCADE)


class ProyectosMineriaSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the ProyectosMineria URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ProyectosMineriaIconSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the ProyectosMineria URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ProyectosMineriaPage(Page):

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    manager = models.CharField(
        blank=True, max_length=255, verbose_name="Administrador")
    start_date = models.DateField(
        "Fecha de inicio", blank=True, null=True
    )
    department = models.TextField(
        help_text='Departamento',
        blank=True,
        verbose_name="Departamento",)
    municipality = models.TextField(
        help_text='Municipio',
        blank=True,
        verbose_name="Municipio",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)
    latitude = models.FloatField(
        help_text='Latitud, valores entre -90 y 90',
        blank=True,
        verbose_name="Latitud",
        default=0)
    longitude = models.FloatField(
        help_text='Longitud, valores entre -180 y 180',
        blank=True,
        verbose_name="Longitud",
        default=0)
    energy_type = models.TextField(
        help_text='Tipo de energía',
        blank=True,
        verbose_name="Tipo de energía",)
    icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del tipo de energía',
        verbose_name="Icono del tipo de energía"
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Anexos",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tags = ClusterTaggableManager(
        through=ProyectosMineriaPageTag, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('manager'),
        FieldPanel('start_date'),
        FieldPanel('department'),
        FieldPanel('municipality'),
        FieldPanel('latitude'),
        FieldPanel('longitude'),
        FieldPanel('users'),
        FieldPanel('energy_type'),
        SvgChooserPanel('icon'),
        DocumentChooserPanel('document_file'),
        InlinePanel(
            'proyectosmineria_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('energy_type'),
        index.SearchField('intro'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.proyectosmineria_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.proyectosmineria_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.proyectosmineria_sector_relationship.all()
        ]

    @property
    def sectors_list_str(self):
        sectors = [
            str(child.sector) for child in self.proyectosmineria_sector_relationship.all()
        ]
        return ', '.join(sectors)

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

    parent_page_types = ['ProyectosMineriaIndexPage']

    subpage_types = []

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('manager'),
        APIField('start_date'),
        APIField('department'),
        APIField('municipality'),
        APIField('latitude'),
        APIField('longitude'),
        APIField('users'),
        APIField('energy_type'),
        APIField('icon', ProyectosMineriaIconSerializedField()),
        APIField('tags'),
        APIField('document_file', ProyectosMineriaSerializedField()),
    ]


class ProyectosMineriaIndexPage(RoutablePageMixin, Page):

    subpage_types = ['ProyectosMineriaPage']

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    projects = models.TextField(
        help_text='Proyectos',
        blank=True,
        verbose_name="Proyectos",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('users'),
        FieldPanel('projects'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('users'),
        APIField('projects'),
    ]

    def children(self):
        return ProyectosMineriaPage.objects.descendant_of(self).live().order_by('-start_date')

    def get_years(self, posts):
        for post in posts:
            years = post.proyectosmineria_year_relationship.filter(
                page_id=post.id)
            post['year'] = years[0].year
        return posts

    def get_context(self, request):
        context = super(ProyectosMineriaIndexPage,
                        self).get_context(request)
        context['posts'] = ProyectosMineriaPage.objects.descendant_of(
            self).live().order_by('-start_date')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = ProyectosMineriaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Proyectos de Mineria """

""" Proyectos de Hidrocarburos """


class ProyectosHidrocarburosAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ProyectosHidrocarburosPage', related_name='proyectoshidrocarburos_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_proyectoshidrocarburos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class ProyectosHidrocarburosSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'ProyectosHidrocarburosPage', related_name='proyectoshidrocarburos_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_proyectoshidrocarburos_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class ProyectosHidrocarburosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProyectosHidrocarburosPage', related_name='tagged_items', on_delete=models.CASCADE)


class ProyectosHidrocarburosSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the ProyectosHidrocarburos URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ProyectosHidrocarburosIconSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the ProyectosHidrocarburos URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class ProyectosHidrocarburosPage(Page):

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    manager = models.CharField(
        blank=True, max_length=255, verbose_name="Administrador")
    start_date = models.DateField(
        "Fecha de inicio", blank=True, null=True
    )
    department = models.TextField(
        help_text='Departamento',
        blank=True,
        verbose_name="Departamento",)
    municipality = models.TextField(
        help_text='Municipio',
        blank=True,
        verbose_name="Municipio",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)
    latitude = models.FloatField(
        help_text='Latitud, valores entre -90 y 90',
        blank=True,
        verbose_name="Latitud",
        default=0)
    longitude = models.FloatField(
        help_text='Longitud, valores entre -180 y 180',
        blank=True,
        verbose_name="Longitud",
        default=0)
    energy_type = models.TextField(
        help_text='Tipo de energía',
        blank=True,
        verbose_name="Tipo de energía",)
    icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del tipo de energía',
        verbose_name="Icono del tipo de energía"
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Anexos",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tags = ClusterTaggableManager(
        through=ProyectosHidrocarburosPageTag, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('manager'),
        FieldPanel('start_date'),
        FieldPanel('department'),
        FieldPanel('municipality'),
        FieldPanel('latitude'),
        FieldPanel('longitude'),
        FieldPanel('users'),
        FieldPanel('energy_type'),
        SvgChooserPanel('icon'),
        DocumentChooserPanel('document_file'),
        InlinePanel(
            'proyectoshidrocarburos_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('energy_type'),
        index.SearchField('intro'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.proyectoshidrocarburos_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.proyectoshidrocarburos_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.proyectoshidrocarburos_sector_relationship.all()
        ]

    @property
    def sectors_list_str(self):
        sectors = [
            str(child.sector) for child in self.proyectoshidrocarburos_sector_relationship.all()
        ]
        return ', '.join(sectors)

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

    parent_page_types = ['ProyectosHidrocarburosIndexPage']

    subpage_types = []

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('manager'),
        APIField('start_date'),
        APIField('department'),
        APIField('municipality'),
        APIField('latitude'),
        APIField('longitude'),
        APIField('users'),
        APIField('energy_type'),
        APIField('icon', ProyectosHidrocarburosIconSerializedField()),
        APIField('tags'),
        APIField('document_file', ProyectosHidrocarburosSerializedField()),
    ]


class ProyectosHidrocarburosIndexPage(RoutablePageMixin, Page):

    subpage_types = ['ProyectosHidrocarburosPage']

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    projects = models.TextField(
        help_text='Proyectos',
        blank=True,
        verbose_name="Proyectos",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('users'),
        FieldPanel('projects'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('users'),
        APIField('projects'),
    ]

    def children(self):
        return ProyectosHidrocarburosPage.objects.descendant_of(self).live().order_by('-start_date')

    def get_years(self, posts):
        for post in posts:
            years = post.proyectoshidrocarburos_year_relationship.filter(
                page_id=post.id)
            post['year'] = years[0].year
        return posts

    def get_context(self, request):
        context = super(ProyectosHidrocarburosIndexPage,
                        self).get_context(request)
        context['posts'] = ProyectosHidrocarburosPage.objects.descendant_of(
            self).live().order_by('-start_date')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = ProyectosHidrocarburosPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Proyectos de Hidrocarburos """

""" Proyectos de Energia """


class EnergiaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'EnergiaPage', related_name='energia_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_energia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class EnergiaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'EnergiaPage', related_name='energia_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_energia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class EnergiaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'EnergiaPage', related_name='tagged_items', on_delete=models.CASCADE)


class EnergiaSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Energia URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class EnergiaIconSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Energia URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class EnergiaPage(Page):

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    manager = models.CharField(
        blank=True, max_length=255, verbose_name="Administrador")
    start_date = models.DateField(
        "Fecha de inicio", blank=True, null=True
    )
    department = models.TextField(
        help_text='Departamento',
        blank=True,
        verbose_name="Departamento",)
    municipality = models.TextField(
        help_text='Municipio',
        blank=True,
        verbose_name="Municipio",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)
    latitude = models.FloatField(
        help_text='Latitud, valores entre -90 y 90',
        blank=True,
        verbose_name="Latitud",
        default=0)
    longitude = models.FloatField(
        help_text='Longitud, valores entre -180 y 180',
        blank=True,
        verbose_name="Longitud",
        default=0)
    energy_type = models.TextField(
        help_text='Tipo de energía',
        blank=True,
        verbose_name="Tipo de energía",)
    icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono del tipo de energía',
        verbose_name="Icono del tipo de energía"
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Anexos",
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tags = ClusterTaggableManager(through=EnergiaPageTag, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('manager'),
        FieldPanel('start_date'),
        FieldPanel('department'),
        FieldPanel('municipality'),
        FieldPanel('latitude'),
        FieldPanel('longitude'),
        FieldPanel('users'),
        FieldPanel('energy_type'),
        SvgChooserPanel('icon'),
        DocumentChooserPanel('document_file'),
        InlinePanel(
            'energia_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('energy_type'),
        index.SearchField('intro'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.energia_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.energia_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.energia_sector_relationship.all()
        ]

    @property
    def sectors_list_str(self):
        sectors = [
            str(child.sector) for child in self.energia_sector_relationship.all()
        ]
        return ', '.join(sectors)

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

    parent_page_types = ['EnergiaIndexPage']

    subpage_types = []

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('manager'),
        APIField('start_date'),
        APIField('department'),
        APIField('municipality'),
        APIField('latitude'),
        APIField('longitude'),
        APIField('users'),
        APIField('energy_type'),
        APIField('icon', EnergiaIconSerializedField()),
        APIField('tags'),
        APIField('document_file', EnergiaSerializedField()),
    ]


class EnergiaIndexPage(RoutablePageMixin, Page):

    subpage_types = ['EnergiaPage']

    intro = models.TextField(
        null=True,
        blank=True,
        help_text='Introducción',
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
    alt_text = models.TextField(verbose_name="Texto alternativo de la imagen", blank=True,
                                help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    projects = models.TextField(
        help_text='Proyectos',
        blank=True,
        verbose_name="Proyectos",)
    users = models.TextField(
        help_text='Usuarios',
        blank=True,
        verbose_name="Usuarios",)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link_video'),
        ImageChooserPanel('image'),
        FieldPanel('alt_text'),
        FieldPanel('users'),
        FieldPanel('projects'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('link_video'),
        APIField('image_data', serializer=ImageRenditionField(
            'original', source='image')),
        APIField('alt_text'),
        APIField('users'),
        APIField('projects'),
    ]

    def children(self):
        return EnergiaPage.objects.descendant_of(self).live().order_by('-start_date')

    def get_years(self, posts):
        for post in posts:
            years = post.energia_year_relationship.filter(
                page_id=post.id)
            post['year'] = years[0].year
        return posts

    def get_context(self, request):
        context = super(EnergiaIndexPage, self).get_context(request)
        context['posts'] = EnergiaPage.objects.descendant_of(
            self).live().order_by('-start_date')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = EnergiaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Proyectos de Energia """
