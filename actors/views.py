import json
import time
import math
import logging

# from django.core.mail import EmailMessage
# from django.template import Context
# from django.template.loader import render_to_string, get_template
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

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
from ricsco.util import *
from models import *
from actors.models import *
# from templated_email import send_templated_mail
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
    # print "after authenticate"
    
    try:
        try:
            actor = Actor.objects.get(email=username)
        except Actor.DoesNotExist:
            # print "Actor error"
            raise ValidationError(incorrect_usr_pwd, 2)
        
        if user is not None:
            if user.is_active :
                login(request, user)
                # print "login"
                response = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                # return render_to_response('dashboard/joinuslanding_new.html',{'username':username},context_instance=RequestContext(request))

            else:
                # print "not active"
                raise ValidationError(inactive_usr_msg, 1)
            
            if not response: 
                response = HttpResponseRedirect(request.POST['next'])
        else:
            # print "same email"
            # user = User.objects.get(email=username)
            # print "validation error"
            raise ValidationError(incorrect_usr_pwd, 2)
    
    except ValidationError as e:
        
        messages.add_message(request, messages.ERROR, e.messages[-1])

        redirect_path = request.POST['next']
        query_string = 'st=%d' % e.code
        redirect_url = format_redirect_url(redirect_path, query_string)
        response = HttpResponseRedirect(redirect_url)
   
    return response

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def create_new_user(request):
    if request.method == 'POST' and request.user.is_anonymous():
        error = {}
        email = request.POST.get('email_p', request.POST.get('email', ''))

        # from django.core.validators import validate_email
        # try:
        #     validate_email( email )
        # except:
        #     error['email_exists'] = ugettext('Enter your email address')
        
        if User.objects.filter(username=email, email=email).exists():
            error['email_exists'] = ugettext('This Email already exists')
        if error:
            messages.add_message(request, messages.ERROR, error['email_exists'])
            response = HttpResponseRedirect('/signup/')
        else:
            caddress = CompanyAddress()
            caddress.street = request.POST.get('company_street', '')
            caddress.postal_code = request.POST.get('company_postal_code', '')
            caddress.city = request.POST.get('company_city', '')
            caddress.country = request.POST.get('company_country', '')
            caddress.save()
            
            company = ActorCompany()
            company.name = request.POST.get('company_name_p', request.POST.get('company_name', ''))
            company.phone_number = request.POST.get('company_phone_number', '')
            company.description = request.POST.get('company_description', '')
            company.website = request.POST.get('company_website', '')
            company.address = caddress
            company.save()
            
            address = ActorAddress()
            address.street = request.POST.get('street', '')
            address.postal_code = request.POST.get('postal_code', '')
            address.city = request.POST.get('city', '')
            address.country = request.POST.get('country', '')
            address.save()
            
            actor = Actor()
            actor.email = email        
            actor.username = email
            # actor.Registration_IPnumber = globals.ip
            actor.first_name = request.POST.get('fname_p', 
                request.POST.get('fname', ''))
            actor.last_name = request.POST.get('lname', '')
            actor.phone_number = request.POST.get('phone_number_p', 
                request.POST.get('phone_number', ''))

            # actor.language = get_global_language(request)
            # pwd = generatePassword()
            # actor.set_password(pwd)
            pwd = generatePassword()
            actor.set_password(pwd)
            current_site = get_current_site(request)
            confirmation_keyy = actor.confirmation_key
            actor.company = company
            actor.address = address
            # actor.currency = request.POST.get('currency', 
            #     LANGUAGE_CURRENCIES[actor.language]).upper()

            # actor.invite_code = request.POST.get('invite_code', '')
            # if 'googleinv_code' in request.POST:
            #     actor.signup_method = 'Registration_1'
            # elif 'googleinv_code_500' in request.POST:
            #     actor.signup_method = 'Registration_2'
            # elif 'campaigninv_code' in request.POST:
            #     actor.signup_method = 'Registration_3'
            # else:
            #     actor.signup_method = 'Website'

            actor.save()
            response = render_to_response('dashboard/joinuslanding_new.html')
            user = authenticate(username=email, password=pwd)
            login(request, user)
            response = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            try:
               
                # send_templated_mail(
                #     template_name = 'welcome',
                #     subject = 'Welcome to Ricsco.com',
                #     from_email = settings.DEFAULT_FROM_EMAIL,
                #     recipient_list = [email,],
                #     bcc = settings.INFO_EMAIL_BCC,
                #     context={
                #              'actor': actor,
                #              'current_site': current_site,
                #              'confirmation_keyy': confirmation_keyy,
                #              'email': email,
                #              'password': pwd,
                #              'version' : settings.STATIC_VERSION,
                #     },
                # )
                # print "try"
                # send_templated_mail(
                #     template_name = 'welcome',
                #     subject = 'Welcome to Fixido.com',
                #     from_email = settings.DEFAULT_FROM_EMAIL,
                #     recipient_list = [email,],
                #     bcc = settings.INFO_EMAIL_BCC,
                #     context={
                #              'actor': actor,
                #              'current_site': current_site,
                #              'confirmation_keyy': confirmation_keyy,
                #              'email': email,
                #              'password': pwd,
                #              # 'version' : settings.STATIC_VERSION,
                #     },
                # )






                

                # subject, from_email, to = 'hello', 'sweetkannan05@gmail.com', 'shivaramcse05@gmail.com'
                # text_content = 'This is an important message.'
                # html_content = '<p> <b>This</b> <a href="www.google.com">is</a> an <strong>important</strong> message.</p>'
                # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                # msg.attach_alternative(html_content, "text/html")
                # msg.send()
                # # print '>>>>>>>', msg1

                htmly     = get_template('welcome.html')

                d = Context({ 'confirmation_keyy': confirmation_keyy, 'actor': actor, 'email': email, 'password': pwd, 'current_site': current_site,})

                subject, from_email, to = 'hello', settings.DEFAULT_FROM_EMAIL, email
                # text_content = plaintext.render(d)
                html_content = htmly.render(d)
                text_content = 'Welcome to Ricsco.'
                msg = EmailMultiAlternatives(subject,text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                # msg.send()
                # print '>>>>>>>>>>>>', msg


                # # username1=email
                # template = get_template('welcome.html')
                # context = Context({
                #     "actor": actor,
                #     "current_site": current_site,
                #     "confirmation_keyy": confirmation_keyy,
                #     "email": email,
                #     "password": pwd,                     
                #     # 'version' : settings.STATIC_VERSION,
                # }) 

                # content = strip_tags(template.render(context))
                # msg = EmailMessage("New signup form submission", content, to=[email])
                # msg.content_subtype = "text/html"
                # msg.send()
                # print '>>>>>>>>>>>>>>',content


            except Exception, e:
                print "exception"
            
    #     caddress = CompanyAddress()
    #     caddress.street = request.POST.get('company_street', '')
    #     caddress.postal_code = request.POST.get('company_postal_code', '')
    #     caddress.city = request.POST.get('company_city', '')
    #     caddress.country = request.POST.get('company_country', '')
    #     caddress.save()
        
    #     company = ActorCompany()
    #     company.name = request.POST.get('company_name_p', request.POST.get('company_name', ''))
    #     company.phone_number = request.POST.get('company_phone_number', '')
    #     company.description = request.POST.get('company_description', '')
    #     company.website = request.POST.get('company_website', '')
    #     company.address = caddress
    #     company.save()
        
    #     address = ActorAddress()
    #     address.street = request.POST.get('street', '')
    #     address.postal_code = request.POST.get('postal_code', '')
    #     address.city = request.POST.get('city', '')
    #     address.country = request.POST.get('country', '')
    #     address.save()
        
    #     actor = Actor()
    #     actor.email = email        
    #     actor.username = email
    #     actor.Registration_IPnumber = globals.ip
    #     actor.first_name = request.POST.get('fname_p', 
    #         request.POST.get('fname', ''))
    #     actor.last_name = request.POST.get('lname', '')
    #     actor.phone_number = request.POST.get('phone_number_p', 
    #         request.POST.get('phone_number', ''))

    #     actor.language = get_global_language(request)
    #     pwd = generatePassword()
    #     actor.set_password(pwd)
        
    #     actor.company = company
    #     actor.address = address
    #     actor.currency = request.POST.get('currency', 
    #         LANGUAGE_CURRENCIES[actor.language]).upper()

    #     actor.invite_code = request.POST.get('invite_code', '')
    #     if 'googleinv_code' in request.POST:
    #         actor.signup_method = 'Registration_1'
    #     elif 'googleinv_code_500' in request.POST:
    #         actor.signup_method = 'Registration_2'
    #     elif 'campaigninv_code' in request.POST:
    #         actor.signup_method = 'Registration_3'
    #     else:
    #         actor.signup_method = 'Website'
    #     actor.save()
        
    #     # if 'docfile' in request.FILES:
    #     #     form = DocumentForm(request.POST, request.FILES)
    #     #     if form.is_valid():
    #     #         newdoc = CompanyAbstract.objects.get(pk=actor.company.pk)
    #     #         newdoc.logo = request.FILES['docfile']
    #     #         newdoc.save()
        
    #     current_site = get_current_site(request)
    #     confirmation_keyy = actor.confirmation_key             
        
    #     account = Account()
    #     account.balance = 0.0
    #     account.type = ''
    #     account.tax_identification_number = ''
    #     account.vat_number = ''
    #     account.actor = actor    
    #     account.save()
        
    #     #invite code transactions
    #     invite_code = ''
        
    #     if 'googleinv_code' in request.POST:
    #         # this is for google reg page sign up they will get 1000SEK 
    #         try: invite_code = settings.GOOGLE_INVITE_CODE
    #         except Exception, e: pass
        
    #     elif 'googleinv_code_500' in request.POST:
    #         # this is for google reg page sign up they will get 500SEK 
    #         try: invite_code = settings.GOOGLE_INVITE_CODE_500
    #         except Exception, e: pass
            
    #     elif 'campaigninv_code' in request.POST:
    #         # this is for google reg page sign up they will get 500SEK 
    #         try: invite_code = settings.CAMPAIGN_INVITE_CODE
    #         except Exception, e: pass
            
    #     elif 'bonus_invite_code' in request.POST:
    #         # this is for google reg page sign up they will get 500SEK 
    #         try: invite_code = request.POST['bonus_invite_code']
    #         except Exception, e: pass
            
    #     elif 'voucher_code' in request.POST:
    #         try: invite_code = request.POST['voucher_code']
    #         except Exception, e: pass
            
        
    #     userip = globals.ip        
    #     if invite_code == '' or invite_code == None:
    #         pass
    #     else:
    #         try:
    #             v_obj = Voucher.objects.get(code=str(invite_code)) 
    #             exp_date = v_obj.expireDate
    #             issueddate = v_obj.issuedDate
    #             today = helper.get_now()
    #             ipcount = Transaction.objects.filter(UserIp=userip,
    #                 payment_reference=invite_code).count()
    #             restrictedip = v_obj.IPRestriction
                
    #             if not 'voucher_code' in request.POST:

    #                 if exp_date > today and v_obj.used < v_obj.times and \
    #                     v_obj.type.lower() == "invite" : 
       
    #                     if restrictedip == None:
    #                         v_obj.used = int(v_obj.used) + 1
    #                         v_obj.save()
    #                         if not actor.partner:
    #                             actor.partner = v_obj.partner
    #                             actor.save()
    #                     else:
    #                         if ipcount < restrictedip:    
    #                             v_obj.used = int(v_obj.used) + 1
    #                             v_obj.save()
    #                             if not actor.partner:
    #                                 actor.partner = v_obj.partner
    #                                 actor.save()
                
    #                     account.deposit(float(v_obj.amount), v_obj.currency)
                    
    #                     def createinvitecodeTransactionReference():
    #                         try:
    #                             return 'IC' + str(int(
    #                                 Transaction.objects.filter(
    #                                     reference__startswith='IC').order_by(
    #                                     '-reference')[0].reference[2:]) + 1)
    #                         except:
    #                             return 'IC20001001'

    #                     t_amount = CurrencyExchangeRate.Convert(v_obj.amount,
    #                         v_obj.currency, actor.currency)[0]                
    #                     InviteTransaction = Transaction()
    #                     InviteTransaction.reference = createinvitecodeTransactionReference()                    
    #                     InviteTransaction.actor = actor
    #                     InviteTransaction.amount = t_amount
    #                     InviteTransaction.currency = actor.currency
    #                     InviteTransaction.payment_method = 'Invite code'
    #                     InviteTransaction.payment_reference = invite_code
    #                     InviteTransaction.payment_message = 'Paid to account %s' % account
    #                     InviteTransaction.transaction_type = 'invite'
    #                     InviteTransaction.transaction_flag = 'paid'
    #                     InviteTransaction.UserIp = userip
    #                     InviteTransaction.created = helper.get_now()
    #                     InviteTransaction.transaction_date = helper.get_now()
    #                     InviteTransaction.save() 
                        
    #             elif 'voucher_code' in request.POST:      
                    
    #                 if exp_date > today and v_obj.used < v_obj.times and \
    #                     v_obj.type.lower() == "voucher" : 
       
    #                     if restrictedip == None:
    #                         v_obj.used = int(v_obj.used) + 1
    #                         v_obj.save()
    #                         if not actor.partner:
    #                             actor.partner = v_obj.partner
    #                             actor.save()
    #                     else:
    #                         if ipcount < restrictedip:    
    #                             v_obj.used = int(v_obj.used) + 1
    #                             v_obj.save()
    #                             if not actor.partner:
    #                                 actor.partner = v_obj.partner
    #                                 actor.save()
                
    #                     account.deposit(float(v_obj.amount), v_obj.currency)
                    
    #                     def createVouchercodeTransactionReference():
    #                         try:
    #                             return 'VC' + str(int(
    #                                 Transaction.objects.filter(
    #                                     reference__startswith='VC').order_by(
    #                                     '-reference')[0].reference[2:]) + 1)
    #                         except:
    #                             return 'VC20001001'

    #                     #----- Creating a Voucher Transaction -----
    #                     voucher_code = invite_code
    #                     t_amount = CurrencyExchangeRate.Convert(v_obj.amount,
    #                         v_obj.currency, actor.currency)[0]                
    #                     VoucherTransaction = Transaction()
    #                     VoucherTransaction.reference = createVouchercodeTransactionReference()
    #                     VoucherTransaction.actor = actor
    #                     VoucherTransaction.amount = t_amount
    #                     VoucherTransaction.currency = actor.currency
    #                     VoucherTransaction.payment_method = 'Voucher code'
    #                     VoucherTransaction.payment_reference = voucher_code
    #                     VoucherTransaction.payment_message = 'Paid to account %s' % account
    #                     VoucherTransaction.transaction_type = 'voucher'
    #                     VoucherTransaction.transaction_flag = 'paid'
    #                     VoucherTransaction.UserIp = userip
    #                     VoucherTransaction.created = helper.get_now()
    #                     VoucherTransaction.transaction_date = helper.get_now()
    #                     VoucherTransaction.save()

    #         except Voucher.DoesNotExist:
    #             v_obj = None
        
    #     try:
    #         send_templated_mail(
    #             template_name = 'welcome',
    #             subject = 'Welcome to Fixido.com',
    #             from_email = settings.DEFAULT_FROM_EMAIL,
    #             recipient_list = [email,],
    #             bcc = settings.INFO_EMAIL_BCC,
    #             context={
    #                      'actor': actor,
    #                      'current_site': current_site,
    #                      'confirmation_keyy': confirmation_keyy,
    #                      'email': email,
    #                      'password': pwd,
    #                      'version' : settings.STATIC_VERSION,
    #             },
    #         )
    #     except Exception, e:
    #         logger.error('Not sent welcome email (@create_new_user) %s' % e)
        
    #     user = authenticate(username=email, password=pwd)
    #     login(request, user)
        
    #     if 'fxapi_registration' in request.POST:
    #         response = HttpResponseRedirect('/apidocs/')
        
    #     elif 'register_in_autobuy' in request.POST:
    #         response = HttpResponseRedirect("/leads/" + selected_lead)
        
    #     elif 'addtobasket_popup_reg' in request.POST:
    #         return addToBasket(request)
        
    #     elif 'auto_buy_popup_reg' in request.POST:
    #         lead_id = request.POST.get('selected_lead2', 0)
    #         lead = Lead.objects.filter(id=lead_id)
    #         if lead:
    #             lead_price = lead[0].price_as(actor.currency)
    #             country, vat_number = actor.get_country_vat(account)
    #             vat_amt = logic.calculate_vat(lead_price, country, vat_number)
    #             balance_need = lead_price + vat_amt
    #         else: balance_need = 1
            
    #         redirect_path = request.POST['next']
    #         query_string = 'lowbalance=%d' % math.ceil(balance_need)
    #         query_string += '&leadid=%d' % int(lead_id)
    #         redirect_url = format_redirect_url(redirect_path, query_string)
    #         response = HttpResponseRedirect(redirect_url)
    #     else:
    #         response = HttpResponseRedirect("/dashboard/start/?user=1")
        
    #     set_email_cookie(response, email)
    #     return response
    return response