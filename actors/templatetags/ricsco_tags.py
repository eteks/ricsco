import re
from django import template
from core import config as fixido_config
register = template.Library()
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy, ugettext as _ 
from django.utils.numberformat import format
from django.template.defaultfilters import stringfilter
from django.conf import settings
from urllib import unquote

@register.filter(is_safe=True)
def country_name(value, default=""):
    if not value: value = ''
    value = value.upper()
    if value not in fixido_config.COUNTRIES_DICT:
        return default
    
    return _(fixido_config.COUNTRIES_DICT[value])
    
@register.filter(is_safe=True)
def countries_as_option(value):
    output = []
    '''
    for key, val in fixido_config.COUNTRIES_DICT.iteritems():
        selected = 'selected="selected"' if key == value else ''
        output.append('<option value="%s" %s>%s</option>' %(key, selected, _(val)))
    '''
    country_list = sorted(['%s_%s' % (_(v), k) for k, v in fixido_config.COUNTRIES_DICT.iteritems() if k])
    country_list.insert(0, '%s_' % _(fixido_config.COUNTRIES_DICT['']))
    for vk in country_list:
        val, key = vk.split('_')
        selected = 'selected="selected"' if key == value else ''
        output.append('<option value="%s" %s>%s</option>' %(key, selected, _(val)))

    return "".join(output) 

@register.filter(is_safe=True)
def currencies_as_option(value):
    output = []
    for val, key in fixido_config.CURRENCIES_DICT.iteritems():
        selected = 'selected="selected"' if key == value else ''
        output.append('<option value="%s" %s>%s</option>' %(key, selected, _(val)))

    return "".join(output) 



    
