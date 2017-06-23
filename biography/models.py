from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	STATUS_CHOICES = (
			("MARRIED", "Married"),
			("SINGLE", "Single"),
			("COMPLICATED", "Complicated")
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	other_names = models.CharField(max_length=200)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	nationality = models.CharField(max_length=200)
	marital_status = models.CharField(max_length=11,
		                              choices=STATUS_CHOICES,
		                              default="SINGLE")

	def get_full_name(self):
		return self.first_name + ' ' + self.other_names + ' ' + self.last_name

	def __str__(self):
		return self.user.username


class Direct(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	phone_number = models.IntegerField()
	email = models.EmailField()
	website = models.URLField(max_length=200)
	github = models.URLField(max_length=200)

	def __str__(self):
		return self.user.username
