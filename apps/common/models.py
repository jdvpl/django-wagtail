#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""Script que define el modulo de modelos comunes a la 
modulos de aplicacion - wagtail models.py

$Id: models.py,v 1.0 2021/05/07 8:00:30 MME

"""

#
# @autor Equipo Portal Web
# last revision: 2021-05-05

# =========================================================
# IMPORTA LOS RECURSOS
# =========================================================

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    StreamFieldPanel,
    FieldPanel
)

import os
from django.db import models
from wagtail.core.models import Page
from wagtailseo.models import SeoMixin
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from .blocks import HeaderStructBlock, SocialNetworkBlock, SectorCompanyBlock, RelatedCompanyBlock
from wagtail.search import index
from modelcluster.models import ClusterableModel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField


# =========================================================
# DEFINE LOS FRACMENTOS
# =========================================================

@register_snippet
class HeaderBlock(models.Model):
    """Clase que representa el fracmento del encabezado de
    las paginas del aplicaivo. 

    ...

    Methods
    -------
    __str__(self)
        Parser del objeto a cadena de caracteres.
    """

    # Define los enlaces del encabezado
    links = StreamField(
        [('enlaces', HeaderStructBlock())], blank=True, verbose_name="Enlaces de gobierno")

    # Define los panels de administracion de las listas
    panels = [
        StreamFieldPanel('links'),
    ]

    def __str__(self):
        """Parser del objeto a cadena de caracteres."""
        # Retorna el nombre del fracmento
        return "Header"

    class Meta:
        """Metaclase"""
        verbose_name_plural = 'Header'


@register_snippet
class FooterBlock(models.Model):
    """Clase que representa el fracmento del pie de las
    paginas del aplicaivo. 

    ...

    Methods
    -------
    __str__(self)
        Parser del objeto a cadena de caracteres.
    """

    # Define el campo de infomacion general
    general_info = RichTextField(verbose_name="Información General",
                                 help_text="Información de la institución",
                                 features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'])

    # Define el campo de links de redes sociales
    social_networks = StreamField(
        [('Redes_Sociales', SocialNetworkBlock())], blank=True, verbose_name="Redes Sociales")

    # Define el campo informacion de contacto
    contact_info = RichTextField(verbose_name="Información de contacto",
                                 help_text="=Información de contacto",
                                 features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'])

    # Define los paneles de captura del gestor
    panels = [
        FieldPanel('general_info'),
        MultiFieldPanel([
            StreamFieldPanel('social_networks'),
        ], heading="Redes Sociales", classname="collapsible"),
        FieldPanel('contact_info'),
    ]

    def __str__(self):
        """Parser del objeto a cadena de caracteres."""
        # Retorna el nombre del fracmento
        return "Footer"

    class Meta:
        """Metaclase"""
        verbose_name_plural = 'Footer'


@register_snippet
class AffiliatedEntitiesBlock(models.Model):
    """Clase que representa el fracmento de Entidades 
    Adscritas. 

    ...

    Methods
    -------
    __str__(self)
        Parser del objeto a cadena de caracteres.
    """

    # Define el campo para las entidades adscritas
    sector_company = StreamField(
        [('Entidad_Adscrita', SectorCompanyBlock())], blank=True, verbose_name="Entidad Adscrita")

    # Define los panels de administracion de las listas
    panels = [
        MultiFieldPanel([
            StreamFieldPanel('sector_company'),
        ], heading="Entidades Adscritas", classname="collapsible",
            help_text="Entidades adscritas"),
    ]

    def __str__(self):
        """Parser del objeto a cadena de caracteres."""
        # Retorna el nombre del fracmento
        return "Entidades Adscritas"

    class Meta:
        """Metaclase"""
        verbose_name_plural = 'Entidades Adscritas'


@register_snippet
class RelatedEntitiesBlock(models.Model):
    """Clase que representa el fracmento de Entidades 
    Vinculadas. 

    ...

    Methods
    -------
    __str__(self)
        Parser del objeto a cadena de caracteres.
    """

    # Define el campo para las entidades adscritas
    sector_company = StreamField(
        [('Entidad_Vinculada', RelatedCompanyBlock())], blank=True, verbose_name="Entidad Vinculadas")

    # Define los panels de administracion de las listas
    panels = [
        MultiFieldPanel([
            StreamFieldPanel('sector_company'),
        ], heading="Entidades Vinculadas", classname="collapsible",
            help_text="Entidades adscritas"),
    ]

    def __str__(self):
        """Parser del objeto a cadena de caracteres."""
        # Retorna el nombre del fracmento
        return "Entidades Vinculadas"

    class Meta:
        """Metaclase"""
        verbose_name_plural = 'Entidades Vinculadas'


@register_snippet
class InfoEntitiesBlock(models.Model):
    """Clase que representa el fracmento de Sistemas de 
    informacion. 

    ...

    Methods
    -------
    __str__(self)
        Parser del objeto a cadena de caracteres.
    """

    # Define el campo para las entidades adscritas
    inf_entity = StreamField(
        [('Sistema_Informacion', SectorCompanyBlock())], blank=True, verbose_name="Define los sistemas de informacion")

    # Define los panels de administracion de las listas
    panels = [
        MultiFieldPanel([
            StreamFieldPanel('inf_entity'),
        ], heading="Entidades Adscritas", classname="collapsible",
            help_text="Entidades adscritas"),
    ]

    def __str__(self):
        """Parser del objeto a cadena de caracteres."""
        # Retorna el nombre del fracmento
        return "Sistemas de Información"

    class Meta:
        """Metaclase"""
        verbose_name_plural = 'Sistemas de Información'


@register_snippet
class Autor(index.Indexed, ClusterableModel):

    organization_title = models.CharField(
        "Nombre de la Organización", max_length=254, null=False, blank=False, default='MINENERGÍA')

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('organization_title'),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('organization_title'),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ''

    def __str__(self):
        return '{}'.format(self.organization_title)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


@register_snippet
class Sector(index.Indexed, ClusterableModel):

    sector_title = models.CharField(
        "Nombre del sector", max_length=254, null=False, blank=False)

    panels = [
        FieldPanel('sector_title'),
    ]

    search_fields = [
        index.SearchField('sector_title'),
    ]

    api_fields = [
        APIField('sector'),
    ]

    def __str__(self):
        return '{}'.format(self.sector_title)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'


@register_snippet
class Year(index.Indexed, ClusterableModel):

    year = models.IntegerField(
        "Año concepto",  null=False, blank=False)

    panels = [
        FieldPanel('year'),
    ]

    search_fields = [
        index.SearchField('year'),
    ]

    api_fields = [
        APIField('year'),
    ]

    def __str__(self):
        return '{}'.format(self.year)

    class Meta:
        verbose_name = 'Año'
        verbose_name_plural = 'Años'
