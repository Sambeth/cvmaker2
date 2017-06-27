from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comapny = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	activities = models.TextField(max_length=200)

	def __str__(self):
		return self.user.username