from django.contrib import admin
from django.db import models
from .models import Profile, Direct
from django import forms
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.DateField: {'widget': forms.DateInput},
    }

	# class Meta:
	# 	model = Profile
	# 	widgets = {
	# 		'date_of_birth': forms.Date
	# 	}



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Direct)