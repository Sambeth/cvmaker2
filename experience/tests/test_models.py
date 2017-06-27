from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Experience


class ExperienceTest(TestCase):

	def setUp(self):
		user = User.objects.create(username='phyll')
		experience = Experience.objects.create(user=user,
			                                 comapny='KNUST',
			                                 duration='2012-2016',
			                                 role='office-clerk',
			                                 activities='cash receipts')

	def test_experience_str_equal_to_username(self):
		user = User.objects.get(username='phyll')
		exp = Experience.objects.get(user=user)
		self.assertEqual(str(exp), exp.user.username)