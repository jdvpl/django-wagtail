from wagtail.core.models import Page
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from wagtail.core.blocks import (
    URLBlock
)

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailmedia.edit_handlers import MediaChooserPanel
from rest_framework.fields import Field

from .blocks import BaseStreamBlock, GalleryStreamBlock, SocialNetworksBlock
from ..common.models import Autor, Sector


class InfografiaAutorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaPage', related_name='infografia_autor_relationship', on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        Autor, related_name='autor_infografia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('autor')
    ]

    api_fields = [
        APIField('autor'),
    ]


class InfografiaSectorRelationship(Orderable, models.Model):

    page = ParentalKey(
        'InfografiaPage', related_name='infografia_sector_relationship', on_delete=models.CASCADE
    )
    sector = models.ForeignKey(
        Sector, related_name='sector_infografia_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sector')
    ]

    api_fields = [
        APIField('sector'),
    ]


class InfografiaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'InfografiaPage', related_name='tagged_items', on_delete=models.CASCADE)


class InfografiaPage(Page):
    introduction = models.TextField(
        help_text='Texto que describe la infografía',
        blank=False,
        verbose_name="Descripción",)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Infografía",
        help_text='Solo modo cuadrado; ancho horizontal entre 1080px y 1080px.'
    )

    city = models.CharField(blank=False, max_length=255, verbose_name="Ciudad")
    tags = ClusterTaggableManager(through=InfografiaPageTag, blank=False)
    date_published = models.DateField(
        "Fecha de publicación", blank=False, null=True
    )

    content_panels = Page.content_panels + [

        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('date_published'),
        FieldPanel('city', classname="full"),
        InlinePanel(
            'infografia_autor_relationship', label="Autor(es)",
            panels=None, min_num=1),
        InlinePanel(
            'infografia_sector_relationship', label="Sector(es)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    def authors(self):
        authors = [
            n.autor for n in self.infografia_autor_relationship.all()
        ]

        return authors

    def sectors(self):
        sectors = [
            n.sector for n in self.infografia_sector_relationship.all()
        ]

        return sectors

    @property
    def sectors_list(self):
        return [
            str(child.sector) for child in self.infografia_sector_relationship.all()
        ]

    @property
    def author_list(self):
        return [
            str(child.autor) for child in self.infografia_autor_relationship.all()
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

    parent_page_types = ['InfografiaIndexPage']

    subpage_types = []

    api_fields = [
        APIField('date_published'),
        APIField('tags'),
        APIField('sectors_list'),
        APIField('introduction'),
        APIField('city'),
        APIField('author_list'),
        APIField('image_data', serializer=ImageRenditionField(
            'fill-350x350-c50', source='image')),

    ]


class InfografiaIndexPage(RoutablePageMixin, Page):

    subpage_types = ['InfografiaPage']

    def children(self):
        return InfografiaPage.objects.descendant_of(self).live().order_by('-date_published')

    def get_context(self, request):
        context = super(InfografiaIndexPage, self).get_context(request)
        context['posts'] = InfografiaPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self, tag=None):
        posts = InfografiaPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags




# class prensaPage(Page):

#     subpage_types = ['InfografiaIndexPage', 'GaleriaIndexPage', 'NoticiaIndexPage',
#                      'VideosIndexPage', 'AudioIndexPage', 'DocumentoIndexPage', 'EventoIndexPage']
#     news_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     news_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de noticias',
#         verbose_name='Índice de noticias'
#     )

#     news_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     gallery_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     gallery_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de galeria',
#         verbose_name='Índice de galeria'
#     )

#     gallery_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     infographics_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     infographics_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de infografías',
#         verbose_name='Índice de infografías'
#     )

#     infographics_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     videos_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     videos_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de videos',
#         verbose_name='Índice de videos'
#     )

#     videos_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     audios_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     audios_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de videos',
#         verbose_name='Índice de audios'
#     )

#     audios_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     documents_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     documents_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de documentos',
#         verbose_name='Índice de documentos'
#     )

#     documents_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     events_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     events_list = models.ForeignKey(
#         'wagtailcore.Page',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Seleccione la página del índice de eventos',
#         verbose_name='Índice de eventos'
#     )

#     events_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     podcast_list_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     podcast_iframe_url = models.URLField(
#         verbose_name="URL iframe Podcats",
#         blank=True,
#         max_length=2000,
#         help_text='URL iframe Podcats'
#     )

#     podcast_url = models.URLField(
#         verbose_name="Link a página de podcast",
#         blank=True,
#         help_text='Link a página de podcast'
#     )

#     podcats_button_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=20,
#         help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres',
#         verbose_name='Título botón más información'
#     )

#     social_networks_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=255,
#         help_text='Título que será presentado al publico',
#         verbose_name='Título de la sección'
#     )

#     social_networks = StreamField(
#         [('Red', SocialNetworksBlock())], blank=True, verbose_name="Redes Sociales")

#     content_panels = Page.content_panels + [
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('news_list_title'), PageChooserPanel('news_list'), FieldPanel('news_button_title'), ]),
#         ], heading="Noticias", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('gallery_list_title'), PageChooserPanel('gallery_list'), FieldPanel('gallery_button_title'), ]),
#         ], heading="Galeria", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('infographics_list_title'), PageChooserPanel('infographics_list'), FieldPanel('infographics_button_title'), ]),
#         ], heading="Infografías", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('videos_list_title'), PageChooserPanel('videos_list'), FieldPanel('videos_button_title'), ]),
#         ], heading="Videos", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('audios_list_title'), PageChooserPanel('audios_list'), FieldPanel('audios_button_title'), ]),
#         ], heading="Audios", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('documents_list_title'), PageChooserPanel('documents_list'), FieldPanel('documents_button_title'), ]),
#         ], heading="Presentaciones", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('events_list_title'), PageChooserPanel('events_list'), FieldPanel('events_button_title'), ]),
#         ], heading="Eventos", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('podcast_list_title'), FieldPanel('podcast_iframe_url'), FieldPanel('podcast_url'), FieldPanel('podcats_button_title'), ]),
#         ], heading="Podcast", classname="collapsible"),
#         MultiFieldPanel([
#             MultiFieldPanel(
#                 [FieldPanel('social_networks_title'), StreamFieldPanel('social_networks')]),
#         ], heading="Redes Sociales", classname="collapsible"),
#     ]
