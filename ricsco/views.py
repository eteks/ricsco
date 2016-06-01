from django.shortcuts import render
from django.shortcuts import *
from actors.models import *
from django.conf import settings
from django.contrib import messages
from django.contrib.gis.geoip import GeoIP
from django.core import serializers
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib.auth.models import User
from django.db.models import Count, F, Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.template.defaultfilters import stringfilter
from django.utils.timezone import utc
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
from datetime import datetime, timedelta
from time import time
from urllib import unquote, urlencode, unquote_plus

def home(request): 
  return render_to_response('base.html',
    context_instance=RequestContext(request))
def signup_view(request): 
  return render_to_response('sign_up.html',
    context_instance=RequestContext(request))
# def home_v2(request, 
#   template='ricsco/home_new.html', 
#   page_template='ricsco/lead_index_page_new.html'):
    
#     # if request.user.is_authenticated():
#     #     return HttpResponseRedirect("/dashboard/start/")       
#     # for home page business calculation
#     ap_date = datetime.utcnow().replace(tzinfo=utc)
#     created = request.POST.get('lead_created')
    
#     error_status_ar = int(request.GET.get('ar', 0))
    
#     inactive_usr_msg = _('User is inactive')
#     incorrect_usr_pwd = _('Incorrect username or password')
    
#     # if error_status_ar == 1:
#     #     return render_to_response('fxapi/index.html', {
#     #         'error_messageee': inactive_usr_msg,
#     #     },context_instance=RequestContext(request))
      

# def home(request): 
#   return render_to_response('Hello world', 
#     context_instance=RequestContext(request))
# def home(request):
#     return HttpResponse('navigation_bar.html')
