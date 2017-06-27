from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Education(models.Model):
	STATUS_CHOICES = (
			("BECE", "BECE"),
			("WASSCE", "WASSCE"),
			("BSC. ACCOUNTING", "BSC. ACCOUNTING")
		)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	institution = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	certificate = models.CharField(max_length=200,
		                          choices=STATUS_CHOICES,
		                          default='BECE')

	def __str__(self):
		return self.user.username
