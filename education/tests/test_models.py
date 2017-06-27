from django.test import TestCase
from ..models import Education
from django.contrib.auth.models import User


class EducationTest(TestCase):

	def setUp(self):
		user = User.objects.create(username='phyll')
		education = Education.objects.create(user=user,
			                                 institution='KNUST',
			                                 duration='2012-2016',
			                                 certificate='WASSCE')

	def test_education_str_equal_to_username(self):
		user = User.objects.get(username='phyll')
		edu = Education.objects.get(user=user)
		self.assertEqual(str(edu), edu.user.username)