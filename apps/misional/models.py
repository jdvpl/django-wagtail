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
from .cierre_brechas_subpages import CierreBrechasPage
from .blocksnoticias import BaseStreamBlock, GalleryStreamBlock, SocialNetworksBlock
from .gestion_social_a_subpages import GestionSocialAmbientalPage

class misionalPage(Page):

    subpage_types = [
        'FuentesNoConvencionalesEnergiaRenovablePage', 'EficienciaEnergeticaPage', 'CierreBrechasPage', 'HidrocarburosPage', 'TransformacionMineraPage', 'UnidadResultadosPage', 'EnergiaElectricaPage', 'GestionSocialAmbientalPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Misional")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tama??o recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripci??n del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripci??n"
    )

    featured_link = StreamField(
        [('Enlace', FeaturedLinkStructBlock())], blank=True, verbose_name="Enlace destacado", min_num=0, max_num=1)

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('text_link'),
            ImageChooserPanel('image_link'),
            StreamFieldPanel('featured_link'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),
    ]


class FuentesNoConvencionalesEnergiaRenovablePage(Page):
    subpage_types = []
    """ First section """
    intro_title = models.CharField(
        "T??tulo de la secci??n",
        max_length=254,
        null=False,
        blank=False,
        default="Fuentes No Convencionales de Energ??a Renovable - FNCER")

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    energy_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    energy_list = StreamField(
        [('Energias', BriefcaseStructBlock())], blank=True, verbose_name="Energ??as renovables no convencionales")

    """ First section """

    """ Second section """
    second_intro_title = models.CharField(
        "T??tulo de la secci??n",
        max_length=254,
        null=False,
        blank=False,
        default="FNCER en Colombia")

    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    sale_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    sale_list = StreamField(
        [('Subastas', TabsListStructBlock())], blank=True, verbose_name="Subastas")

    """ Second section """

    """ Third section """
    third_intro_title = models.CharField(
        "T??tulo de la secci??n",
        max_length=254,
        null=False,
        blank=False,
        default="Recursos Energ??ticos Distribuidos")

    third_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    third_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    third_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    resource_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    resource_list = StreamField(
        [('Recursos', BriefcaseStructBlock())], blank=True, verbose_name="Recursos Energ??ticos Distribuidos")
    """ Third section """

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Indroducci??n Fuentes No Convencionales de Energ??a Renovable", classname="collapsible",
            help_text='Fuentes No Convencionales de Energ??a Renovable'),

        MultiFieldPanel([
            FieldPanel('energy_list_title'),
            StreamFieldPanel('energy_list'),
        ], heading=" Energ??as renovables no convencionales", classname="collapsible",
            help_text='Energ??as renovables no convencionales'),

        MultiFieldPanel([
            FieldPanel('second_intro_title'),
            FieldPanel('second_intro'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Indroducci??n FNCER en Colombia", classname="collapsible",
            help_text='FNCER en Colombia'),

        MultiFieldPanel([
            FieldPanel('sale_list_title'),
            StreamFieldPanel('sale_list'),
        ], heading="Subastas", classname="collapsible",
            help_text='Subastas'),

        MultiFieldPanel([
            FieldPanel('third_intro_title'),
            FieldPanel('third_intro'),
            ImageChooserPanel('third_image'),
            FieldPanel('third_alt_text'),
        ], heading="Indroducci??n Recursos Energ??ticos Distribuidos", classname="collapsible",
            help_text='Recursos Energ??ticos Distribuidos'),

        MultiFieldPanel([
            FieldPanel('resource_list_title'),
            StreamFieldPanel('resource_list'),
        ], heading="Recursos Energ??ticos Distribuidos", classname="collapsible",
            help_text='Recursos Energ??ticos Distribuidos'),

    ]


class EficienciaEnergeticaPage(Page):
    subpage_types = ['BuenasPracticasIndexPage',
                     'EstudioMetasIndexPage', 'MedidoresInteligentesPage', 'MovilidadElectricaPage', 'CiudadesEnergeticasPage', 'EtiquetadoEficienciaEnergeticaPage']
    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Eficiencia Energ??tica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
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
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),

    ]


""" Estudio de Metas Obligatorias de Eficiencia Energ??tica """


class EstudioAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'EstudioPage', related_name='estudio_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_estudio_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class EstudioSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'EstudioPage', related_name='estudio_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_estudio_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class EstudioPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'EstudioPage', related_name='tagged_items', on_delete=models.CASCADE)


class EstudioSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Estudio URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class EstudioPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la presentaci??n',
        blank=False,
        verbose_name="Introducci??n",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen de la presentaci??n",
        help_text='Imagen de presentaci??n para la presentaci??n'
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
    tags = ClusterTaggableManager(through=EstudioPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicaci??n", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        DocumentChooserPanel('document_file'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'estudio_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'estudio_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.estudio_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.estudio_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.estudio_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.estudio_autor_relationship.all()
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

    parent_page_types = ['EstudioMetasIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', EstudioSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class EstudioMetasIndexPage(RoutablePageMixin, Page):

    subpage_types = ['EstudioPage']

    def children(self):
        return EstudioPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(EstudioMetasIndexPage, self).get_context(request)
        context['posts'] = EstudioPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = EstudioPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Estudio de Metas Obligatorias de Eficiencia Energ??tica """

""" Buenas Pr??cticas para la Gesti??n Eficiente de la Energ??a """


class PracticaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'PracticaPage', related_name='practica_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_practica_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class PracticaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'PracticaPage', related_name='practica_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_practica_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class PracticaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'PracticaPage', related_name='tagged_items', on_delete=models.CASCADE)


class PracticaSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the Practica URL and title """
        return {
            "url": value.file.url,
            "title": value.title,
        }


class PracticaPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la presentaci??n',
        blank=False,
        verbose_name="Introducci??n",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagen de la presentaci??n",
        help_text='Imagen de presentaci??n para la presentaci??n'
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
    tags = ClusterTaggableManager(through=PracticaPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicaci??n", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        DocumentChooserPanel('document_file'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'practica_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'practica_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.practica_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.practica_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.practica_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.practica_autor_relationship.all()
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

    parent_page_types = ['BuenasPracticasIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('document_file', PracticaSerializedField()),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),
    ]


class BuenasPracticasIndexPage(RoutablePageMixin, Page):

    subpage_types = ['PracticaPage']

    def children(self):
        return PracticaPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(BuenasPracticasIndexPage, self).get_context(request)
        context['posts'] = PracticaPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = PracticaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


""" Buenas Pr??cticas para la Gesti??n Eficiente de la Energ??a """


class MedidoresInteligentesPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Medidores inteligentes")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),

    ]


class MovilidadElectricaPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Movilidad El??ctrica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),

        MultiFieldPanel([
            StreamFieldPanel('link_list'),
        ], heading="Enlaces de la secci??n", classname="collapsible",
            help_text='Listado de enlaces de la secci??n'),

    ]


class CiudadesEnergeticasPage(Page):
    subpage_types = []

    city_list = StreamField(
        [('Ciudades', ImageTextStructBlock())], blank=True, verbose_name="Ciudades Energ??ticas")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            StreamFieldPanel('city_list'),
        ], heading="Ciudades Energ??ticas", classname="collapsible",
            help_text='Listado de Ciudades Energ??ticas'),

    ]


class EtiquetadoEficienciaEnergeticaPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Etiquetado de eficiencia energ??tica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    title_page = models.CharField(
        "T??tulo del boton", max_length=254, null=False, blank=False, default="etiquetaenergetica.gov.co")

    link_page = models.URLField(
        verbose_name="Link etiquetaenergetica.gov.coI", blank=True, help_text='Link etiquetaenergetica.gov.co',)

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
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
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),

        MultiFieldPanel([
            FieldPanel('second_intro'),
            FieldPanel('title_page'),
            FieldPanel('link_page'),
        ], heading="Segundo bloque", classname="collapsible",
            help_text='Segundo bloque'),

        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Enlaces de la secci??n", classname="collapsible",
            help_text='Listado de enlaces de la secci??n'),

    ]


class TransformacionMineraPage(Page):
    subpage_types = ['DiversificacionProduccionMineralesPage',
                     'LegalidadPage', 'FomentoBuenasPracticasMinerasPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Transformaci??n Minera")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="??Qu?? es el sector minero?")
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    title_pbi = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="??D??nde est??n los Minerales en el Pa??s?")
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)

    tab_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="??Cu??les son los minerales y para que sirven?")
    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    block_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Transformaci??n Minera")
    block_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    block_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Descripci??n',
        verbose_name="Descripci??n"
    )

    cards_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    cards = StreamField(
        [('Tarjetas', CardsStructBlock())], blank=True, verbose_name="??En qu?? consiste la Transformaci??n Minera?")

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Lineamientos y Pol??ticas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_video'),
        ], heading="??Qu?? es el sector minero?", classname="collapsible",
            help_text='??Qu?? es el sector minero?'),
        MultiFieldPanel([
            FieldPanel('title_pbi'),
            FieldPanel('link_pbi'),
        ], heading="??D??nde est??n los Minerales en el Pa??s?", classname="collapsible",
            help_text='??D??nde est??n los Minerales en el Pa??s?'),
        MultiFieldPanel([
            FieldPanel('tab_title'),
            StreamFieldPanel('tab_list'),
        ], heading="??Cu??les son los minerales y para que sirven?", classname="collapsible",
            help_text='??Cu??les son los minerales y para que sirven?'),
        MultiFieldPanel([
            FieldPanel('block_title'),
            FieldPanel('block_intro'),
            ImageChooserPanel('block_image'),
            FieldPanel('block_alt_text'),
        ], heading="Transformaci??n Minera", classname="collapsible",
            help_text='Transformaci??n Minera'),
        MultiFieldPanel([
            FieldPanel('cards_title'),
            StreamFieldPanel('cards'),
        ], heading="??En qu?? consiste la Transformaci??n Minera?", classname="collapsible",
            help_text='??En qu?? consiste la Transformaci??n Minera?'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            StreamFieldPanel('menu_list'),
        ], heading="Lineamientos y Pol??ticas", classname="collapsible",
            help_text='Lineamientos y Pol??ticas'),
    ]


class DiversificacionProduccionMineralesPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Diversificaci??n de la producci??n de minerales")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    third_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    third_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    third_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    third_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    third_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    cards_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    cards_list = StreamField(
        [('Agenda', SimpleDocumentCardSliderStructBlock())], blank=True, verbose_name="Agendas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),

        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),

            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Fortalecimiento a la Explotaci??n", classname="collapsible",
            help_text='Fortalecimiento a la Explotaci??n'),

        MultiFieldPanel([
            FieldPanel('third_title'),
            FieldPanel('third_intro'),
            FieldPanel('third_link_pbi'),
            ImageChooserPanel('third_image'),
            FieldPanel('third_alt_text'),
        ], heading="Gesti??n y Acompa??amiento de Proyectos", classname="collapsible",
            help_text='Gesti??n y Acompa??amiento de Proyectos'),

        MultiFieldPanel([
            FieldPanel('cards_list_title'),
            StreamFieldPanel('cards_list'),
        ], heading="Agendas por subsector", classname="collapsible",
            help_text='Agendas por subsector'),
    ]


class LegalidadPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Legalidad")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Casos de ??xito")

    third_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    third_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Apoyo al control a la Explotaci??n Il??cita de Minerales")

    fourth_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    fourth_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fourth_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    fourth_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Miner??a de subsistencia")
    fourth_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Fortalecimiento a la Explotaci??n", classname="collapsible",
            help_text='Fortalecimiento a la Explotaci??n'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            StreamFieldPanel('menu_list'),
        ], heading="Casos de ??xito", classname="collapsible",
            help_text='Casos de ??xito'),
        MultiFieldPanel([
            FieldPanel('third_title'),
            StreamFieldPanel('third_links'),
        ], heading="Apoyo al control a la Explotaci??n Il??cita de Minerales", classname="collapsible",
            help_text='Apoyo al control a la Explotaci??n Il??cita de Minerales'),
        MultiFieldPanel([
            FieldPanel('fourth_title'),
            ImageChooserPanel('fourth_image'),
            FieldPanel('fourth_alt_text'),
            StreamFieldPanel('fourth_links'),
            FieldPanel('fourth_intro'),
        ], heading="Miner??a de subsistencia", classname="collapsible",
            help_text='Miner??a de subsistencia'),


    ]


class FomentoBuenasPracticasMinerasPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Fomento y buenas pr??cticas mineras")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Casos de ??xito")

    fourth_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    fourth_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fourth_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    fourth_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Miner??a de subsistencia")

    block_list = StreamField(
        [('Bloque', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Bloques de texto")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Modelo de fomento", classname="collapsible",
            help_text='Modelo de fomento'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            StreamFieldPanel('menu_list'),
        ], heading="Buenas pr??cticas para la actividad minera", classname="collapsible",
            help_text='Buenas pr??cticas para la actividad minera'),
        MultiFieldPanel([
            FieldPanel('fourth_title'),
            ImageChooserPanel('fourth_image'),
            FieldPanel('fourth_alt_text'),
            StreamFieldPanel('fourth_links'),
        ], heading="Centro de Aprendizaje Minero", classname="collapsible",
            help_text='Centro de Aprendizaje Minero'),
        MultiFieldPanel([
            StreamFieldPanel('block_list'),
        ], heading="Bloques de texto", classname="collapsible",
            help_text='Bloques de texto'),
    ]


class HidrocarburosPage(Page):

    subpage_types = ['FuncionamientoSectorPage',
                     'ReglamentosTecnicosPage', 'TramitesServiciosPage', 'FuncionamientoSectorPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Hidrocarburos")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    title_pbi = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Informaci??n a publicar PPIS- GAS- Precios")

    intro_pbi = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)

    second_links_two = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    title_pbi_two = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Datos del Sector")

    intro_pbi_two = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi_two = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)

    link_pbi_three = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    link_pbi_four = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    link_pbi_five = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    link_pbi_six = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),
        MultiFieldPanel([
            FieldPanel('title_pbi'),
            FieldPanel('intro_pbi'),
            FieldPanel('link_pbi'),
        ], heading="Informaci??n a publicar PPIS- GAS- Precios", classname="collapsible",
            help_text='Informaci??n a publicar PPIS- GAS- Precios'),
        MultiFieldPanel([
            StreamFieldPanel('second_links_two'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios'),
        MultiFieldPanel([
            FieldPanel('title_pbi_two'),
            FieldPanel('intro_pbi_two'),
            FieldPanel('link_pbi_two'),
        ], heading="Datos del Sector", classname="collapsible",
            help_text='Datos del Sector'),
        MultiFieldPanel([
            FieldPanel('link_pbi_three'),
            FieldPanel('link_pbi_four'),
            FieldPanel('link_pbi_five'),
            FieldPanel('link_pbi_six'),
        ], heading="Datos del Sector Tableros", classname="collapsible",
            help_text='Datos del Sector Tableros'),

    ]


class ReglamentosTecnicosPage(Page):

    subpage_types = []

    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Casos de ??xito")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Reglamentos T??cnicos", classname="collapsible",
            help_text='Reglamentos T??cnicos'),

    ]


class TramitesServiciosPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Tr??mites y Servicios")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    items_list = StreamField(
        [('Lista', SubitemsBriefcaseStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
        ], heading="Tr??mites y Servicios", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel('items_list'),
        ], heading="Elementos", classname="collapsible",
            help_text="Elementos"),
    ]


class FuncionamientoSectorPage(Page):

    subpage_types = ['GasNaturalPage', 'GasLicuadoPetroleoPage',
                     'EstadisticasGasCombustiblePage', 'FondosEspecialesPage', 'DownstreamPage', 'MidstreamPage', 'UpstreamPage', 'AsesoriaJuridicaPage', 'GestionProyectosOptimizacionPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Funcionamiento del Sector")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    intro_title_second = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Importancia del Sector de Hidrocarburos")

    block_list = StreamField(
        [('Tabs', SimpleBlockIconStructBlock())], blank=True, verbose_name="Bloques")

    link_list_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Grupos Transversales de la Direcci??n")
    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('block_list'),
        ], heading="Bloque de texto", classname="collapsible",
            help_text='Bloque de texto'),
        MultiFieldPanel([
            FieldPanel('link_list_title'),
            StreamFieldPanel('link_list'),
        ], heading="Grupos Transversales de la Direcci??n", classname="collapsible",
            help_text='Grupos Transversales de la Direcci??n'),
    ]


class GasLicuadoPetroleoPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    history_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    history = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    chain_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    chain = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    chain_links = StreamField(
        [('Elementos', SecondLinkStructBlock())], blank=True, verbose_name="Cadena de valor")

    assigned_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    assigned_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Declaraci??n de Producci??n de Gas Licuado de Petr??leo")
    assigned_tabs_list_title_two = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    assigned_tabs_list_two = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Reglamentaci??n T??cnica")
    general_tabs_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Indroducci??n", classname="collapsible",
            help_text='Indroducci??n'),
        MultiFieldPanel([
            FieldPanel('history_title'),
            FieldPanel('history'),
        ], heading="Historia", classname="collapsible",
            help_text='Historia'),
        MultiFieldPanel([
            FieldPanel('chain_title'),
            FieldPanel('chain'),
            StreamFieldPanel('chain_links'),
        ], heading="Cadena de valor", classname="collapsible",
            help_text='Cadena de valor'),
        MultiFieldPanel([
            FieldPanel('assigned_tabs_list_title'),
            StreamFieldPanel('assigned_tabs_list'),
            FieldPanel('assigned_tabs_list_title_two'),
            StreamFieldPanel('assigned_tabs_list_two'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Declaraciones", classname="collapsible",
            help_text='Declaraciones'),

    ]


class GasNaturalPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    history_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    history = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    chain_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    chain = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    chain_links = StreamField(
        [('Elementos', SecondLinkStructBlock())], blank=True, verbose_name="Cadena de valor")

    assigned_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    assigned_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")
    general_tabs_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    gas_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    gas = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Indroducci??n", classname="collapsible",
            help_text='Indroducci??n'),
        MultiFieldPanel([
            FieldPanel('history_title'),
            FieldPanel('history'),
        ], heading="Historia", classname="collapsible",
            help_text='Historia'),
        MultiFieldPanel([
            FieldPanel('chain_title'),
            FieldPanel('chain'),
            StreamFieldPanel('chain_links'),
        ], heading="Cadena de valor", classname="collapsible",
            help_text='Cadena de valor'),
        MultiFieldPanel([
            FieldPanel('assigned_tabs_list_title'),
            StreamFieldPanel('assigned_tabs_list'),
            StreamFieldPanel('general_tabs_list'),
        ], heading="Declaraci??n de Producci??n de Gas Natural", classname="collapsible",
            help_text='Declaraci??n de Producci??n de Gas Natural'),
        MultiFieldPanel([
            FieldPanel('gas_title'),
            FieldPanel('gas'),
        ], heading="Gas Comprimido Vehicular", classname="collapsible",
            help_text='Gas Comprimido Vehicular'),
    ]


class EstadisticasGasCombustiblePage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Cobertura Nacional Gas Combustible por Red")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    title_list_one = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Cobertura Nacional del Servicio de Gas Natural")
    list_one = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    title_list_two = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Cobertura Nacional Gas Licuado de Petr??leo - GLP")
    list_two = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    link_list_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Formatos de Cargue de Cobertura")
    intro_list = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")

    title_list_three = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Estad??sticas de Conversiones")
    list_three = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    resolution_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Publicaci??n Resoluci??n 18041 de 2007")
    resolution_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    stats_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Estad??sticas Estaciones de Servicio de Gas Natural Vehicular - GNV")
    stats_intro_block_one = RichTextField(
        null=True,
        blank=True,
        help_text='Block de texto',
        verbose_name="Block de texto"
    )
    stats_intro_block_two = RichTextField(
        null=True,
        blank=True,
        help_text='Block de texto',
        verbose_name="Block de texto"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('title_list_one'),
            StreamFieldPanel('list_one'),
        ], heading="Cobertura Nacional del Servicio de Gas Natural", classname="collapsible",
            help_text='Cobertura Nacional del Servicio de Gas Natural'),
        MultiFieldPanel([
            FieldPanel('title_list_two'),
            StreamFieldPanel('list_two'),
        ], heading="Cobertura Nacional Gas Licuado de Petr??leo - GLP", classname="collapsible",
            help_text='Cobertura Nacional Gas Licuado de Petr??leo - GLP'),
        MultiFieldPanel([
            FieldPanel('link_list_title'),
            FieldPanel('intro_list'),
            StreamFieldPanel('link_list'),
        ], heading="Formatos de Cargue de Cobertura", classname="collapsible",
            help_text='Formatos de Cargue de Cobertura'),
        MultiFieldPanel([
            FieldPanel('title_list_three'),
            StreamFieldPanel('list_three'),
        ], heading="Estad??sticas de Conversiones", classname="collapsible",
            help_text='Estad??sticas de Conversiones'),
        MultiFieldPanel([
            FieldPanel('resolution_title'),
            StreamFieldPanel('resolution_intro'),
        ], heading="Publicaci??n Resoluci??n 18041 de 2007", classname="collapsible",
            help_text='Publicaci??n Resoluci??n 18041 de 2007'),
        MultiFieldPanel([
            FieldPanel('stats_title'),
            FieldPanel('stats_intro_block_one'),
            FieldPanel('stats_intro_block_two'),
        ], heading="Estad??sticas Estaciones de Servicio de Gas Natural Vehicular - GNV", classname="collapsible",
            help_text='Estad??sticas Estaciones de Servicio de Gas Natural Vehicular - GNV'),
    ]


class FondosEspecialesPage(Page):
    subpage_types = []

    history_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    history = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    assigned_tabs_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    assigned_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('history_title'),
            FieldPanel('history'),
        ], heading="Fondos Especial Cuota de Fomento Gas Natural", classname="collapsible",
            help_text='Fondos Especial Cuota de Fomento Gas Natural'),
        MultiFieldPanel([
            FieldPanel('assigned_tabs_list_title'),
            FieldPanel('intro'),
            StreamFieldPanel('assigned_tabs_list'),
        ], heading="Fondo de Solidaridad para Subsidios y Redistribuci??n de Ingresos - FSSRI", classname="collapsible",
            help_text='Fondo de Solidaridad para Subsidios y Redistribuci??n de Ingresos - FSSRI'),

    ]


