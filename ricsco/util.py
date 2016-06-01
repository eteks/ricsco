import os
import random
import string
import uuid
import urllib2

from django.conf import settings

def remove_none(field, empty_str=''):
    ''' This utility remove none and select strings
    '''
    try:
        if not field or field.lower() == 'none' or field.lower() == 'select':
            return empty_str
    except Exception, e:
        pass
    return field