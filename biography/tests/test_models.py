from django.test import TestCase
from ..models import Profile, Direct
from django.contrib.auth.models import User


class ProfileTest(TestCase):

	def setUp(self):
		user = User.objects.create(username='phyll')
		Profile.objects.create(user=user, first_name='Phyllis',
			                   last_name='Boatemaah', other_names='Sambeth',
			                   date_of_birth='1992-12-30', nationality='Ghanaian',
			                   marital_status='Single')

	def test_profile_full_name(self):
		user = User.objects.get(username='phyll')
		p = Profile.objects.get(user=user)
		self.assertEqual(p.get_full_name(), 'Phyllis Sambeth Boatemaah')

	def test_profile_str_equal_to_username(self):
		user = User.objects.get(username='phyll')
		p = Profile.objects.get(user=user)
		self.assertEqual(str(p), p.user.username)


class DirectTest(TestCase):

	def setUp(self):
		user = User.objects.create(username='phyll')
		Direct.objects.create(user=user, address="P. O. Box GP 419",
			                  location='Accra', phone_number='020415994')

	def test_direct_str_equal_to_username(self):
		user = User.objects.get(username='phyll')
		d = Direct.objects.get(user=user)
		self.assertEqual(str(d), d.user.username)