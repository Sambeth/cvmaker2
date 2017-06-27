from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.user.username