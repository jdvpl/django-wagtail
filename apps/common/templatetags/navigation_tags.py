
from django import template
from wagtail.core.models import Page, Site
from ..models import HeaderBlock, FooterBlock, AffiliatedEntitiesBlock, RelatedEntitiesBlock, InfoEntitiesBlock
from ..models import Sector, Year


register = template.Library()


@register.inclusion_tag('includes/header_block.html', takes_context=True)
def get_header(context):
    """Expone el contenido del componente de encabezado
    @param context :Object
    @see header_block.html
    """
    links = ""
    if HeaderBlock.objects.first() is not None:
        links = HeaderBlock.objects.first().links
    return {
        'links': links,
    }


@register.inclusion_tag('blocks/gov_bar_block.html', takes_context=True)
def get_gov_bar(context):
    """Expone el contenido del componente de encabezado
    @param context :Object
    @see header_block.html
    """
    links = ""
    if HeaderBlock.objects.first() is not None:
        links = HeaderBlock.objects.first().links
    return {
        'links': links,
    }


@register.inclusion_tag('includes/footer_block.html', takes_context=True)
def get_footer(context):
    """Expone el contenido del componente de pie
    @param context :Object
    @see footer_block.html
    """
    general_info = ""
    social_networks = ""
    contact_info = ""
    if FooterBlock.objects.first() is not None:
        general_info = FooterBlock.objects.first().general_info
        social_networks = FooterBlock.objects.first().social_networks
        contact_info = FooterBlock.objects.first().contact_info
    return {
        'general_info': general_info,
        'social_networks': social_networks,
        'contact_info': contact_info,
    }


@register.inclusion_tag('blocks/footer_block.html', takes_context=True)
def get_footer_mme(context):
    """Expone el contenido del componente de pie
    @param context :Object
    @see footer_block.html
    """
    general_info = ""
    social_networks = ""
    contact_info = ""
    if FooterBlock.objects.first() is not None:
        general_info = FooterBlock.objects.first().general_info
        social_networks = FooterBlock.objects.first().social_networks
        contact_info = FooterBlock.objects.first().contact_info
    return {
        'general_info': general_info,
        'social_networks': social_networks,
        'contact_info': contact_info,
    }


@register.inclusion_tag('includes/affiliated_entities_block.html', takes_context=True)
def get_affiliated_entities(context):
    """Expone el contenido del componente de
    entidades afiliadas
    @param context :Object
    @see affiliated_entities_block.html
    """
    sector_company = ""
    if AffiliatedEntitiesBlock.objects.first() is not None:
        sector_company = AffiliatedEntitiesBlock.objects.first().sector_company
    return {
        'sector_company': sector_company,
    }


@register.inclusion_tag('blocks/affiliated_entities_block.html', takes_context=True)
def get_affiliated_entities_block(context):
    """Expone el contenido del componente de
    entidades afiliadas
    @param context :Object
    @see affiliated_entities_block.html
    """
    sector_company = ""
    if AffiliatedEntitiesBlock.objects.first() is not None:
        sector_company = AffiliatedEntitiesBlock.objects.first().sector_company
    return {
        'sector_company': sector_company,
    }


@register.inclusion_tag('blocks/related_entities_block.html', takes_context=True)
def get_related_entities(context):
    """Expone el contenido del componente de
    entidades vinculadas
    @param context :Object
    @see related_entities_block.html
    """
    sector_company = ""
    if RelatedEntitiesBlock.objects.first() is not None:
        sector_company = RelatedEntitiesBlock.objects.first().sector_company
    return {
        'sector_company': sector_company,
    }


@register.inclusion_tag('blocks/affiliated_entities_mobil_block.html', takes_context=True)
def get_affiliated_entities_mobil_block(context):
    """Expone el contenido del componente de
    entidades afiliadas
    @param context :Object
    @see affiliated_entities_block.html
    """
    sector_company = ""
    if AffiliatedEntitiesBlock.objects.first() is not None:
        sector_company = AffiliatedEntitiesBlock.objects.first().sector_company
    return {
        'sector_company': sector_company,
    }


@register.inclusion_tag('blocks/related_entities_mobil_block.html', takes_context=True)
def get_related_entities_mobil_block(context):
    """Expone el contenido del componente de
    entidades vinculadas
    @param context :Object
    @see related_entities_block.html
    """
    sector_company = ""
    if RelatedEntitiesBlock.objects.first() is not None:
        sector_company = RelatedEntitiesBlock.objects.first().sector_company
    return {
        'sector_company': sector_company,
    }

@register.inclusion_tag('blocks/interest_places_block.html', takes_context=True)
def get_interest_places(context):
    """Expone el contenido del componente de
    sitios de interes
    @param context :Object
    @see interest_places_block.html
    """
    inf_entity = ""
    if InfoEntitiesBlock.objects.first() is not None:
        inf_entity = InfoEntitiesBlock.objects.first().inf_entity
    return {
        'inf_entity': inf_entity,
    }


@register.inclusion_tag('blocks/information_systems_block.html', takes_context=True)
def get_information_systems(context):
    """Expone el contenido del componente de
    sistemas de informacion
    @param context :Object
    @see informaiton_systems_block.html
    """
    inf_entity = ""
    if InfoEntitiesBlock.objects.first() is not None:
        inf_entity = InfoEntitiesBlock.objects.first().inf_entity
    return {
        'inf_entity': inf_entity,
    }


@register.inclusion_tag('includes/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('blocks/sectors_block.html', takes_context=True)
def get_sectors_mme(context):

    sectors = ""
    if Sector.objects.all() is not None:
        sectors = Sector.objects.all().order_by('sector_title')

    return {
        'sectors': sectors
    }


@register.inclusion_tag('blocks/years_block.html', takes_context=True)
def get_years_mme(context):

    years = ""
    if Year.objects.all() is not None:
        years = Year.objects.all().order_by('year')

    return {
        'years': years
    }
