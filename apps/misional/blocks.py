from wagtail.core.blocks import (
    StructBlock, TextBlock, URLBlock, PageChooserBlock, StructValue,
    CharBlock, RichTextBlock, DateBlock, EmailBlock, ListBlock, StreamBlock, ChoiceBlock
)
from wagtailsvg.blocks import SvgChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from django.db import models


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class LinkListStructBlock(StructBlock):
    title = CharBlock(label="Titulo del elemento", required=True,
                      help_text="Titulo del elemento.")
    icono = SvgChooserBlock(label="Icono del elemento", required=True,
                            help_text="Icono del link, solo se acepta imágenes en formato SVG.")
    description = CharBlock(label="Descripción del elemento", required=True,
                            help_text="Descripción del elemento")
    enlaces = ListBlock(
        StructBlock(
            [('name', CharBlock(label='Texto del link', required=True, blank=False, help_text="Texto del link que será mostrado al público.")),
                ('page', PageChooserBlock(
                    label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
                ('external_url', URLBlock(
                    label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),
             ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=True

    )

    class Meta:
        icon = 'link'


class FeaturedLinkStructBlock(StructBlock):

    page = PageChooserBlock(label="Link a página local:",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class ImageTextStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")

    description = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        help_text="Descripción del elemento",
        required=True,
    )

    image = ImageChooserBlock(label="Imagen", required=False, blank=False,
                              help_text='Imagen')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')
    align = ChoiceBlock(
        label='Alinear imagen a la izquierda',
        required=False,
        help_text="Si esta opción esta activa, la imagen se alineara a la izquierda, por defecto se alineará a la derecha.",
        choices=[
            ('true', 'Izquierda'),
        ],
    )

    class Meta:
        icon = 'list-ul'


class SliderStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del slider")

    image = ImageChooserBlock(label="Imagen", required=True, blank=False,
                              help_text='Tamaño recomendado de la imagen 1820px pixeles.')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).')

    page = PageChooserBlock(label="Link a página local", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este slider con una página local.')

    external_url = URLBlock(label="Link a página externa", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')

    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo del slider.',
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'],
    )

    class Meta:
        """Metaclase"""
        icon = 'image'
        value_class = LinkStructValue
        closed = True


class TabTableStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    intro = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    subitems = ListBlock(
        StructBlock(
            [
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
                ('date', TextBlock(label='Fecha', required=True, blank=False,
                                   help_text="Fecha en formato 28/02/2021")),
                ('description', RichTextBlock(
                    icon="fa-paragraph",
                    label="Descripción:",
                    required=False,
                    template="blocks/paragraph_block.html",
                    help_text='Breve descripción',
                    features=['h2', 'h3', 'h4', 'bold',
                              'italic', 'link', 'hr'],
                ))
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos que se presentaran en formato tabla dentro de una pestaña"

    )


class RETIETableStructBlock(StructBlock):

    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")
    intro = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )

class HeaderMenuBlockAcordeon(StructBlock):
    title = CharBlock(label="Nombre", required=True,
                    help_text="Nombre del elemento")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono, solo imágenes en formato SVG.")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('subitems_acordeon', ListBlock(
                    StructBlock(
                        [
                            ('title', CharBlock(label='Título del elemento', required=True, blank=False,
                                                help_text="Título del elemento")),
                            ('subitems_acordeon_body', ListBlock(
                                StructBlock(
                                    [
                                        ('description', RichTextBlock(
                                            icon="fa-paragraph",
                                            label="Descripción",
                                            required=False,
                                            help_text='Breve descripción',
                                        ))
                                    ]
                                ),
                                required=False,
                                blank=True,
                                label="Lista de elementos",
                                help_text="Lista de elementos que se presentaran"
                            )
                            ),

                        ],
                    ),
                    required=False,
                    blank=True,
                    label="Lista de elementos",
                    help_text="Lista de elementos",
                    icon='list-ul'
                )
                )
            ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )

    class Meta:
        icon = 'link'