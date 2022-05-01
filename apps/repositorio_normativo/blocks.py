from wagtail.core.blocks import (
    CharBlock,  StructBlock, URLBlock, PageChooserBlock, StructValue, ListBlock, RichTextBlock,TextBlock
)
from wagtailsvg.blocks import SvgChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


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


class SecondLinkStructBlock(StructBlock):
    link_text = CharBlock(label="Texto del link", required=True,
                          help_text="Texto del link que será mostrado al público", max_length=20)
    description = CharBlock(label="Descripción del elemento", required=True,
                            help_text="Descripción del elemento")
    icono = SvgChooserBlock(label="Icono del elemento", required=True,
                            help_text="Icono del link, solo se acepta imágenes en formato SVG.")
    page = PageChooserBlock(label="Link a página local:",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class FeaturedLinkStructBlock(StructBlock):

    page = PageChooserBlock(label="Link a página local:",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue

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


class NotiAdminTableStructBlock(StructBlock):
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")
    intro_1 = RichTextBlock(
        icon="fa-paragraph",
        label="Fecha de publicación",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_2 = RichTextBlock(
        icon="fa-paragraph",
        label="Nombre del Interesado",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_3 = RichTextBlock(
        icon="fa-paragraph",
        label="Procesos y/o Trámites",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_4 = RichTextBlock(
        icon="fa-paragraph",
        label="Acto Administrativo",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_5 = RichTextBlock(
        icon="fa-paragraph",
        label="Fecha Acto Administrativo",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )

class EdictosTableStructBlock(StructBlock):
    document = DocumentChooserBlock(label="Acto Administrativo", required=False,
                                    help_text="Seleccione un documento")
    intro_1 = RichTextBlock(
        icon="fa-paragraph",
        label="No. Proceso o fecha de publicación",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_2 = RichTextBlock(
        icon="fa-paragraph",
        label="Nombre del Interesado",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_3 = RichTextBlock(
        icon="fa-paragraph",
        label="Sección",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )
    intro_4 = RichTextBlock(
        icon="fa-paragraph",
        label="Fecha de emisión",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Texto descriptivo',
    )

class GrupoEjecucionTableStructBlock(StructBlock):

    subitems = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(label="Nombre", required=True,
                                    help_text="Nombre y apellido")),
                ('email', CharBlock(label="Correo", required=True,
                                    help_text="Correo")),
                ('phone', CharBlock(label="Celular", required=True,
                                    help_text="Celular")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )


class SubItemseStructBlock(StructBlock):
    
    description_block = RichTextBlock(label="Descripción", required=False,
                                help_text="Descripción")
    title = CharBlock(label="Título", required=True,
            help_text="Título del elemento")
    description = RichTextBlock(label="Descripción", required=False,
                                help_text="Descripción")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                            help_text="Título del elemento")),
                ('documents_block', ListBlock(
                    StructBlock(
                        [
                            ('subtitle', CharBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                            ('icono', SvgChooserBlock(label="Icono", required=True,
                                    help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                            ('description', TextBlock(label='Descripción del elemento', required=True, blank=False,
                                        help_text="Descripción del elemento")),
                            ('document', DocumentChooserBlock(label="Documento", required=False,
                                        help_text="Seleccione un documento")),
                            ('page', PageChooserBlock(
                            label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
                            ('external_url', URLBlock(
                            label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),
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
        icon = 'list-ul'
        closed = True


class TabsListStructBlockTable(StructBlock):
    
    title = CharBlock(label="Título", required=True,
                    help_text="Título del elemento")
    subitems = ListBlock(
        StructBlock(
            [
                ('decreto', RichTextBlock(label="N° Decreto", required=True,
                                    help_text="N° Decreto")),
                ('date', CharBlock(label="Fecha de expedicion", required=True,
                                    help_text="Fecha de expedicion")),
                ('epigrafe', CharBlock(label="Epígrafe", required=True,
                                    help_text="Epígrafe")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )
class TabsListStructBlockDocuments(StructBlock):

    title = CharBlock(label="Título", required=True,
                    help_text="Título del elemento")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', CharBlock(label="Título (Opcional)", required=False,
                    help_text="Texto del link que será mostrado al público")),
                ('description' ,RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")),
                ('icono', SvgChooserBlock(label="Icono del elemento (Opcional)", required=False,
                            help_text="Icono del link, solo se acepta imágenes en formato SVG.")),
                ('alt_text' , TextBlock(label="Texto alternativo", required=False, blank=False,
                        help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')),

                ('page' ,PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")),
                ('external_url', URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')),
                ('document' ,DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento,Si carga un documento la opción de link no se mostrará."))
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )
