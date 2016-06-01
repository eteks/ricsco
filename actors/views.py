import json
import time
import math
import logging

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.messages import get_messages
from django.conf import settings
#from lockout.exceptions import LockedOut

from models import *
from actors.models import *
from django import forms
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.core.exceptions import ValidationError
from django.db.models import F, Q
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.utils import translation
from django.utils.http import urlencode, base36_to_int
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext, string_concat
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from urllib import urlencode
from urllib import unquote_plus
from django.template.loader import render_to_string

logger = logging.getLogger('myapplog')

def login_view(request):
    if not request.method == 'POST':
        return HttpResponseRedirect('/')
    username = request.POST['auth_name']
    password = request.POST['auth_paw']

    inactive_usr_msg = ugettext('User is inactive')
    incorrect_usr_pwd = ugettext('Incorrect username or password')
    # lockout_msg = string_concat(ugettext('We locked your account for'), ' ' + 
    #     str(settings.LOCKOUT_TIME / 60) + ' ')
    # lockout_msg = string_concat(lockout_msg, ugettext('min'))
    
    response = None
    user = authenticate(username=username, password=password)
    
    try:
        try:
            actor = Actor.objects.get(email=username)
        except Actor.DoesNotExist:
            print "Actor error"
            raise ValidationError(incorrect_usr_pwd, 2)
        
        if user is not None:
            if user.is_active :
                login(request, user)
                print "login"
                response = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                # return render_to_response('dashboard/joinuslanding_new.html',{'username':username},context_instance=RequestContext(request))

            else:
                print "not active"
                raise ValidationError(inactive_usr_msg, 1)
            
            if not response: 
                print "response"
                print next
                response = HttpResponseRedirect(request.POST['next'])
        else:
            user = User.objects.get(email=username)
            print "validation error"
            raise ValidationError(incorrect_usr_pwd, 2)
    
    except ValidationError as e:
        
        messages.add_message(request, messages.ERROR, e.messages[-1])
    return response

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
