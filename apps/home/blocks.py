# import os

# from ..common.blocks import LinkStructValue
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AudioChooserBlock
from wagtailsvg.blocks import SvgChooserBlock
from wagtail.core.blocks import (
    RichTextBlock, StructBlock, TextBlock, URLBlock, PageChooserBlock, StructValue, CharBlock,
    StreamBlock, ChoiceBlock,
)
class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url

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
    
class InterestPlacesStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del sitio de interes")

    image = ImageChooserBlock(label="Imagen", required=True, blank=False,
                              help_text='Imagen del sitio de interes')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).')

    page = PageChooserBlock(label="Link a página local", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este sitio con una página local.')

    external_url = URLBlock(label="Link a página externa", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este sitio con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')
    class Meta:
        """Metaclase"""
        icon = 'image'
        value_class = LinkStructValue
        closed = True





class InformationSystemsStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del sitio de interes")

    image = ImageChooserBlock(label="Imagen", required=True, blank=False,
                              help_text='Imagen del sitio de interes')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).')

    page = PageChooserBlock(label="Link a página local", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este sitio con una página local.')

    external_url = URLBlock(label="Link a página externa", required=False, blank=False,
                            help_text='Complete este campo si desea enlazar este sitio con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')
    class Meta:
        """Metaclase"""
        icon = 'image'
        value_class = LinkStructValue
        closed = True


class ImageGalleryBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True, label="Título")
    image = ImageChooserBlock(required=True, label="Imagen")

    class Meta:
        icon = 'image'

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


#     class Meta:
#         """Metaclase"""
#         icon = 'image'
#         value_class = LinkStructValue
#         closed = True
