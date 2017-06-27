from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ..models import Skill
from django.urls import reverse
from django.contrib.auth.models import User


class SkillTestAPIVIew(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create(username='phyll',
										email='phyll@gmail.com',
				                        is_active=True,
				                        is_superuser=True,
				                        is_staff=True)
		self.client.force_authenticate(user=self.user)

	def test_skill_api_can_create(self):
		url = reverse('skill-api:skill-create')
		data = {'title': 'web Skills', 'content': 'HTML5 & CSS3'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_skill_api_can_get(self):
		skill = Skill.objects.create(user=self.user, title='Personal Skills',
			                          content='Reading')
		url = reverse('skill-api:skill-detail', kwargs={'pk': skill.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, skill)

	def test_skill_api_can_update(self):
		skill = Skill.objects.create(user=self.user, title='Personal Skills',
			                          content='Reading')
		data = {'title': 'web Skills', 'content': 'HTML5 & CSS3'}
		url = reverse('skill-api:skill-update', kwargs={'pk': skill.id})
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_skill_api_can_delete(self):
		skill = Skill.objects.create(user=self.user, title='Personal Skills',
			                          content='Reading')
		url = reverse('skill-api:skill-delete', kwargs={'pk': skill.id})
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)