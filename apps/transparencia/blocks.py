from wagtail.core.blocks import (
    CharBlock,  StructBlock, URLBlock, PageChooserBlock, StructValue, ListBlock, RichTextBlock
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
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")
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
