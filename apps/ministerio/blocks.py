
import os
from django.db import models
from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.core.blocks import (
    RichTextBlock, StructBlock, TextBlock, URLBlock, PageChooserBlock, StructValue, CharBlock, ListBlock
)
from wagtail.documents.blocks import DocumentChooserBlock


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class CorporateCultureObjetivesBlock(StructBlock):

    name = CharBlock(label="Título del Elemento", required=True,
                     help_text="Título que describe el elemento de objetivos de calidad")

    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text="Texto descriptivo del elemento de objetivos de calidad",
        features=['h2', 'h3', 'h4', 'bold',
                  'ul', 'ol', 'italic', 'link', 'hr'],
    )

    class Meta:
        """Metaclase"""
        icon = 'doc-full'
        value_class = LinkStructValue


class MinistrosBlock(StructBlock):
    title = CharBlock(label="Periodo de tiempo", required=True, blank=False,
                      help_text="Corresponde al periodo de tiempo que se presentara como título de la sección. Ejemplo: ‘Ministros de Minas y Energía entre 2010 – 2020’")
    ministros = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(label='Nombre', required=True, blank=False)),
                ('image', ImageChooserBlock(
                    label='Foto de perfil', required=True, blank=False)),
                ('alt_text', TextBlock(label='Texto alternativo foto de perfil', required=False, blank=False,
                                       help_text='Este atributo proporciona información alternativa para una imagen si un usuario,' +
                                       ' por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o' +
                                       ' si el usuario utiliza un lector de pantalla).')),
                ('period', TextBlock(label='Peridodo', required=True, blank=False,
                                     help_text="Periodo de tiempo en el cual estuvo activo el funcionario. Ejemplo: ‘7 de agosto de 2018 al 1 junio de 2020’")),
                ('paragraph_block', RichTextBlock(
                    icon="fa-paragraph",
                    label="Descripción:",
                    required=False,
                    template="blocks/paragraph_block.html",
                    help_text='Breve descripción del funcionario.',
                    features=['h2', 'h3', 'h4', 'bold',
                              'italic', 'link', 'hr'],
                ))
            ],
            icon='user',
            closed=True
        )
    )

    class Meta:
        template = 'ministerio/includes/ministros.html'
        closed = True
        icon = 'time'
        label = 'Ministros de la entidad'


class CurrentMinisterBlock(StructBlock):
    Nombre = CharBlock(label='Nombre', required=True, blank=False)
    image = ImageChooserBlock(
        label='Foto de perfil', required=True, blank=False)
    alt_text = TextBlock(label='Texto alternativo foto de perfil', required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario,' +
                         ' por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o' +
                         ' si el usuario utiliza un lector de pantalla).')
    period = TextBlock(label='Peridodo', required=True, blank=False,
                       help_text="Periodo de tiempo en el cual estuvo activo el funcionario. Ejemplo: ‘7 de agosto de 2018 al 1 junio de 2020’")
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción:",
        required=False,
        template="blocks/paragraph_block.html",
        help_text='Breve descripción del funcionario.',
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'],
    )

    class Meta:
        icon = 'user'
        value_class = LinkStructValue
        closed = True


class EntitiesBlock(StructBlock):
    name = CharBlock(label="Nombre de la entidad", required=True,
                     help_text='Texto que será mostrado al público.')
    image_color = ImageChooserBlock(label="Imagen a color", required=True,
                                    help_text="Imagen a color de la entidad")
    image_black = ImageChooserBlock(label="Imagen en blanco y negro", required=True,
                                    help_text="Imagen en blanco y negro")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')
    description = TextBlock(label="Descripción de la empresa", required=True,
                            help_text='Descripción de la empresa.')

    class Meta:
        icon = 'site'
        value_class = LinkStructValue
        closed = True


class IntroSectionBlock(StructBlock):
    title = CharBlock(label="Título del elemento", required=True,
                      help_text="Título del elemento.")
    icono = SvgChooserBlock(label="Icono del elemento", required=True,
                            help_text="Icono de la parte superior izquierda del elemento, solo se acepta imágenes en formato SVG.")
    description = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=True,
        help_text='Texto descriptivo.',
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'],
    )
    background_color = CharBlock(label="Color de fondo", required=True,
                                 help_text="Color de fondo para el elemento en formato hexadecimal. Ejemplo: #5A0C6D",
                                 max_length=7)
    text_color = CharBlock(label="Color de texto", required=True,
                                 help_text="Color de texto en formato hexadecimal. Ejemplo: #5A0C6D",
                                 max_length=7)

    class Meta:
        icon = 'doc-full'


