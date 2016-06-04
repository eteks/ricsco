from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
import logging
import datetime as dt
from django.db import transaction
from models import *
from actors.models import *
from control.models import *
# Create your views here.

@login_required
# @transaction.commit_on_success
def leadSave(request):
    # try:   
    if request.POST.get('txthidden'):
        # Edit provided lead
        leadId = request.POST.get('txthidden')
        actor = request.user.actor
        lead = Lead.objects.get(pk=leadId)
        consumer = lead.consumer
        consumercompany = lead.consumer.company
        companyaddress = lead.consumer.company.address
        consumeraddress = lead.consumer.address
        
        consumeraddress.street = request.POST.get('consumeraddress_address', '')
        consumeraddress.postal_code = request.POST.get('consumeraddress_postal_code', '')
        consumeraddress.city = request.POST.get('consumeraddress_city', '')
        consumeraddress.state = request.POST.get('consumeraddress_state', '')
        consumeraddress.region = request.POST.get('consumeraddress_region', '')
        consumeraddress.country = request.POST.get('consumeraddress_country', '')    
        consumeraddress.geotag = request.POST.get('consumeraddress_geotag', '')
        consumeraddress.save()
        
        companyaddress.postal_code = request.POST.get('companyaddress_postalcode', '')
        companyaddress.country = request.POST.get('companyaddress_country', '')
        companyaddress.city = request.POST.get('companyaddress_city', '')
        companyaddress.street = request.POST.get('companyaddress_address', '')
        companyaddress.save() 

    
        consumercompany.name = request.POST.get('companyabstract_name', '')
        consumercompany.phone_number = request.POST.get('companyabstract_phoneno', '')
        consumercompany.email = request.POST.get('companyabstract_email', '')
        if request.POST.get('companyabstract_cin', ''):
            consumercompany.cin = request.POST.get('companyabstract_cin', '')

        consumercompany.address = companyaddress
        consumercompany.website = request.POST.get('companyabstract_website', '')
        consumercompany.alt_phone_number = request.POST.get('companyabstract_alt_phone_number', '')

        consumercompany.industry = request.POST.get('consumercompany_industry', '')
        if request.POST.get('consumercompany_no_of_employees', ''):
            consumercompany.no_of_employees = request.POST.get('consumercompany_no_of_employees', '')
        if request.POST.get('consumercompany_turn_over', ''):
            consumercompany.turn_over = request.POST.get('consumercompany_turn_over', '')
        if request.POST.get('consumercompany_profit', ''):
            consumercompany.profit = request.POST.get('consumercompany_profit', '')
        consumercompany.company_financial_data_currency = request.POST.get('consumercompany_company_financial_data_currency', '')
        consumercompany.save()

        consumer.first_name = request.POST.get('consumer_first_name', '')
        consumer.last_name = request.POST.get('consumer_last_name', '')
        consumer.email = request.POST.get('consumer_email', '')
        consumer.skype = request.POST.get('consumer_skype', '')
        consumer.phone_number = request.POST.get('consumer_phone_number', '')
       
        
        consumer.title = request.POST.get('consumer_title', '')
        consumer.gender = request.POST.get('consumer_gender', '')
        
        consumer.alt_phone_number = request.POST.get('consumer_alt_phone_number', '')    
        consumer.best_call_time = request.POST.get('consumer_best_call_time', '')
        consumer.preferred_method = request.POST.get('consumer_preferred_method', '')
         
        if request.POST.get('consumer_ssn', ''):
            consumer.ssn = request.POST.get('consumer_ssn', '')
        birthdate = request.POST.get('consumer_date_of_birth', '')
        birthdate = birthdate.replace("/","-")  
        if birthdate:
            consumer.date_of_birth = dt.datetime.strptime(birthdate,"%m-%d-%Y")   
        consumer.language = request.POST.get('consumer_language', '')
        consumer.save()
        
        leadcategoryid = LeadCategory.objects.get(pk=int(request.POST.get('lead_category')))       

        lead.title = request.POST.get('lead_title', '')
        lead.sale = request.POST.get('lead_available', '')
        lead.description = request.POST.get('lead_description', '')
        lead.read_more_link = request.POST.get('lead_read_more_link', '')
        lead.price = float(request.POST.get('lead_price'))
        lead.budget_currency = lead.price_currency
        lead.reference = request.POST.get('lead_reference', '')
        pre_sold_value = request.POST.get('pre_sold', 0)
        if pre_sold_value:
            lead.pre_sold = pre_sold_value
        else:
            lead.pre_sold = 0
        lead.budget = request.POST.get('lead_budget', '')
        lead.category = leadcategoryid
        lead.consumer = consumer
        lead.language = request.POST.get('language', '')
        lead.status = request.POST.get('status_change', '')
        lead.generation_source = request.POST.get('generation_source', '')
        lead.generation_method = request.POST.get('generation_method', '')
        lead.accept_campaign = int(request.POST.get('accept_campaign', 0))
        lead.reinquire = int(request.POST.get('reinquire_lead', 0))
        
        startdate = request.POST.get('lead_deal_starts', '')
        startdate = startdate.replace("/", "-")
        enddate = request.POST.get('lead_deal_ends', '')
        enddate = enddate.replace("/","-")
        if startdate:
            lead.deal_starts = dt.datetime.strptime(startdate,"%m-%d-%Y")
        if enddate:    
            lead.deal_ends = dt.datetime.strptime(enddate,"%m-%d-%Y")
        
        lead.save()

        saved_keywords = []
        keywords = request.POST.get('lead_keywords', '')
        if keywords:
            for keyword in keywords.split(','):
                kw, created = LeadKeyword.objects.get_or_create(name=keyword)
                saved_keywords.append(kw)
    
            if saved_keywords:
                lead.keywords = saved_keywords
                lead.save()

        return HttpResponseRedirect('/dashboard/providedlead/')
        
    else:
        # Adding new lead
        actor = request.user.actor
        consumeraddress = ConsumerAddress()
        consumeraddress.street = request.POST.get('consumeraddress_address', '')
        consumeraddress.postal_code = request.POST.get('consumeraddress_postal_code', '')
        consumeraddress.city = request.POST.get('consumeraddress_city', '')
        consumeraddress.state = request.POST.get('consumeraddress_state', '')
        consumeraddress.region = request.POST.get('consumeraddress_region', '')
        consumeraddress.country = request.POST.get('consumeraddress_country', '')    
        consumeraddress.geotag = request.POST.get('consumeraddress_geotag', '')
        consumeraddress.save()
        
        companyaddress = CompanyAddress()
        companyaddress.postal_code = request.POST.get('companyaddress_postalcode', '')
        companyaddress.country = request.POST.get('companyaddress_country', '')
        companyaddress.city = request.POST.get('companyaddress_city', '')
        companyaddress.street = request.POST.get('companyaddress_address', '')
        companyaddress.save() 
    
        consumercompany = ConsumerCompany()     
        consumercompany.name = request.POST.get('companyabstract_name', '')
        consumercompany.phone_number = request.POST.get('companyabstract_phoneno', '')
        consumercompany.email = request.POST.get('companyabstract_email', '')
        if request.POST.get('companyabstract_cin', ''):
            consumercompany.cin = request.POST.get('companyabstract_cin', '')
        consumercompany.address = companyaddress
        consumercompany.website = request.POST.get('companyabstract_website', '')
        consumercompany.alt_phone_number = request.POST.get('companyabstract_alt_phone_number', '')
        
        consumercompany.industry =   request.POST.get('consumercompany_industry', '')
        if request.POST.get('consumercompany_no_of_employees', ''):
            consumercompany.no_of_employees =   request.POST.get('consumercompany_no_of_employees', '')
        if request.POST.get('consumercompany_turn_over', ''):
            consumercompany.turn_over =   request.POST.get('consumercompany_turn_over', '')
        if request.POST.get('consumercompany_profit', ''):
            consumercompany.profit =   request.POST.get('consumercompany_profit', '')
        consumercompany.company_financial_data_currency =   request.POST.get('consumercompany_company_financial_data_currency', '')
        consumercompany.save()
    
          
        consumer = Consumer()
        consumer.first_name = request.POST.get('consumer_first_name', '')
        consumer.last_name = request.POST.get('consumer_last_name', '')
        consumer.email = request.POST.get('consumer_email', '')
        consumer.skype = request.POST.get('consumer_skype', '')
        consumer.phone_number = request.POST.get('consumer_phone_number', '')
        consumer.address = consumeraddress
        consumer.company = consumercompany
        consumer.title = request.POST.get('consumer_title', '')
        consumer.gender = request.POST.get('consumer_gender', '')           
        consumer.alt_phone_number = request.POST.get('consumer_alt_phone_number', '')    
        consumer.best_call_time = request.POST.get('consumer_best_call_time', '')
        consumer.preferred_method = request.POST.get('consumer_preferred_method', '')             
        consumer.ssn = request.POST.get('consumer_ssn', '')
        birthdate = request.POST.get('consumer_date_of_birth', '')
        birthdate = birthdate.replace("/","-")
        if birthdate:
            consumer.date_of_birth = dt.datetime.strptime(birthdate, "%m-%d-%Y")   
        consumer.language = request.POST.get('consumer_language', '')
        consumer.save()
        
        lead = Lead()
        lead.title = request.POST.get('lead_title', '')
        lead.sale = request.POST.get('lead_available', '')
        lead.description = request.POST.get('lead_description', '')
        lead.read_more_link = request.POST.get('lead_read_more_link', '')
        lead.price = float(request.POST.get('lead_price'))
        lead.price_currency = request.POST.get('lead_price_currency')
        lead.language = request.POST.get('language', '')
        lead.status = request.POST.get('status_change', '')
        lead.generation_method = request.POST.get('generation_method', '')
        lead.generation_source = request.POST.get('generation_source', '')
        lead.accept_campaign = int(request.POST.get('accept_campaign', 0))
        lead.reinquire = int(request.POST.get('reinquire_lead', 0))
        lead.seller = actor
        lead.consumer = consumer
        lead.reference = request.POST.get('lead_reference', '')
        
        pre_sold_value = request.POST.get('pre_sold', 0)
        if pre_sold_value:
            lead.pre_sold = pre_sold_value
        else:
            lead.pre_sold = 0
        
        lead_budget = request.POST.get('lead_budget', 0)
        if lead_budget:
            lead.budget = lead_budget
        else:
            lead.budget = 0
        lead.budget_currency = lead.price_currency
        
        lead_category = request.POST.get('lead_category', '')
        if lead_category:
            lead.category = LeadCategory.objects.get(pk=int(lead_category))
        
        startdate = request.POST.get('lead_deal_starts', '')
        startdate = startdate.replace("/", "-")
        enddate = request.POST.get('lead_deal_ends', '')
        enddate = enddate.replace("/","-")
        if startdate:
            lead.deal_starts = dt.datetime.strptime(startdate,"%m-%d-%Y")
        if enddate:
            lead.deal_ends = dt.datetime.strptime(enddate,"%m-%d-%Y")   
        
        # if check_moderation():
        #     lead.active = False
        #     lead.inactive_reason = 'moderate'
        
        lead.save()
        
        # # If auction parameters available then we send this lead for Auction
        # auction_status = update_auction(request, lead)
        # if isinstance(auction_status, str):
        #     logging.info("Error at lead save : {} : {} ".format(
        #                  actor.email, auction_status))
        #     raise Exception(actor.email + ' : ' + auction_status)

        saved_keywords = []
        keywords = request.POST.get('lead_keywords', '')
        if keywords:
            for keyword in keywords.split(','):
                kw, created = LeadKeyword.objects.get_or_create(name=keyword)
                saved_keywords.append(kw)
    
            if saved_keywords:
                lead.keywords = saved_keywords
                lead.save()
        
        provided_leads = ActorProvidedLead()   
        provided_leads.lead = lead
        provided_leads.actor = actor
        provided_leads.save()
    # except Exception, error:
    #     # print 'transaction rolling back'
    #     logging.error("Error while creating lead %s" % error)
    #     transaction.rollback()
    # else:
    #     # print 'transaction committed'
    #     transaction.commit()
    return HttpResponseRedirect('/dashboard/providedlead/')

@login_required
def edit_leads(request, pk):
    actor = request.user.actor
    if not actor.is_sellerregistered:
        return HttpResponseRedirect(reverse('providedlead'))
    
    try:
        lead = actor.actorprovidedlead_set.get(lead__id=int(pk)).lead

        if lead.keywords:
            keywords = ','.join([kw.name for kw in lead.keywords.all()])
        else:
            keywords = ''
        leadcategory = LeadCategory.objects.order_by('name')
        return render_to_response('dashboard/edit_new_leads.html', {
                                    'keywords':keywords, 'leads':lead, 'consumer':lead.consumer, 
                                    'consumeraddress': lead.consumer.address,
                                    'consumercompany': lead.consumer.company, 
                                    'companyaddress': lead.consumer.company.address,
                                    'leadcategory': leadcategory,'selectedcategory':lead.category,
                                },context_instance=RequestContext(request))
    except:
        return HttpResponseRedirect('/dashboard/providedlead/')
