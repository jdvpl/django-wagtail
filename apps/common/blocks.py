
import os

from django.db import models
from django.forms.utils import flatatt
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from django.utils.html import format_html, format_html_join
from wagtail.core.blocks import (
    StructBlock, TextBlock, URLBlock, PageChooserBlock, StructValue,
    CharBlock, RichTextBlock, DateBlock, EmailBlock, ListBlock, StreamBlock, ChoiceBlock
)

from wagtail.documents.blocks import DocumentChooserBlock
from wagtailsvg.blocks import SvgChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class LinkStructValue(StructValue):

    def url(self):
        """Permite obtener la url del enlace.
        @return URL
        """
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class HeaderStructBlock(StructBlock):
    """Clase que representa el contenido del fracmento de 
    header. 

    ...

    Methods
    -------
    None
    """

    # Define el campo de caption
    caption = CharBlock(label="Texto del link", required=True, blank=False,
                        help_text="Texto del link que será mostrado al público")

    # Define el campo de enlace interno
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")

    # Define el campo de enlace externo
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local")

    class Meta:
        """Metaclase"""
        icon = 'link'
        value_class = LinkStructValue
        closed = True


class SocialNetworkBlock(StructBlock):
    """Clase que representa el contenido del fracmento de 
    header. 

    ...

    Methods
    -------
    None
    """

    # Define el campo de nombre de la red social
    name = CharBlock(label="Texto del link", required=True,
                     help_text="Texto del link que será mostrado al público")

    # Define el campo del icono de la red social
    image = ImageChooserBlock(label="Icono de la red social", required=True,
                              help_text="Icono")

    # Define el campo del enlace externo
    external_url = URLBlock(label="Link hacia la red social", required=True,
                            help_text="Enlace hacia la página")

    class Meta:
        """Metaclase"""
        icon = 'group'
        value_class = LinkStructValue
        closed = True


class SectorCompanyBlock(StructBlock):
    """Clase que representa el contenido del fracmento de 
    entidades adscritas. 

    ...

    Methods
    -------
    None
    """

    # Define el campo de nombre de la entidad
    name = CharBlock(label="Nombre de la entidad", required=True,
                     help_text="Nombre de la entidad que será mostrado al público")

    # Define el campo de imagen de la entidad
    image = ImageChooserBlock(label="Logotipo de la entidad", required=True,
                              help_text="Logotipo de la entidad")

    # Define el campo de enlace interno
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")

    # Define el campo de externo
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local")

    # Define el campo de descripcion
    description = TextBlock(label="Descripción de la entidad", required=True,
                            help_text="Descripción de la entidad")

    class Meta:
        """Metaclase"""
        icon = 'site'
        value_class = LinkStructValue
        closed = True


class RelatedCompanyBlock(StructBlock):
    """Clase que representa el contenido del fracmento de 
    entidades vinculadas. 

    ...

    Methods
    -------
    None
    """

    # Define el campo de nombre de la entidad
    name = CharBlock(label="Nombre de la empresa", required=True,
                     help_text="Nombre de la entidad que será mostrado al público")

    # Define el campo de imagen de la entidad
    image = ImageChooserBlock(label="Logotipo de la empresa", required=True,
                              help_text="Logotipo de la empresa")

    # Define el campo de enlace interno
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")

    # Define el campo de externo
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local")

    # Define el campo de nombre del representante legal
    represent = CharBlock(label="Nombre del representante legal de la empresa", required=True,
                          help_text="Digite el nombre completo del representante legal")

    # Define el campo de mail
    mail = EmailBlock(label="Correo Corporativo", required=True,
                      help_text="Correo Corporativo")

    class Meta:
        """Metaclase"""
        icon = 'site'
        value_class = LinkStructValue
        closed = True


