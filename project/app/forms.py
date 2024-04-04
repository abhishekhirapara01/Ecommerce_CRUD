from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Mobile,Company

class UserCreateForm(UserCreationForm):
  def __init__(self, *args, **kwargs) :
    super(UserCreateForm,self).__init__(*args, **kwargs)
    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None
      self.fields[fieldname].widget.attrs.update({'class':'form-control'})


class MobileForm(forms.ModelForm):
   class Meta:
       model=Mobile
       fields="__all__"

class CompanyForm(forms.ModelForm):
   class Meta:
       model=Company
       fields="__all__"