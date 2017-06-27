from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Skill


class SkillTest(TestCase):

	def setUp(self):
		self.user = User.objects.create(username='phyll')
		self.skill = Skill.objects.create(user=self.user,
			                              title='Technical Skills',
			                              content='Wed Development')

	def test_skill_str_eqaul_to_username(self):
		self.user = User.objects.get(username=self.user)
		self.skill = Skill.objects.get(user=self.user)
		self.assertEqual(str(self.skill), self.skill.user.username)