class LinksStructBlock(StructBlock):
    """Clase que representa el contenido del fragmento de enlaces.

    ...

    Methods
    -------
    None
    """

    # Define el campo de caption
    caption = CharBlock(label="Texto del link", required=True, blank=False,
                        help_text="Texto del link que será mostrado al público")

    # Define el campo de enlace interno
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")

    # Define el campo de enlace externo
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local")

    class Meta:
        """Metaclase"""
        icon = 'link'
        value_class = LinkStructValue
        closed = True


class NewsMissionaryBlock(StructBlock):
    """Clase que representa el contenido del fragmento de
    de Misional.

    ...

    Methods
    -------
    None
    """
    # Define el campo del título
    title = CharBlock(label="Titilo", required=True,
                      help_text="Título")
    # Define el campo de descripción
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")
    # Define el campo de enlace externo
    external_url = URLBlock(label="URL",
                            required=False, help_text="URL")

    class Meta:
        icon = 'site'
        value_class = LinkStructValue
        closed = True


class ElementsListStructBlock(StructBlock):
    """Class that provides the structure for icon sections
    ...
    Methods
    -------
    None
    """
    title = CharBlock(label="Título", required=False,
                      help_text="Título del elemento que será mostrado al publico")
    icono = SvgChooserBlock(label="Icono", required=False,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    image = ImageChooserBlock(label="Imagen", required=False, blank=False,
                              help_text='Icono del elemento que será mostrado al publico, solo se mostrara la imagen si no se ha seleccionado un icono SVG')

    description = TextBlock(label="Descripción", required=False,
                            help_text="Corta descripción del elemento")
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Complete este campo si el elemento debe presentar un documento como enlace directo")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')
    subitems = ListBlock(
        StructBlock(
            [('name', CharBlock(label='Subitem', required=True, blank=False, help_text="Subitems que serán presentados como un listado en la ventana modal ")),
             ('page', PageChooserBlock(
                 label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
             ('external_url', URLBlock(
                 label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),
             ('document', DocumentChooserBlock(label="Documento", required=False,
                                               help_text="Complete este campo si el elemento debe presentar un documento como enlace directo"))
             ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos que se presentaran en la ventana modal, si se agregan ítems en esta sección, no se presentara información de documento o enlace a otra página"

    )

    class Meta:
        icon = 'list-ol'
        value_class = LinkStructValue


class DeclarationStructBlock(StructBlock):
    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    managers_subitems = ListBlock(
        StructBlock(
            [('name', CharBlock(label='Título ', required=True, blank=False, help_text="Título del documento")),
             ('document', DocumentChooserBlock(label="Documento", required=False,
                                               help_text="Seleccione un documento"))
             ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=False,
        blank=True,
        label="Lista de documentos directivos",
        help_text="Documentos que serán presentados en formato de lista"
    )
    functionary_subitems = ListBlock(
        StructBlock(
            [('name', CharBlock(label='Título ', required=True, blank=False, help_text="Título del documento")),
             ('document', DocumentChooserBlock(label="Documento", required=False,
                                               help_text="Seleccione un documento"))
             ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=False,
        blank=True,
        label="Lista de documentos funcionarios",
        help_text="Documentos que serán presentados en formato de lista"
    )

    class Meta:
        icon = 'list-ol'


class IconDocumentListTabStructBlock(StructBlock):
    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    subitems = ListBlock(
        StructBlock(
            [('name', CharBlock(label='Título ', required=True, blank=False, help_text="Título del documento")),
             ('document', DocumentChooserBlock(label="Documento", required=False,
                                               help_text="Seleccione un documento"))
             ],
            icon='link',
            closed=False,
            value_class=LinkStructValue
        ),
        required=False,
        blank=True,
        label="Lista de documentos",
        help_text="Documentos que serán presentados en formato de lista"
    )

    class Meta:
        icon = 'list-ol'


class TabsListStructBlock(StructBlock):
    """Class that provides the structure for tabs sections
    ...
    Methods
    -------
    None
    """
    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    description = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        help_text="Descripción del elemento",
        required=True,
    )
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')

    class Meta:
        icon = 'cogs'
        value_class = LinkStructValue


class BriefcaseStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del portafolio, políticas y/o protocolos de servicio ")

    main_description = TextBlock(label="Descripción principal ", required=True,
                                 help_text="Descripción principal del portafolio, políticas y/o protocolos de servicio ")
    second_description = RichTextBlock(
                          icon="fa-paragraph",
                          label="Descripción secundaria",
                          help_text="Descripción complementaria del portafolio, políticas y/o protocolos de servicio",
                          required=True,
                          )
 
    icono = SvgChooserBlock(label="Icono", required=False,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")

    image = ImageChooserBlock(label="Imagen", required=False, blank=False,
                              help_text='Tamaño recomendado de la imagen 200px X 200px pixeles. Icono del elemento que será mostrado al publico, solo se mostrara la imagen si no se ha seleccionado un icono SVG')

    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class SimpleBriefcaseStructBlock1(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del elemento")

    main_description = RichTextBlock(label="Descripción", required=False,
                                     help_text="Si desea que se muestre el icono NO ! complete este campo, dejelo vacio.")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    # external_url = URLBlock(label="Link a página externa",
    #                         required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')
    description = RichTextBlock(label="Descripción", required=False,
                                help_text="Descripción")
    icono = SvgChooserBlock(label="Icono", required=False,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")

    

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class SimpleBriefcaseStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del elemento")

    main_description = RichTextBlock(label="Descripción", required=True,
                                     help_text="Descripción")
     

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class SimpleBlockIconStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")

    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    align = ChoiceBlock(
        label='Alinear icono a la izquierda',
        required=False,
        help_text="Si esta opción esta activa, la icono se alineara a la izquierda, por defecto se alineará a la derecha.",
        choices=[
            ('true', 'Izquierda'),
        ],
    )
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class SimpleIconBriefcaseStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Título del portafolio, políticas y/o protocolos de servicio ")

    main_description = RichTextBlock(label="Descripción", required=True,
                                     help_text="Descripción")

    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class DocumentBriefcaseStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
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


class DocumentListStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
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


class AccordeonRichTextStructBlock(StructBlock):

    title = CharBlock(label="Título", required=False,
                      help_text="Título del elemento (Opcional)")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', CharBlock(label="Título", required=True,
                                    help_text="Título del elemento")),
                ('description', RichTextBlock(label="Descripción", required=True,
                                              help_text="Descripción")
                 )
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


class AccordeonDocumentStructBlock(StructBlock):

    title = CharBlock(label="Título", required=False,
                      help_text="Título del elemento (Opcional)")

    subitems = ListBlock(
        StructBlock(
            [
                # ('title', CharBlock(label="Título", required=True,
                #                     help_text="Título del elemento")),
                # ('description', RichTextBlock(label="Descripción", required=True,
                #                               help_text="Descripción")
                #  )

                #  ('title', CharBlock(label='Título del elemento', required=True, blank=False,
                #                     help_text="Título del elemento")),
                ('icono', SvgChooserBlock(label="Icono", required=True,
                                          help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                ('description', TextBlock(label='Descripción del elemento', required=True, blank=False,
                                          help_text="Descripción del elemento")),
                ('page', PageChooserBlock(
                 label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
                ('external_url', URLBlock(
                 label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),

                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=True,
                                                  help_text="Seleccione un documento")),
                # ('starred', ChoiceBlock(
                #     label='Item destacado',
                #     required=False,
                #     help_text="Seleccione Destacado si el archivo debe resaltarse en la lista de elementos",
                #     choices=[
                #         ('true', 'Destacado'),
                #     ],
                # )),
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


class AccordeonIconStructBlock(StructBlock):

    title = CharBlock(label="Título", required=False,
                      help_text="Título del elemento (Opcional)")

    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")

    subitems = ListBlock(
        StructBlock(
            [
                # ('title', CharBlock(label="Título", required=True,
                #                     help_text="Título del elemento")),
                # ('description', RichTextBlock(label="Descripción", required=True,
                #                               help_text="Descripción")
                #  )

                ('title', CharBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),

                (('documents', ListBlock(
                    StructBlock(
                        [
                                        ('icono', SvgChooserBlock(label="Icono", required=True,
                                                                  help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                                        ('description', RichTextBlock(label="Descripción", required=True,
                                                                      help_text="Descripción")),
                        ],
                    ),
                    required=False,
                    blank=True,
                    label="Lista",
                    help_text="Lista",
                    icon='list-ul'
                ))),

                # ('description', TextBlock(label='Descripción del elemento', required=True, blank=False,
                #                           help_text="Descripción del elemento")),
                # ('page', PageChooserBlock(
                #  label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
                # ('external_url', URLBlock(
                #  label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),

                # ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                #                     help_text="Título del elemento")),
                # ('document', DocumentChooserBlock(label="Documento", required=True,
                #                                   help_text="Seleccione un documento")),
                # ('starred', ChoiceBlock(
                #     label='Item destacado',
                #     required=False,
                #     help_text="Seleccione Destacado si el archivo debe resaltarse en la lista de elementos",
                #     choices=[
                #         ('true', 'Destacado'),
                #     ],
                # )),
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


class DocumentSimpleListStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")

    class Meta:
        icon = 'list-ul'
        closed = True


class IconDocumentBriefcaseStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    icono = SvgChooserBlock(label="Icono", required=True,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=True,
                                                  help_text="Seleccione un documento")),
                ('starred', ChoiceBlock(
                    label='Item destacado',
                    required=False,
                    help_text="Seleccione Destacado si el archivo debe resaltarse en la lista de elementos",
                    choices=[
                        ('true', 'Destacado'),
                    ],
                )),
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


class IconDocumentListStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('description', TextBlock(label="Descripción", required=True,
                                          help_text="Descripción del elemento")),
                ('icono', SvgChooserBlock(label="Icono", required=True,
                                          help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                ('document', DocumentChooserBlock(label="Documento", required=True,
                                                  help_text="Seleccione un documento")),

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


class IconDocumentMenuStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('icono', SvgChooserBlock(label="Icono", required=True,
                                          help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                ('document', DocumentChooserBlock(label="Documento", required=True,
                                                  help_text="Seleccione un documento")),
                ('description', TextBlock(label="Descripción", required=False,
                                          help_text="Descripción del elemento")),
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


class DocumentRetentionTableStructBlock(StructBlock):

    section_code = CharBlock(label="Código Sección", required=False,
                             help_text="Código Sección")
    section = TextBlock(label="Sección ", required=False,
                        help_text="Sección")
    section_document = DocumentChooserBlock(label="Documento sección", required=False,
                                            help_text="Seleccione un documento para la sección")
    sub_section_code = CharBlock(label="Código Subsección", required=False,
                                 help_text="Código Subsección")
    subsection_description = TextBlock(label="Subsección", required=False,
                                       help_text="Subsección")
    subsection_document = DocumentChooserBlock(label="Documento subsección", required=False,
                                               help_text="Seleccione un documento para la subsección")
    starred = ChoiceBlock(
        label='Item destacado',
        required=False,
        help_text="Seleccione Destacado si el elemento debe resaltarse en la lista de elementos",
        choices=[
            ('true', 'Destacado'),
        ],
    )

    class Meta:
        icon = 'list-ul'
        closed = True


class SubitemsBriefcaseStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento")
    description = RichTextBlock(label="Descripción", required=False,
                                help_text="Descripción")

    subitems = ListBlock(
        StructBlock(
            [
                ('title', CharBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('icono', SvgChooserBlock(label="Icono", required=True,
                                          help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")),
                ('description', TextBlock(label='Descripción del elemento', required=True, blank=False,
                                          help_text="Descripción del elemento")),
                ('page', PageChooserBlock(
                    label='Link a página local', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página local.')),
                ('external_url', URLBlock(
                    label='Link a página externa', required=False, blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.')),
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


class SecondLinkDocuemntStructBlock(StructBlock):
    title = CharBlock(label="Título", required=False,
                      help_text="Texto del link que será mostrado al público")
    description = RichTextBlock(label="Descripción", required=False,
                                help_text="Descripción")
    icono = SvgChooserBlock(label="Icono del elemento", required=False,
                            help_text="Icono del link, solo se acepta imágenes en formato SVG.")
    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")


class SecondLinkStructBlock(StructBlock):
    title = CharBlock(label="Título (Opcional)", required=False,
                      help_text="Texto del link que será mostrado al público")
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")
    icono = SvgChooserBlock(label="Icono del elemento (Opcional)", required=False,
                            help_text="Icono del link, solo se acepta imágenes en formato SVG.")
    alt_text = TextBlock(label="Texto alternativo", required=False, blank=False,
                         help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)')
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento,Si carga un documento la opción de link no se mostrará.")

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class TabTableStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
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


class AccodionRichTextStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    subitems = ListBlock(
        StructBlock(
            [
                ('description', RichTextBlock(
                    icon="fa-paragraph",
                    label="Descripción",
                    required=False,
                    help_text='Breve descripción',
                ))
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos que se presentaran"

    )


class AlienationTabStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('description', RichTextBlock(
                    icon="fa-paragraph",
                    label="Descripción:",
                    required=False,
                    template="blocks/paragraph_block.html",
                    help_text='Breve descripción',
                ))
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos que se presentaran en formato tabla dentro de una pestaña"

    )


class BudgetExecutionTabStructBlock(StructBlock):

    title = CharBlock(label="Título", required=True,
                      help_text="Título del elemento que será mostrado al publico")
    description = RichTextBlock(label="Descripción", required=True,
                                help_text="Descripción")

    report_title = CharBlock(label="Titulo Subsección", required=True,
                             help_text="Título del elemento que será mostrado al publico")
    report_subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos - Informes de Gestión Financiera",
        help_text="Lista de elementos que se presentaran en formato tabla dentro de una pestaña (Informes)"
    )

    expenses_title = CharBlock(label="Titulo Subsección", required=True,
                               help_text="Título del elemento que será mostrado al publico")
    expenses_subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos - Gastos",
        help_text="Lista de elementos que se presentaran en formato tabla dentro de una pestaña (Gastos)"
    )

    reservation_title = CharBlock(label="Titulo Subsección", required=True,
                                  help_text="Título del elemento que será mostrado al publico")
    reservation_subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('document', DocumentChooserBlock(label="Documento", required=False,
                                                  help_text="Seleccione un documento")),
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos - Reserva presupuestal",
        help_text="Lista de elementos que se presentaran en formato tabla dentro de una pestaña (Reserva)"
    )


class CorporateCultureBlock(StructBlock):

    name = CharBlock(label="Título del Elemento", required=True,
                     help_text="Título que describe el elemento")

    image = ImageChooserBlock(label="Imagen", required=True,
                              help_text="Imagen que representa el elemento")

    alt_text = CharBlock(label="Texto alternativo", required=False,
                         help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        label="Descripción",
        required=False,
        template="blocks/paragraph_block.html",
        help_text="Texto descriptivo del elemento",
        features=['h2', 'h3', 'h4', 'bold',
                  'ul', 'ol', 'italic', 'link', 'hr'],
    )

    class Meta:
        """Metaclase"""
        icon = 'doc-full'
        value_class = LinkStructValue


class CardsHomePageBlock(StructBlock):

    name = CharBlock(label="Título del Elemento", required=True,
                     help_text="Título que describe el elemento")

    image = ImageChooserBlock(label="Imagen", required=True,
                              help_text="Imagen que representa el elemento")

    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    alt_text = CharBlock(label="Texto alternativo", required=False,
                         help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    description = TextBlock(label="Descripción", required=False,
                            help_text="Descripción")

    class Meta:
        """Metaclase"""
        icon = 'doc-full'
        value_class = LinkStructValue


class CardsStructBlock(StructBlock):

    name = CharBlock(label="Título del Elemento", required=True,
                     help_text="Título que describe el elemento")

    image = ImageChooserBlock(label="Imagen", required=True,
                              help_text="Imagen que representa el elemento")

    alt_text = CharBlock(label="Texto alternativo", required=False,
                         help_text="Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)")

    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class SimpleDocumentCardSliderStructBlock(StructBlock):
    title = CharBlock(label="Titulo", required=True,
                      help_text="Titulo del mecanismo de participación")
    description = TextBlock(label="Descripción del elemento", required=True,
                            help_text="Descripción del mecanismo de participación")
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class LinkDocumentCardSliderStructBlock(StructBlock):
    title = CharBlock(label="Titulo", required=True,
                      help_text="Titulo del mecanismo de participación")
    description = TextBlock(label="Descripción del elemento", required=True,
                            help_text="Descripción del mecanismo de participación")
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Seleccione un documento")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local.")
    external_url = URLBlock(label="Link a página externa:",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa.' +
                            'Si este campo está completo, no se tendrá en cuenta el link a página local.')

    class Meta:
        icon = 'link'
        value_class = LinkStructValue


class BriefcaseMenuAccodeonStructBlock(StructBlock):

    caption = CharBlock(label="Título", required=True,
                        help_text="Planes y Programas")
    subitems = ListBlock(
        StructBlock(
            [
                ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                    help_text="Título del elemento")),
                ('subtitle', TextBlock(label='Subtítulo del elemento', required=True, blank=False,
                                       help_text="Subtítulo del elemento")),
                ('page', PageChooserBlock(label="Link a página local",
                                          required=False, help_text="Link a página local")),

                ('documents_block', ListBlock(
                    StructBlock(
                        [
                            ('title', TextBlock(label='Título del elemento', required=True, blank=False,
                                                help_text="Título del elemento")),
                            (('documents', ListBlock(
                                StructBlock(
                                    [
                                        ('title', TextBlock(label='Título del documento', required=True, blank=False,
                                                            help_text="Título del documento")),
                                        ('document', DocumentChooserBlock(label="Documento", required=True,
                                                                          help_text="Seleccione un documento")),
                                    ],
                                ),
                                required=False,
                                blank=True,
                                label="Lista de documentos",
                                help_text="Lista de documentos",
                                icon='list-ul'
                            ))),
                        ],
                    ),
                    required=False,
                    blank=True,
                    label="Lista de elementos",
                    help_text="Lista de elementos",
                    icon='list-ul'
                ))
            ],
        ),
        required=False,
        blank=True,
        label="Lista de elementos",
        help_text="Lista de elementos",
        icon='list-ul',
        value_class=LinkStructValue
    )

    class Meta:
        icon = 'list-ul'
        value_class = LinkStructValue
        closed = True


class ElementsListStructMenuBlock(StructBlock):
    """Class that provides the structure for icon sections
    ...
    Methods
    -------
    None
    """
    title = CharBlock(label="Título", required=False,
                      help_text="Título del elemento que será mostrado al publico")
    icono = SvgChooserBlock(label="Icono", required=False,
                            help_text="Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.")
    image = ImageChooserBlock(label="Imagen", required=False, blank=False,
                              help_text='Icono del elemento que será mostrado al publico, solo se mostrara la imagen si no se ha seleccionado un icono SVG')
    title_button = CharBlock(label="Título Boton", required=False,
                      help_text="Título del boton para descargar")

    description = TextBlock(label="Descripción", required=False,
                            help_text="Corta descripción del elemento")
    document = DocumentChooserBlock(label="Documento", required=False,
                                    help_text="Complete este campo si el elemento debe presentar un documento como enlace directo")
    page = PageChooserBlock(label="Link a página local",
                            required=False, help_text="Complete este campo si desea enlazar este elemento con una página local")
    external_url = URLBlock(label="Link a página externa",
                            required=False, help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local')


    class Meta:
        icon = 'list-ol'
        value_class = LinkStructValue