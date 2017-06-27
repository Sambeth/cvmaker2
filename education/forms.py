# from django import forms
# from django.forms import inlineformset_factory
# from .models import Education
# from django.contrib.auth.models import User


# class EducationModelForm(forms.ModelForm):
# 	duration = forms.Charfield(widget=forms.TextInput(attrs={'placeholder': '2012-2016'}))

# 	class Meta:
# 		model = Education
# 		fields = ['institution', 'duration', 'certificate']


# EducationModelFormset = inlineformset_factory(User,
# 	                                          Education,
# 	                                          form=EducationModelForm,
# 	                                          max_num=5,
# 	                                          extra=1,
# 	                                          can_delete=True)