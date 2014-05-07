from registration.forms import RegistrationForm
from django import forms
from waitlisty.models import Child, Family, Parent
from django.contrib.admin import widgets
 
class ParentForm(forms.ModelForm):
	class Meta:
                model = Parent
                exclude = ['created_by']
class ProfileForm(RegistrationForm):
	class Meta:
		model = Family
		
class ChildForm(forms.ModelForm):
	class Meta:
		model = Child
		exclude = ('created_by')