class DownstreamPage(Page):
    subpage_types = []

    how_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    how = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    systems_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    systems = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    chain_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    chain_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    menu_list = StreamField(
        [('Menu', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Items")

    sicom_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Sistema de informaci??n de combustibles - SICOM")
    sicom_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    sicom_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sicom_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    bio_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Biocombustibles")
    bio_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    bio_tabs_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    price_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Precios Combustibles")
    price_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    price_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    price_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    history_price_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Precios Combustibles")
    history_price_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    history_price_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    history_price_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                              help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    prices_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    prices_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    zone_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Zonas de frontera")
    zone_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    zone_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    zone_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                     help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    vol_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Asignaci??n de vol??menes m??ximos")
    vol_tabs_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    plan_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Plan de abastecimiento")
    plan_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    plan_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")

    program_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Programa reconversi??n socio-laboral")
    program_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('how_title'),
            FieldPanel('how'),
        ], heading="??C??mo lo hacemos?", classname="collapsible",
            help_text='??C??mo lo hacemos?'),
        MultiFieldPanel([
            FieldPanel('systems_title'),
            FieldPanel('systems'),
            StreamFieldPanel('link_list'),
        ], heading="Sistemas de Informaci??n", classname="collapsible",
            help_text='Sistemas de Informaci??n'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Combustibles l??quidos y Biocombustibles", classname="collapsible",
            help_text='Combustibles l??quidos y Biocombustibles'),
        MultiFieldPanel([
            FieldPanel('chain_title'),
            FieldPanel('chain_intro'),
        ], heading="Agentes de la Cadena", classname="collapsible",
            help_text='Agentes de la Cadena'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Combustibles L??quidos y Biocombustibles", classname="collapsible",
            help_text='Combustibles L??quidos y Biocombustibles'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            FieldPanel('menu_list_intro'),
            StreamFieldPanel('menu_list'),
        ], heading="Biocombustibles", classname="collapsible",
            help_text='Biocombustibles'),
        MultiFieldPanel([
            FieldPanel('sicom_title'),
            FieldPanel('sicom_intro'),
            ImageChooserPanel('sicom_image'),
            FieldPanel('sicom_alt_text'),
        ], heading="Combustibles l??quidos y Biocombustibles", classname="collapsible",
            help_text='Combustibles l??quidos y Biocombustibles'),
        MultiFieldPanel([
            FieldPanel('bio_title'),
            FieldPanel('bio_intro'),
            StreamFieldPanel('bio_tabs_list'),
        ], heading="Biocombustibles", classname="collapsible",
            help_text='Biocombustibles'),
        MultiFieldPanel([
            FieldPanel('price_title'),
            FieldPanel('price_intro'),
            ImageChooserPanel('price_image'),
            FieldPanel('price_alt_text'),
        ], heading="Precios Combustibles", classname="collapsible",
            help_text='Precios Combustibles'),
        MultiFieldPanel([
            FieldPanel('history_price_title'),
            FieldPanel('history_price_intro'),
            ImageChooserPanel('history_price_image'),
            FieldPanel('history_price_alt_text'),
        ], heading="Hist??rico Precios de Combustibles", classname="collapsible",
            help_text='Hist??rico Precios de Combustibles'),
        MultiFieldPanel([
            FieldPanel('prices_links_title'),
            StreamFieldPanel('prices_links'),
        ], heading="Precios Reportados por la EDS ", classname="collapsible",
            help_text='Precios Reportados por la EDS '),
        MultiFieldPanel([
            FieldPanel('zone_title'),
            FieldPanel('zone_intro'),
            ImageChooserPanel('zone_image'),
            FieldPanel('zone_alt_text'),
        ], heading="Zonas de frontera", classname="collapsible",
            help_text='Zonas de frontera'),
        MultiFieldPanel([
            FieldPanel('vol_title'),
            StreamFieldPanel('vol_tabs_list'),
        ], heading="Asignaci??n de vol??menes m??ximos", classname="collapsible",
            help_text='Asignaci??n de vol??menes m??ximos'),
        MultiFieldPanel([
            FieldPanel('plan_title'),
            FieldPanel('plan_intro'),
            StreamFieldPanel('plan_tabs_list'),
        ], heading="Plan de abastecimiento", classname="collapsible",
            help_text='Plan de abastecimiento'),
        MultiFieldPanel([
            FieldPanel('program_title'),
            StreamFieldPanel('program_intro'),
        ], heading="Programa reconversi??n socio-laboral", classname="collapsible",
            help_text='Programa reconversi??n socio-laboral'),
    ]


class MidstreamPage(Page):
    subpage_types = []

    how_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    how = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro_one = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n primer bloque',
        verbose_name="Introducci??n"
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    sicom_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Transporte de crudos")
    sicom_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    sicom_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sicom_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    chain_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    chain_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    menu_list = StreamField(
        [('Menu', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Items")

    plan_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Impuesto de Transporte")
    plan_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    plan_tabs_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")

    price_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Transporte de Biocombustibles")
    price_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    price_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    price_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('how_title'),
            FieldPanel('how'),
        ], heading="Transporte de combustibles l??quidos y GPL", classname="collapsible",
            help_text='Transporte de combustibles l??quidos y GPL'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro_one'),
            FieldPanel('second_intro'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Transporte de combustibles l??quidos y GPL y Biocombustibles por v??a terrestre", classname="collapsible",
            help_text='Transporte de combustibles l??quidos y GPL y Biocombustibles por v??a terrestre'),
        MultiFieldPanel([
            FieldPanel('sicom_title'),
            FieldPanel('sicom_intro'),
            ImageChooserPanel('sicom_image'),
            FieldPanel('sicom_alt_text'),
        ], heading="Transporte de crudos", classname="collapsible",
            help_text='Transporte de crudos'),
        MultiFieldPanel([
            FieldPanel('chain_title'),
            FieldPanel('chain_intro'),
        ], heading="Construcci??n de oleoductos, conexiones y conversiones", classname="collapsible",
            help_text='Construcci??n de oleoductos, conexiones y conversiones'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            FieldPanel('menu_list_intro'),
            StreamFieldPanel('menu_list'),
        ], heading="Fijaci??n de tarifas de transporte de crudo por oleoducto", classname="collapsible",
            help_text='Fijaci??n de tarifas de transporte de crudo por oleoducto'),
        MultiFieldPanel([
            FieldPanel('plan_title'),
            FieldPanel('plan_intro'),
            StreamFieldPanel('plan_tabs_list'),
        ], heading="Impuesto de Transporte", classname="collapsible",
            help_text='Impuesto de Transporte'),
        MultiFieldPanel([
            FieldPanel('price_title'),
            FieldPanel('price_intro'),
            ImageChooserPanel('price_image'),
            FieldPanel('price_alt_text'),
        ], heading="Transporte de Biocombustibles", classname="collapsible",
            help_text='Transporte de Biocombustibles'),

    ]


