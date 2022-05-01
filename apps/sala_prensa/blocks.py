from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailsvg.blocks import SvgChooserBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, URLBlock, StructValue, PageChooserBlock
)
from wagtailmedia.blocks import AudioChooserBlock


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class LinkBlock(StructBlock):

    heading_text = CharBlock(classname="title", required=True, label="Título")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        template = "news_blocks/embed_block.html"
        value_class = LinkStructValue
class VideoBlock(StructBlock):

    video_url = URLBlock(label="Link del video",
                            required=False, help_text='El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85')
    class Meta:
        icon = 'link'
        template = "news_blocks/video_block.html"
        value_class = LinkStructValue


class AudioBlock(StructBlock):

    heading_text = CharBlock(classname="title", required=True, label="Título")
    audio = AudioChooserBlock(label="Audio",
                              required=False)

    class Meta:
        icon = 'link'
        template = "news_blocks/audio_block.html"


class ImageGalleryBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True, label="Título")
    image = ImageChooserBlock(required=True, label="Imagen")

    class Meta:
        icon = 'image'


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    heading_text = CharBlock(classname="title", required=True, label="Título")
    image = ImageChooserBlock(required=True, label="Imagen")
    paragraph_block = RichTextBlock(
        label="Texto de la imagen", required=True
    )
    text = TextBlock(label="Cita", required=False)

    class Meta:
        icon = 'image'
        template = "news_blocks/image_block.html"


class ImageLinkBlock(StructBlock):

    heading_text = CharBlock(classname="title", required=False, label="Título")
    image = ImageChooserBlock(required=True, label="Imagen")
    paragraph_block = RichTextBlock(
        label="Texto de la imagen", required=False
    )
    text = TextBlock(label="Cita", required=False)
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'image'
        template = "news_blocks/image_link_block.html"
        value_class = LinkStructValue


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h5 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True, label="Título")
    size = ChoiceBlock(choices=[
        ('', 'Seleccione un tamaño de encabezado'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "news_blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    text = TextBlock(label="Cita",
                     help_text="No incluir comillas de inicio")
    attribute_name = CharBlock(
        blank=True, required=False, label='Ej. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "news_blocks/blockquote.html"


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    """ heading_block = HeadingBlock(label="Bloque de título") """
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="news_blocks/paragraph_block.html",
        label="Bloque de párrafo"
    )
    image_block = ImageBlock(label="Bloque de imagen")
    image_link_block = ImageLinkBlock(label="Bloque de imagen con link")
    block_quote = BlockQuote(label="Bloque de citación")
    embed_block = LinkBlock(label="Bloque de link")
    audio_block = AudioBlock(label="Bloque de audio")
    video_block = VideoBlock(label="Bloque de video")


class GalleryStreamBlock(StreamBlock):

    image_block = ImageGalleryBlock(label="Bloque de imagen")


class SocialNetworksBlock(StructBlock):
    title = CharBlock(label="Nombre", required=True,
                      help_text="Nombre de la red social")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono de la red social, solo imágenes en formato SVG.")
    text = TextBlock(label="Codigo Embebido",
                     help_text="Fragmento de código correspondiente al iframe o timeline de la red social",
                     max_length=4000,
                     required=False,
                     null=True,
                     )
    external_url = URLBlock(label="Link a la red social",
                            required=False,
                            null=True,
                            help_text='URL de acceso a la red social')

    class Meta:
        icon = 'link'
