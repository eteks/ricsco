import time
import datetime as dt
import datetime
import logging

from urllib import unquote

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.defaultfilters import stringfilter
from django.utils import translation
from django.utils.translation import ugettext, string_concat
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt
from actors.models import *

logger = logging.getLogger('myapplog')

       
@login_required
def start_new(request):
    if request.user.is_superuser:
        logout(request)
        return HttpResponseRedirect('/')
        
   
 
    
    if 'seller_registration' in request.POST:
               
        return render_to_response('dashboard/joinuslanding_new.html',context_instance=RequestContext(request))