class UpstreamPage(Page):
    subpage_types = []

    exploration_exploitation_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    exploration_icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono',
        verbose_name="Icono"
    )
    exploration_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    exploration_intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    exploration_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")
    exploration_intro_three = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    exploitation_icon = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Icono',
        verbose_name="Icono"
    )
    exploitation_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    exploitation_intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    exploitation_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")
    exploitation_intro_three = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    certificates_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo',
        verbose_name='T??tulo de la secci??n')
    certificates_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    certificates_list = StreamField(
        [('Elementos', AccodionRichTextStructBlock())], blank=True, verbose_name="Acorde??n")

    form_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo',
        verbose_name='T??tulo de la secci??n')
    form_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    form_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    slider_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo',
        verbose_name='T??tulo de la secci??n')
    slider = StreamField(
        [('slider', SliderStructBlock())], blank=True, verbose_name="Slider")

    myths_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo',
        verbose_name='T??tulo de la secci??n')
    myths_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    myths_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tabs_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo',
        verbose_name='T??tulo de la secci??n')
    tabs = StreamField(
        [('Elementos', TabTableStructBlock())], blank=True, verbose_name="Pesta??as")

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('exploration_exploitation_title'),
        ], heading="Exploraci??n y Explotaci??n", classname="collapsible",
            help_text='Exploraci??n y Explotaci??n'),
        MultiFieldPanel([
            SvgChooserPanel('exploration_icon'),
            FieldPanel('exploration_intro'),
            FieldPanel('exploration_intro_two'),
            StreamFieldPanel('exploration_list'),
            FieldPanel('exploration_intro_three'),
        ], heading="Exploraci??n", classname="collapsible",
            help_text='Exploraci??n'),
        MultiFieldPanel([
            SvgChooserPanel('exploitation_icon'),
            FieldPanel('exploitation_intro'),
            FieldPanel('exploitation_intro_two'),
            StreamFieldPanel('exploitation_list'),
            FieldPanel('exploitation_intro_three'),
        ], heading="Explotaci??n", classname="collapsible",
            help_text='Explotaci??n'),
        MultiFieldPanel([
            FieldPanel('certificates_title'),
            FieldPanel('certificates_intro'),
            StreamFieldPanel('certificates_list'),
        ], heading="Certificados de Dedicaci??n Exclusiva", classname="collapsible",
            help_text='Certificados de Dedicaci??n Exclusiva'),
        MultiFieldPanel([
            FieldPanel('form_title'),
            FieldPanel('form_intro'),
            StreamFieldPanel('form_list'),
        ], heading="Formas Oficiales", classname="collapsible",
            help_text='Formas Oficiales'),
        MultiFieldPanel([
            FieldPanel('slider_title'),
            StreamFieldPanel('slider'),
        ], heading="Producci??n", classname="collapsible",
            help_text='Producci??n'),
        MultiFieldPanel([
            FieldPanel('myths_title'),
            ImageChooserPanel('myths_image_one'),
            ImageChooserPanel('myths_image_two'),
        ], heading="Mitos y Realidades", classname="collapsible",
            help_text='Mitos y Realidades'),
        MultiFieldPanel([
            FieldPanel('tabs_title'),
            StreamFieldPanel('tabs'),
        ], heading="Proyectos Piloto de Inversi??n Integral", classname="collapsible",
            help_text='Proyectos Piloto de Inversi??n Integral'),
    ]


class AsesoriaJuridicaPage(Page):
    subpage_types = []

    form_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    form_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('form_intro'),
            StreamFieldPanel('form_list'),
        ], heading="Asesor??a Jur??dica", classname="collapsible",
            help_text='Asesor??a Jur??dica'),
    ]


class GestionProyectosOptimizacionPage(Page):
    subpage_types = []

    form_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    form_list = StreamField(
        [('Elementos', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('form_intro'),
            StreamFieldPanel('form_list'),
        ], heading="Gesti??n de Proyectos y Optimizaci??n", classname="collapsible",
            help_text='Gesti??n de Proyectos y Optimizaci??n'),
    ]




class CapacidadGeneracionEnergiaElectricaPage(Page):

    subpage_types = ['CapacidadIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default=" Capacidad de generaci??n de energ??a el??ctrica a partir de FNCER")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Infograf??as",
        help_text='Infograf??a',
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('infographic'),
        ], heading="Infograf??a", classname="collapsible"),

    ]


class ConstruccionProyectosEolicosPage(Page):

    subpage_types = ['ConstruccionIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default=" Construcci??n de proyectos e??licos en La Guajira")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Infograf??as",
        help_text='Infograf??a',
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('infographic'),
        ], heading="Infograf??a", classname="collapsible"),

    ]


class NuevosHogaresServicioEnergiaElectricaPage(Page):

    subpage_types = ['NuevosHogaresIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Nuevos hogares con servicio de energ??a el??ctrica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Infograf??as",
        help_text='Infograf??a',
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('infographic'),
        ], heading="Infograf??a", classname="collapsible"),

    ]


class MarcoNormativoAprovechamientoPage(Page):

    subpage_types = ['MarcoNormativoIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Marco normativo del aprovechamiento geot??rmico")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    intro_image = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )
    document_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        verbose_name="Documento",
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('infographic'),
            FieldPanel('image_alt_text'),
            FieldPanel('intro_image'),
            DocumentChooserPanel('document_file'),
        ], heading="Bloque", classname="collapsible"),

    ]


class ImplementacionMisionPage(Page):

    subpage_types = ['ImplementacionIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Implementaci??n de la Misi??n de Transformaci??n Energ??tica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    images_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_one = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_two = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    video_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    link_video_two = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Infograf??as",
        help_text='Infograf??a',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link = models.URLField(
        "Link del sitio", blank=True)
    infographic_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('images_title'),
            ImageChooserPanel('image_one'),
            FieldPanel('alt_text_one'),
            ImageChooserPanel('image_two'),
            FieldPanel('alt_text_two'),
        ], heading="Imagenes", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('video_title'),
            FieldPanel('link_video'),
            FieldPanel('link_video_two'),
        ], heading="Videos", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('infographic'),
            FieldPanel('link'),
            FieldPanel('infographic_button_title'),
        ], heading="Infograf??a", classname="collapsible"),

    ]


class ReglamentacionLeyPage(Page):

    subpage_types = ['ReglamentacionIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default=" Reglamentaci??n de la Ley de Transici??n Energ??tica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
    ]


class DiversificacionMineraPage(Page):

    subpage_types = ['DiversificacionIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Diversificaci??n minera como aliada de la transici??n energ??tica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),


    ]


class SubastasEnergiasRenovablesPage(Page):

    subpage_types = ['SubastasEnergiasIndexPage',
                     'SubastasDocumentoUnidadIndexPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Subastas de energ??as renovables")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )

    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )
    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    subasta_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    subasta_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de subastas',
        verbose_name='??ndice de noticias'
    )
    subasta_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('news_list_title'),
            PageChooserPanel('news_list'),
            FieldPanel('news_button_title'),
        ], heading="Noticias", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('subasta_list_title'),
            PageChooserPanel('subasta_list'),
            FieldPanel('subasta_button_title'),
        ], heading="Subastas", classname="collapsible"),


    ]


class FuncionesPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Funciones")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
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
            FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),

    ]


class EnergiaElectricaPage(Page):

    subpage_types = ['EnergiaFuncionamientoSectorPage',
                     'EnergiaReglamentosTecnicosPage', 'TarifasSubsidiosRedNacionalPage', 'PlanesExpansionPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Energ??a el??ctrica")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_intro'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
        ], heading="Indicadores del MEM", classname="collapsible",
            help_text='Indicadores del MEM'),

    ]


class EnergiaFuncionamientoSectorPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Funcionamiento del Sector")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    title_one = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="??C??mo est?? integrado el sector el??ctrico colombiano?")
    intro_one = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video_one = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_one = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    title_two = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Estructura y Gobernanza")
    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video_two = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_two = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    title_three = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="??Qu?? hacemos?")
    intro_three = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video_three = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_three = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    title_pbi = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    link_pbi_one = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image_pbi_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_one = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    link_pbi_two = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image_pbi_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text_two = models.TextField(verbose_name="Texto alternativo", blank=True,
                                    help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('title_one'),
            FieldPanel('intro_one'),
            FieldPanel('link_video_one'),
            ImageChooserPanel('image_one'),
            FieldPanel('alt_text_one'),
        ], heading="??C??mo est?? integrado el sector el??ctrico colombiano?", classname="collapsible",
            help_text='??C??mo est?? integrado el sector el??ctrico colombiano?'),
        MultiFieldPanel([
            FieldPanel('title_two'),
            FieldPanel('intro_two'),
            FieldPanel('link_video_two'),
            ImageChooserPanel('image_two'),
            FieldPanel('alt_text_two'),
        ], heading="Estructura y Gobernanza", classname="collapsible",
            help_text='Estructura y Gobernanza'),
        MultiFieldPanel([
            FieldPanel('title_three'),
            FieldPanel('intro_three'),
            FieldPanel('link_video_three'),
            ImageChooserPanel('image_three'),
            FieldPanel('alt_text_three'),
        ], heading="??Qu?? hacemos?", classname="collapsible",
            help_text='??Qu?? hacemos?'),
        MultiFieldPanel([
            FieldPanel('title_pbi'),
            FieldPanel('link_pbi_one'),
            ImageChooserPanel('image_pbi_one'),
            FieldPanel('alt_text_one'),
        ], heading="Recomendaciones Misi??n Hoja de Ruta", classname="collapsible",
            help_text='Recomendaciones Misi??n Hoja de Ruta'),
        MultiFieldPanel([
            FieldPanel('link_pbi_two'),
            ImageChooserPanel('image_pbi_two'),
            FieldPanel('alt_text_two'),
        ], heading="Recomendaciones Misi??n Hoja de Ruta", classname="collapsible",
            help_text='Recomendaciones Misi??n Hoja de Ruta'),
    ]


class EnergiaReglamentosTecnicosPage(Page):
    subpage_types = ['ReglamentoTecnicoInstalacionesElectricasPage', 'ReglamentoTecnicoEtiquetadoPage', 'ReglamentoTecnicoIluminacionAlumbradoPublicoPage',
                     'ReglamentoTecnicoSistemasInstalacionesTermicasPage', 'PreguntasFrecuentesReglamentosTecnicosSectorEnergiaElectricaPage']
    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Reglamentos T??cnicos")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    elements_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    elements_list = StreamField(
        [('Menu_reglamentos_tecnicos', ElementsListStructBlock())], blank=True, verbose_name="Menu reglamentos tecnicos")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            StreamFieldPanel('second_links'),
        ], heading="Enlaces secundarios", classname="collapsible",
            help_text='Enlaces secundarios de la secci??n'),
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            StreamFieldPanel('tab_list'),
        ], heading="Memorias talles y otros encuentros", classname="collapsible",
            help_text='Memorias talles y otros encuentros'),
        MultiFieldPanel([
            FieldPanel('elements_list_title'),
            StreamFieldPanel('elements_list'),
        ], heading="Menu_reglamentos_tecnicos", classname="collapsible",
            help_text='Menu reglamentos tecnicos'),
    ]




class ReglamentoTecnicoInstalacionesElectricasPage(Page):
    subpage_types = []

    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    menu_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="RETIE Vigente")

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Relaci??n Cronol??gica RETIE ")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('tab_list'),
        ], heading="Pesta??as", classname="collapsible",
            help_text='Pesta??as'),
        MultiFieldPanel([
            FieldPanel('menu_list_title'),
            StreamFieldPanel('menu_list'),
        ], heading="Lineamientos y Pol??ticas", classname="collapsible",
            help_text='Lineamientos y Pol??ticas'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            StreamFieldPanel('retie_list'),
        ], heading="Relaci??n Cronol??gica RETIE", classname="collapsible",
            help_text='Relaci??n Cronol??gica RETIE'),
    ]


class ReglamentoTecnicoEtiquetadoPage(Page):
    subpage_types = []

    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    tab_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_links_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    projects_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    projects_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    actions_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    actions_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    actions_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")

    training_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    training_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    tools_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    tools_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('tab_intro'),
            StreamFieldPanel('tab_list'),
        ], heading="Antecedentes", classname="collapsible",
            help_text='Antecedentes'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            FieldPanel('second_links_intro'),
            StreamFieldPanel('second_links'),
        ], heading="Reglamento", classname="collapsible",
            help_text='Reglamento'),
        MultiFieldPanel([
            FieldPanel('projects_title'),
            FieldPanel('projects_intro'),
        ], heading="Proyectos de actualizaci??n", classname="collapsible",
            help_text='Proyectos de actualizaci??n'),
        MultiFieldPanel([
            FieldPanel('actions_title'),
            FieldPanel('actions_intro'),
            StreamFieldPanel('actions_list'),
        ], heading="Acciones de implementaci??n", classname="collapsible",
            help_text='Acciones de implementaci??n'),
        MultiFieldPanel([
            FieldPanel('training_title'),
            FieldPanel('training_intro'),
        ], heading="Formaci??n Complementaria en RETIQ", classname="collapsible",
            help_text='Formaci??n Complementaria en RETIQ'),
        MultiFieldPanel([
            FieldPanel('tools_title'),
            FieldPanel('tools_intro'),
        ], heading="Herramientas Inform??ticas", classname="collapsible",
            help_text='Herramientas Inform??ticas'),

    ]


class ReglamentoTecnicoIluminacionAlumbradoPublicoPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Men??")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
            StreamFieldPanel('second_links'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Men??", classname="collapsible",
            help_text='Men??'),

    ]


class ReglamentoTecnicoSistemasInstalacionesTermicasPage(Page):
    subpage_types = []

    intro_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    menu_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Men??")

    actions_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    actions_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('menu_title'),
            StreamFieldPanel('menu_list'),
        ], heading="Men??", classname="collapsible",
            help_text='Men??'),
        MultiFieldPanel([
            FieldPanel('actions_title'),
            StreamFieldPanel('actions_intro'),
        ], heading="Acciones de implementaci??n", classname="collapsible",
            help_text='Acciones de implementaci??n'),

    ]


class PreguntasFrecuentesReglamentosTecnicosSectorEnergiaElectricaPage(Page):
    subpage_types = []

    actions_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    element_list = StreamField(
        [('Lista', HeaderMenuBlockAcordeon())], blank=True, verbose_name="Preguntas Frecuentes")




    
    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel('actions_intro'),
        ], heading="Indroducci??n", classname="collapsible",
            help_text='Indroducci??n'),

        MultiFieldPanel([
            StreamFieldPanel('element_list'),
        ], heading="Preguntas Frecuentes Reglamentos", classname="collapsible",
            help_text='Preguntas Frecuentes Reglamentos'),

    ]


class TarifasSubsidiosRedNacionalPage(Page):

    subpage_types = ['FazniPage', 'PronePage',
                     'FoesPage', 'FfsriPage', 'FaerPage', 'FenogePage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Tarifas y Subsidios Red Nacional")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    cards_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    cards_list = StreamField(
        [('Documentos', LinkDocumentCardSliderStructBlock())], blank=True, verbose_name="Documentos")

    second_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    second_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    second_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                       help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    third_link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    third_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    third_alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                      help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('cards_list_title'),
            StreamFieldPanel('cards_list'),
        ], heading="Fondos Especiales", classname="collapsible",
            help_text='Fondos Especiales'),
        MultiFieldPanel([
            FieldPanel('second_title'),
            FieldPanel('second_link_pbi'),
            ImageChooserPanel('second_image'),
            FieldPanel('second_alt_text'),
            FieldPanel('third_link_pbi'),
            ImageChooserPanel('third_image'),
            FieldPanel('third_alt_text'),
        ], heading="Tarifas y componentes", classname="collapsible",
            help_text='Tarifas y componentes'),
    ]


class FazniPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    menu_list = StreamField(
        [('Items', SimpleBriefcaseStructBlock())], blank=True, verbose_name="Men??")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            StreamFieldPanel('menu_list'),
        ], heading="Men??", classname="collapsible",
            help_text='Men??'),

    ]


class PronePage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    second_links_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Actas PRONE")

    title_list_one = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Convocatorias PRONE")
    list_one = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('second_links_title'),
            StreamFieldPanel('second_links'),
        ], heading="Circulares FAER PRONE", classname="collapsible",
            help_text='Circulares FAER PRONE'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            StreamFieldPanel('retie_list'),
        ], heading="Actas CAPRONE", classname="collapsible",
            help_text='Actas CAPRONE'),
        MultiFieldPanel([
            FieldPanel('title_list_one'),
            StreamFieldPanel('list_one'),
        ], heading="Convocatorias PRONE", classname="collapsible",
            help_text='Convocatorias PRONE'),

    ]


class FoesPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Circulares e Instructivos")

    title_list_one = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Subsidios de Energ??a Social - FOES")
    list_one = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            StreamFieldPanel('retie_list'),
        ], heading="Circulares e Instructivos", classname="collapsible",
            help_text='Circulares e Instructivos'),
        MultiFieldPanel([
            FieldPanel('title_list_one'),
            StreamFieldPanel('list_one'),
        ], heading="Subsidios de Energ??a Social - FOES", classname="collapsible",
            help_text='Subsidios de Energ??a Social - FOES'),

    ]


class FfsriPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    block_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    title_list_one = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Circulares FSSRI")
    list_one = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    block_two_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_two_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    block_three_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_three_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    list_two = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    title_list_three = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Subsidios Sistema Inteconectado Nacional - SIN")
    list_three = StreamField(
        [('Lista', AccordeonRichTextStructBlock())], blank=True, verbose_name="Lista")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('block_title'),
            FieldPanel('block_intro'),
        ], heading="Instructivos y Formatos", classname="collapsible",
            help_text='Instructivos y Formatos'),
        MultiFieldPanel([
            FieldPanel('title_list_one'),
            StreamFieldPanel('list_one'),
        ], heading="Circulares FSSRI", classname="collapsible",
            help_text='Circulares FSSRI'),
        MultiFieldPanel([
            FieldPanel('block_two_title'),
            FieldPanel('block_two_intro'),
        ], heading="Subsidios Zonas No Interconectadas - ZNI", classname="collapsible",
            help_text='Subsidios Zonas No Interconectadas - ZNI'),
        MultiFieldPanel([
            FieldPanel('block_three_title'),
            FieldPanel('block_three_intro'),
            StreamFieldPanel('list_two'),
        ], heading="Desembolsos para pagos de subsidios ZNI", classname="collapsible",
            help_text='Desembolsos para pagos de subsidios ZNI'),
        MultiFieldPanel([
            FieldPanel('title_list_three'),
            StreamFieldPanel('list_three'),
        ], heading="Subsidios Sistema Inteconectado Nacional - SIN", classname="collapsible",
            help_text='Subsidios Sistema Inteconectado Nacional - SIN'),
    ]


class FaerPage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Circulares e Instructivos")

    block_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    actions_list = StreamField(
        [('Enlaces', ElementsListStructBlock())], blank=True, verbose_name="Enlaces de la secci??n")
    table_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Acuerdos")

    block_two_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_two_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    table_two_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Actas")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            StreamFieldPanel('retie_list'),
        ], heading="Circulares e Instructivos", classname="collapsible",
            help_text='Circulares e Instructivos'),
        MultiFieldPanel([
            FieldPanel('block_title'),
            FieldPanel('block_intro'),
            StreamFieldPanel('actions_list'),
            StreamFieldPanel('table_list'),
        ], heading="Electrificaci??n Rural en el Sistema Interconectado Nacional", classname="collapsible",
            help_text='Electrificaci??n Rural en el Sistema Interconectado Nacional'),
        MultiFieldPanel([
            FieldPanel('block_two_title'),
            FieldPanel('block_two_intro'),
            StreamFieldPanel('table_two_list'),
        ], heading="Planes de Expansi??n El??ctrica del Sistema Interconectado Nacional - SIN", classname="collapsible",
            help_text='Planes de Expansi??n El??ctrica del Sistema Interconectado Nacional - SIN'),


    ]


class FenogePage(Page):
    subpage_types = []

    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Resoluciones")

    block_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    block_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            StreamFieldPanel('retie_list'),
        ], heading="Resoluciones", classname="collapsible",
            help_text='Resoluciones'),
        MultiFieldPanel([
            FieldPanel('block_title'),
            FieldPanel('block_intro'),
        ], heading="Actas de Comit?? Directivo", classname="collapsible",
            help_text='Actas de Comit?? Directivo'),

    ]


class PlanesExpansionPage(Page):

    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Planes de Expansi??n")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_video = models.URLField(
        "Video", blank=True, help_text='Si completa este campo, la imagen no ser?? presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    intro_one = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    second_links = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    resolutions_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Resoluciones")
    resolutions_list = StreamField(
        [('Enlaces', SecondLinkStructBlock())], blank=True, verbose_name="Enlaces secundarios")

    tab_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    intro_tab = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    tab_list = StreamField(
        [('Tabs', TabsListStructBlock())], blank=True, verbose_name="Pesta??as")

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tama??o recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripci??n del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripci??n"
    )
    featured_link = models.URLField(
        "Enlace destacado", blank=True)

    retie_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    retie_intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    retie_list = StreamField(
        [('Items', RETIETableStructBlock())], blank=True, verbose_name="Resoluciones")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_video'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('intro_one'),
            StreamFieldPanel('second_links'),
        ], heading="Informaci??n complemetaria", classname="collapsible",
            help_text='Informaci??n complemetaria'),
        MultiFieldPanel([
            FieldPanel('resolutions_title'),
            StreamFieldPanel('resolutions_list'),
        ], heading="Resoluciones", classname="collapsible",
            help_text='Resoluciones'),
        MultiFieldPanel([
            FieldPanel('tab_list_title'),
            FieldPanel('intro_tab'),
            StreamFieldPanel('tab_list'),
        ], heading="Plan Indicativo de Expansi??n de Cobertura de Energ??a El??ctrica ??? PIEC", classname="collapsible",
            help_text='Plan Indicativo de Expansi??n de Cobertura de Energ??a El??ctrica ??? PIEC'),
        MultiFieldPanel([
            FieldPanel('text_link'),
            ImageChooserPanel('image_link'),
            FieldPanel('featured_link'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la secci??n'),
        MultiFieldPanel([
            FieldPanel('retie_list_title'),
            FieldPanel('retie_intro'),
            StreamFieldPanel('retie_list'),
        ], heading="Declaratoria de Utilidad P??blica e Inter??s Social DUPIS ", classname="collapsible",
            help_text='Declaratoria de Utilidad P??blica e Inter??s Social DUPIS '),

    ]




class UnidadResultadosPage(Page):
    
    subpage_types = ['FuncionesPage','UnidadResultadoNoticias','ConoceUnidadResultadosPage']

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Unidad de Resultados")
    
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    image_link = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Tama??o recomendado, Alto: 375px, Ancho:1920px',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_link = RichTextField(
        null=True,
        blank=True,
        help_text='Descripci??n del elemento, longitud recomendada 85 caracteres',
        verbose_name="Descripci??n"
    )

    button_title = models.CharField(
        "T??tulo del boton", max_length=254, help_text='T??tulo del boton')
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

    featured_link = StreamField(
        [('Enlace', FeaturedLinkStructBlock())], blank=True, verbose_name="Enlace destacado", min_num=0, max_num=1)

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
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('text_link'),
            ImageChooserPanel('image_link'),
            StreamFieldPanel('featured_link'),
        ], heading="Enlace destacado", classname="collapsible",
            help_text='Enlace destacado de la secci??n'),
    ]