class SubsectionsBlock(StructBlock):
    title = CharBlock(label="Título de la subsección", required=True,
                      help_text="Título de la subsección.")
    icono = SvgChooserBlock(label="Icono de la subsección", required=True,
                            help_text="Icono de la subsección, solo se acepta imágenes en formato SVG.")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        closed = True
        icon = 'link'
        value_class = LinkStructValue


class AcordionBlock(StructBlock):
    title = CharBlock(label="Título del elemento", required=True,
                      help_text="Título del elemento.")
    description = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=True,
        help_text='Texto descriptivo.',
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'],
    )

    class Meta:
        closed = True
        icon = 'doc-full'
        value_class = LinkStructValue


class FunctionaryListStructBlock(StructBlock):
    name = CharBlock(label="Nombre del funcionario", required=True,
                     help_text="Título del elemento.")
    position = CharBlock(label="Cargo del funcionario", required=True,
                         help_text="Título del elemento.")

    personal = ListBlock(
        StructBlock(
            [('group', CharBlock(label='Nombre del grupo', required=False, blank=False, help_text="Nombre del grupo.")),
             ('name', CharBlock(label='Nombre del funcionario',
              required=False, blank=False, help_text="Nombre del funcionario a cargo del grupo."))

             ],
            icon='user',
            closed=False,
            value_class=LinkStructValue
        ),
        required=True

    )

    class Meta:
        icon = 'user'


class ProcessBlock(StructBlock):

    name = CharBlock(label="Nombre del sistema", required=True,
                     help_text="Nombre del sistema al que se enlazará")

    image = ImageChooserBlock(label="Imagen del sistema", required=True,
                              help_text="Imagen del sistema")

    alt_text = CharBlock(label="Texto alternativo", required=False,
                         help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    description = RichTextBlock(label="Descripción del sistema", required=True,
                                help_text="Descripción del sistema")

    button_title = CharBlock(label="Título del boton", required=True,
                             help_text="Título del boton")

    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text="Link a página externa")

    class Meta:
        icon = 'site'
        value_class = LinkStructValue
        closed = True


class InformationManagementBlock(StructBlock):

    name = CharBlock(label="Título del Elemento", required=True,
                     help_text="Título que describe el elemento")

    svg_image = SvgChooserBlock(label="Imagen", required=True,
                                help_text="Imagen")

    alt_text = CharBlock(label="Texto alternativo", required=False,
                         help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        label="=Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text="Texto descriptivo del elemento",
        features=['h2', 'h3', 'h4', 'bold',
                  'ul', 'ol', 'italic', 'link', 'hr'],
    )

    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'doc-full'
        value_class = LinkStructValue

# Clase de acordeon creado para Gestion Talento Humano, seccion Hoja de vida Aspitantes
#necesita 4 columnas y texto introductorio y texto final
class AccordeonSheetsCVStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    intro =  RichTextBlock(label="Introduccion", required=False,
                           help_text="Introducción")
    
    piedp =  RichTextBlock(label="Pie de pagina", required=False,
                           help_text="Pie de pagina")
                           
    subitems = ListBlock(
        StructBlock(
            [
                ('aplicacion', CharBlock(label="Aplicacion", required=False,
                           help_text="Aplicacion")),
                ('name', CharBlock(label="Nombre", required=True,
                                   help_text="Nombre")),
                ('position', RichTextBlock(label="Descripción", required=True,
                                           help_text="Descripción")
                 ),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
                ('date', CharBlock(label="Fecha", required=True,
                                   help_text="Fecha formato dd/mm/aaaa")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )

class AdministrativeCareerTableStructBlock(StructBlock):
    
    titulo = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")

    subitems = ListBlock(
        
        StructBlock(
            [
                ('title', CharBlock(label="Título", required=True,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
                ('date', CharBlock(label="Fecha", required=True,
                                   help_text="Fecha formato dd/mm/aaaa")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos"

    )

    class Meta:
        icon = 'list-ul'
        closed = True
