from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page


from .blocks import LinkListStructBlock, FeaturedLinkStructBlock, SecondLinkStructBlock
from ..common.blocks import ElementsListStructBlock, DeclarationStructBlock


class transparenciaPage(Page):

    subpage_types = ['declaracionRentaPage', ]
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Transparencia")
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

    featured_link = StreamField(
        [('Enlace', FeaturedLinkStructBlock())], blank=True, verbose_name="Enlace destacado", min_num=0, max_num=1)

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la sección")

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
            StreamFieldPanel('featured_link'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('link_list'),
        ], heading="Enlaces de la sección", classname="collapsible",
            help_text='Listado de enlaces de la sección'),
    ]


class declaracionRentaPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Publicación de la declaración de renta y complementarios de funcionarios públicos")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducción de la sección',
        verbose_name="Introducción"
    )
    documents_list = StreamField(
        [('Documentos', DeclarationStructBlock())], blank=True, verbose_name="Documentos de la sección")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
        ], heading="Introducción", classname="collapsible",
            help_text='Introducción de la sección'),
        MultiFieldPanel([
            StreamFieldPanel('documents_list'),
        ], heading="Documentos de la sección", classname="collapsible",
            help_text='Listado de enlaces de la sección'),
    ]