#! noticias de unidad de resultados
class UnidadResultadosAutorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Autor` 
    and the UnidadResultadoPage below. This allows Autor to be added to a UnidadResultadoPage.
    """
    page = ParentalKey(
        'UnidadResultadoPage', related_name='unidad_resultados_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='unidad_resultados_autor_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]



class UnidadResultado1NoticiaSectorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sector` 
    and the UnidadResultadoPage below. This allows Sector to be added to a UnidadResultadoPage.

    """
    page = ParentalKey(
        'UnidadResultadoPage', related_name='unidad_resultados1_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='unidad_resultados1_sector_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class UnidadResultadoPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the UnidadResultadoPage object and tags.
    """
    content_object = ParentalKey(
        'UnidadResultadoPage', related_name='unidad_resultado_tagged_items', on_delete=models.CASCADE)


class UnidadResultadoPage(Page):
    
    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=UnidadResultadoPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicaci??n", blank=False, null=True
    )
    # new section

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Noticia")
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")
    intro_two = RichTextField(
        null=True,
        blank=True,
        help_text='Bloque de texto',
        verbose_name="Bloque de texto"
    )


    image_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )
    infographic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Infograf??as",
        help_text='Infograf??a',
        on_delete=models.SET_NULL,
        related_name='+'
    )

    link_list = StreamField(
        [('Enlaces', ElementsListStructMenuBlock())], blank=True, verbose_name="Enlaces de la secci??n documentos")


    news_list = StreamField(
        [('Enlaces', HeaderStructBlock())], blank=False, verbose_name="Enlace de mas noticias")

    body = StreamField(
        BaseStreamBlock(), verbose_name="Cuerpo de la noticia", blank=False
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            # FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
            # FieldPanel('intro_two'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),

        StreamFieldPanel('body'),

        # MultiFieldPanel([
        #     StreamFieldPanel('link_list'),
        # ], heading="Enlaces", classname="collapsible",
        #     help_text='Listas de enlaces'),
        # MultiFieldPanel([
        #     FieldPanel('image_title'),
        #     ImageChooserPanel('infographic'),
        # ], heading="Infograf??a", classname="collapsible"),

        # MultiFieldPanel([
        #     StreamFieldPanel('news_list'),
        # ], heading="Enlace de historial", classname="collapsible"),
        
        

        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'unidad_resultados_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'unidad_resultados1_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
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
            n.autor for n in self.unidad_resultados_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        """
        Returns the UnidadResultadoPage's related Sector. Again note that we are using
        the ParentalKey's related_name from the NoticiaSectorRelationship model
        to access these objects. This allows us to access the Sector objects
        with a loop on the template. If we tried to access the noticia_sector_
        relationship directly we'd print `noticia.NoticiaSectorRelationship.None`
        """
        sectors = [
            n.sector for n in self.unidad_resultados1_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.unidad_resultados1_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.unidad_resultados_autor_relationship.all()
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
        return UnidadResultadoPage.objects.live().order_by('-date_published')[:6]

    # Specifies parent to UnidadResultadoPage as being NoticiaIndexPages
    parent_page_types = ['UnidadResultadoIndexPage']

    # Specifies what content types can exist as children of UnidadResultadoPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('body'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-850x450-c50', source='image')),

    ]


class UnidadResultadoIndexPage(RoutablePageMixin, Page):

    # Speficies that only UnidadResultadoPage objects can live under this index page
    subpage_types = ['UnidadResultadoPage']

    # Defines a method to access the children of the page (e.g. UnidadResultadoPage
    # objects).
    def children(self):
        return UnidadResultadoPage.objects.descendant_of(self).live().order_by('-date_published')

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(UnidadResultadoIndexPage, self).get_context(request)
        context['posts'] = UnidadResultadoPage.objects.descendant_of(
            self).live().order_by('-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child UnidadResultadoPage objects for this NoticiaPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = UnidadResultadoPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this UnidadResultadoPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class UnidadResultadoNoticias(Page):

    subpage_types = ['UnidadResultadoIndexPage']
    news_list_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='T??tulo que ser?? presentado al publico',
        verbose_name='T??tulo de la secci??n'
    )

    news_list = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Seleccione la p??gina del ??ndice de noticias',
        verbose_name='??ndice de noticias'
    )

    news_button_title = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        help_text='T??tulo del bot??n m??s informaci??n que ser?? presentado al p??blico, longitud m??xima 20 caracteres',
        verbose_name='T??tulo bot??n m??s informaci??n'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            MultiFieldPanel(
                [FieldPanel('news_list_title'), PageChooserPanel('news_list'), FieldPanel('news_button_title'), ]),
        ], heading="Noticias", classname="collapsible"),
    ]





class ConoceUnidadResultadosPage(Page):
    
    subpage_types = []

    intro_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Unidad de Resultados")
    
    intro = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    link_pbi = models.URLField(
        verbose_name="Link tablero Power BI", blank=True, help_text='Link de acceso al tablero Power BI',)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text='Imagen que representa la secci??n',
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.TextField(verbose_name="Texto alternativo", blank=True,
                                help_text="Este atributo proporciona informaci??n alternativa para una imagen si un usuario, por alguna raz??n, no puede verla (debido a una conexi??n lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    objetivos_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Objetivos transformacionales minero-energ??ticos")

    intro_objetivos = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )
    modelo_title = models.CharField(
        "T??tulo de la secci??n", max_length=254, null=False, blank=False, default="Modelo de Gesti??n del Cumplimiento")

    intro_modelo = RichTextField(
        null=True,
        blank=True,
        help_text='Introducci??n de la secci??n',
        verbose_name="Introducci??n"
    )


    link_list = StreamField(
        [('Enlaces', ElementsListStructMenuBlock())], blank=True, verbose_name="Enlaces de la secci??n documentos")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro'),
            FieldPanel('link_pbi'),
            ImageChooserPanel('image'),
            FieldPanel('alt_text'),
        ], heading="Introducci??n", classname="collapsible",
            help_text='Introducci??n de la secci??n'),
        MultiFieldPanel([
            FieldPanel('objetivos_title'),
            FieldPanel('intro_objetivos'),
        ], heading="intro objetivos", classname="collapsible",
            help_text='intro objetivos de la secci??n'),
        MultiFieldPanel([
            FieldPanel('modelo_title'),
            FieldPanel('intro_modelo'),
        ], heading="Modelo de Gesti??n del Cumplimiento", classname="collapsible",
            help_text='Modelo de Gesti??n del Cumplimiento secci??n'),
        
        MultiFieldPanel([
            StreamFieldPanel('link_list'),
        ], heading="Enlaces", classname="collapsible",
            help_text='Listas de enlaces'),
    ]



