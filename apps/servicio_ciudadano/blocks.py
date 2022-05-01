from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.blocks import (
    CharBlock,  StructBlock, URLBlock, PageChooserBlock, StructValue, ListBlock, TextBlock, RichTextBlock
)
from wagtailsvg.blocks import SvgChooserBlock


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class ParticipationListStructBlock(StructBlock):
    title = CharBlock(label="Titulo", required=True,
                      help_text="Titulo del mecanismo de participación")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del mecanismo de participación, solo imágenes en formato SVG.")
    description = TextBlock(label="Descripción del elemento", required=True,
                            help_text="Descripción del mecanismo de participación")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class SliderStructBlock(StructBlock):

    image = ImageChooserBlock(label="Imagen", required=False, blank=True,
                              help_text='Tamaño recomendado de la imagen 1820px X 680px pixeles')

    video = URLBlock(label="Link video", required=False, blank=False,
                     help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85')

    page = PageChooserBlock(label="Link a página local", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este slider con una página local')

    external_url = URLBlock(label="Link a página externa", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')

    class Meta:
        icon = 'image'
        value_class = LinkStructValue
        closed = True


class IconMenuStructBlock(StructBlock):
    """Class that provides the structure for icon menu sections
    ...
    Methods
    -------
    None
    """
    title = CharBlock(label="Titulo", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    description = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        help_text="Descripción del elemento",
        required=True,
    )

    subitems = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(label="Imagen", required=False, blank=True,
                                            help_text='Imagen del documento')),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                 help_text="Link al documento"))
            ],
            icon='doc-empty',

        ),
        required=False,
        blank=True,
        label="Lista de documentos",
        help_text="Lista de documentos que serán presentados en el slider de la sección "

    )
    taps = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(label='Subitem', required=True, blank=False,
                 help_text="Subitems que serán presentados como pestañas")),
                ('description', RichTextBlock(
                    icon="fa-paragraph",
                    label="Descripción",
                    help_text="Descripción del elemento",
                    required=True,
                )),
            ],
            icon='link',

        ),
        required=False,
        blank=True,
        label="Lista de pestañas",
        help_text="Lista de elementos que serán presentados como pestañas"

    )

    class Meta:
        icon = 'list-ol'
        value_class = LinkStructValue


class HeaderMenuBlock(StructBlock):
    title = CharBlock(label="Nombre", required=True,
                      help_text="Nombre del elemento")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono, solo imágenes en formato SVG.")
    text = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        help_text="Descripción del elemento",
        required=True,
    )

    class Meta:
        icon = 'link'
