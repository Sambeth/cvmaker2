from django import forms
from .models import Profile, Direct


class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'other_names',
			      'date_of_birth', 'nationality', 'marital_status')


class DirectForm(forms.ModelForm):

	class Meta:
		model = Direct
		fields = ('address', 'location', 'phone_number', 'email'
			      'website', 'github')
