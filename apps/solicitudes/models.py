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

# from .blocks import LinkListStructBlock, FeaturedLinkStructBlock, ImageTextStructBlock, SliderStructBlock, TabTableStructBlock, RETIETableStructBlock, HeaderMenuBlockAcordeon
from ..common.blocks import ElementsListStructBlock, TabsListStructBlock, BriefcaseStructBlock, SecondLinkStructBlock, CardsStructBlock, SimpleDocumentCardSliderStructBlock, SimpleBriefcaseStructBlock, SubitemsBriefcaseStructBlock, SimpleBlockIconStructBlock, AccodionRichTextStructBlock, AccordeonRichTextStructBlock, LinkDocumentCardSliderStructBlock,HeaderStructBlock,ElementsListStructMenuBlock

class SolicitudesEspecialesPage(Page):
    subpage_types = []
    intro_title = models.CharField(
        "Título de la sección", max_length=254, null=False, blank=False, default="Solicitudes especiales")
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
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la sección'),

    ]