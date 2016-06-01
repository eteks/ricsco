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
from control.models import Tempdata


logger = logging.getLogger('myapplog')
def start_new(request): 
  print "test"
  return render_to_response('dashboard/joinuslanding_new.html',
    context_instance=RequestContext(request))
       

# @csrf_exempt
# @login_required
def providedlead(request):
    # actors = request.user.actor
    actors = Actor.objects.get(username="kalairkv.mca14@gmail.com")
    if not actors.is_sellerregistered:
        
        if 'seller_registration' in request.POST:
            lead_type = request.POST.get('lead_type', '')
            categories = request.POST.get('categories', '')
            volume = request.POST.get('lead_volume', '')
            sites = request.POST.get('sites', '')
            company_name = request.POST.get('company_name', '')
            contact_person = request.POST.get('contact_person', '')
            phone_no = request.POST.get('phone_number', '')
            email_id = request.POST.get('email', '')
            current_site = get_current_site(request)
            
            sellerregistered = Tempdata()
            # sellerregistered.user_id = request.user
            sellerregistered.user_id = actors.email
            sellerregistered.is_send = True
            sellerregistered.save()
            # userseller = 'actor not seller'
            # usernotseller = None
            # language = request.user.actor.language.lower()
            
            # if settings.SITE_NAME == 'fixido.com':
            #     try:
            #         send_templated_mail(
            #             template_name="sellerregistration",
            #             subject = "Seller Registration",
            #             from_email = settings.DEFAULT_FROM_EMAIL,
            #             recipient_list=['sastha@globalensolutions.com'],
            #             context={
            #                      'type':lead_type,
            #                      'categories':categories,
            #                      'volume':volume,
            #                      'sites':sites,
            #                      'company_name':company_name,
            #                      'contact_person':contact_person,
            #                      'phone_no':phone_no,
            #                      'email_id':email_id,
            #                      'language':language,
            #                      'current_site':current_site,
            #                      'version' : settings.STATIC_VERSION,
            #             },
            #         )
            #     except Exception, e:
            #         logging.error('Not sent sellerregistration email (@providedlead) %s' % e)
        
        # if Tempdata.objects.filter(user_id=request.user.email, is_send=True).exists():
       	if Tempdata.objects.filter(user_id=actors.email, is_send=True).exists():
            userseller = 'actor not seller'
            usernotseller = None
        else:
            usernotseller = 'seller'  
            userseller = None   
                       
        return render_to_response('dashboard/providedleads.html', {
                    "usernotseller":usernotseller, "userseller":userseller,
                }, context_instance=RequestContext(request))                 
    else:
        userseller = 'actor seller'
        providedlead = actors.actorprovidedlead_set.exclude(
                            lead__inactive_reason='user_deleted'
                        ).order_by('-created')
        
        # status = request.POST.get('status', 'all')
        # lead_filter = request.POST.get('filter', '')
        
        # if request.method == 'POST':
        #     if status != 'all':
        #         providedlead = providedlead.filter(
        #                             lead__active=True,
        #                             lead__status__iexact=status, 
        #                         )
        #     if lead_filter:
        #         try:
        #             lead_filter = int(lead_filter)
        #         except Exception, e:
        #             providedlead = providedlead.filter(lead__title__icontains=lead_filter)
        #         else:
        #             providedlead = providedlead.filter(
        #                 Q(lead__id=lead_filter) | Q(lead__title__icontains=lead_filter))
                    
        # sort_order = None
        # sort_order_title = None
        # sort_order_leadsleft = None
        # sort_order_id = None
        # sort_order_date = None
        # sort_order_leadstatus = None 
        # sort_order_price = None
        
        # next_sorting_title = None
        # next_sorting_leadsleft = None
        # next_sorting_id = None
        # next_sorting_date = None
        # next_sorting_status = None
        # next_sorting_price = None
        
        # if request.GET :
        #     if 'sort_order' in request.GET:
        #         sort_order = request.GET['sort_order']
        #         if request.GET['sort_by'] == 'title':
        #             if sort_order == 'asc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                                 lead__inactive_reason='user_deleted'
        #                             ).order_by('lead__title')
        #                 next_sorting_title = 'desc'
        #                 sort_order_title = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                                 lead__inactive_reason='user_deleted'
        #                             ).order_by('-lead__title')
        #                 next_sorting_title = 'asc'
        #                 sort_order_title = 'desc'
        #         elif request.GET['sort_by'] == 'leads_left':
        #             if sort_order == 'asc': 
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                            lead__inactive_reason='user_deleted'
        #                        ).extra(select={'available': "sale - sold"}).order_by('available')
        #                 next_sorting_leadsleft = 'desc'
        #                 sort_order_leadsleft = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                            lead__inactive_reason='user_deleted'
        #                        ).extra(select={'available': "sale - sold"}).order_by('-available')
        #                 next_sorting_leadsleft = 'asc'
        #                 sort_order_leadsleft = 'desc'
                     
        #         elif request.GET['sort_by'] == 'leads_id':
        #             if sort_order == 'asc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('lead__id')
        #                 next_sorting_id = 'desc'
        #                 sort_order_id = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('-lead__id')
        #                 next_sorting_id = 'asc'
        #                 sort_order_id = 'desc'
                     
        #         elif request.GET['sort_by'] == 'created':
        #             if sort_order == 'asc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'    
        #                         ).order_by('created')
        #                 next_sorting_date = 'desc'
        #                 sort_order_date = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'    
        #                         ).order_by('-created')
        #                 next_sorting_date = 'asc'
        #                 sort_order_date = 'desc'
                     
        #         elif request.GET['sort_by'] == 'lead_status':
        #             if sort_order == 'asc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('lead__inactive_reason')
        #                 next_sorting_status = 'desc'
        #                 sort_order_leadstatus = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('-lead__inactive_reason')
        #                 next_sorting_status = 'asc'
        #                 sort_order_leadstatus = 'desc'
                        
        #         elif request.GET['sort_by'] == 'lead_price':
        #             if sort_order == 'asc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('lead__price')
        #                 next_sorting_price = 'desc'
        #                 sort_order_price = 'asc'
        #             elif sort_order == 'desc':
        #                 providedlead = actors.actorprovidedlead_set.exclude(
        #                             lead__inactive_reason='user_deleted'
        #                         ).order_by('-lead__price')
        #                 next_sorting_price = 'asc'
        #                 sort_order_price = 'desc'
            
            
        if providedlead.count() < 1:
           no_result_found = 'no result found'
           result_found = None
        else:
            no_result_found = None
            result_found = 'result found'
        
        # status = status.capitalize()
        # return render_to_response('dashboard/providedleads.html', {
        #        "userseller":userseller, "result_found":result_found, 
        #        "no_result_found":no_result_found, "providedlead":providedlead, 
        #        "basketline": getCheckOutInfo(request.user.id),
        #        "filter":lead_filter, "status":status,
        #        'sort_order':sort_order,
        #        'sort_order_title':sort_order_title,
        #        'sort_order_leadsleft':sort_order_leadsleft,
        #        'sort_order_id':sort_order_id,
        #        'sort_order_date':sort_order_date,
        #        'sort_order_leadstatus':sort_order_leadstatus,
        #        'sort_order_price':sort_order_price,
        #        'next_sorting_title':next_sorting_title,
        #        'next_sorting_leadsleft': next_sorting_leadsleft,
        #        'next_sorting_id' : next_sorting_id,
        #        'next_sorting_date' : next_sorting_date,
        #        'next_sorting_status' : next_sorting_status,
        #        'next_sorting_price' : next_sorting_price,
        #     }, context_instance=RequestContext(request))    
         
        return render_to_response('dashboard/providedleads.html', {
               "userseller":userseller, "result_found":result_found, 
               "no_result_found":no_result_found, "providedlead":providedlead, 
            }, context_instance=RequestContext(request))    

# @login_required
def add_new_leads(request):
    # if not request.user.actor.is_sellerregistered:
    #     return HttpResponseRedirect(reverse('providedlead'))
    
    # leadcategory = LeadCategory.objects.order_by('name')
    # return render_to_response('dashboard/add_new_leads.html', {
    #                                 'leadcategory':leadcategory, 
    #                             },context_instance=RequestContext(request))

    return render_to_response('dashboard/add_new_leads.html',context_instance=RequestContext(request))

