from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy, ugettext as _ 

from actors.models import ActorCampaignEmailStatistics,Note

actor_obj = User.objects.filter(is_superuser = 1)
actor_list = []
for i in actor_obj:
    actor_list.append((str(i.email),str(i.email)))
    
actor_tuple = tuple(actor_list)    

class ActorCampaignEmailStatisticsForm( forms.ModelForm ):
    emailcampaignurl = forms.CharField( 
        label = _('Email Campaign URL'),
        widget = forms.Textarea(
            attrs = {'rows': 6, 'cols': 60, 'readonly': True}
        ),
        required = False,
    )
    
    class Meta:
        model = ActorCampaignEmailStatistics
        
        
        
class AdminNoteForm(forms.ModelForm):
    admin_note_user = forms.ChoiceField( 
        widget = forms.Select(),
        required = False,
        choices = actor_tuple,
    )
    
    class Meta:
        model = Note        


class UserForm(forms.ModelForm):
    
    username = forms.RegexField(
        max_length=75, 
        regex=r'^[\w.@+-]+$',
        help_text='Required. 75 characters or fewer. Letters, digits and @/./+/-/_ only.',
    )
    
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))
    class Meta:
        model = User

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


User._meta.get_field('username').max_length = 75
User._meta.get_field('username').validators[0].limit_value = 75
UserAdmin.form.base_fields['username'].max_length = 75
UserAdmin.form.base_fields['username'].validators[0].limit_value = 75