from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Experience


class ExperienceAPITestView(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create(username='phyll',
										email='phyll@gmail.com',
				                        is_active=True,
				                        is_superuser=True,
				                        is_staff=True)
		self.client.force_authenticate(user=self.user)

	def test_experience_api_can_create(self):
		url = reverse('exp-api:exp-create')
		data = {'comapny': 'MEST', 'duration': '2012-2016',
				'role': 'full stack web developer', 'activities':'I develop web apps'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_experience_api_can_get(self):
		exp = Experience.objects.create(user=self.user, comapny='UPSA',
			                           duration='2012-2016', role='BECE',
			                           activities='I wrote the BECE')
		url = reverse('exp-api:exp-detail', kwargs={'pk': exp.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, exp)

	def test_experience_api_can_update(self):
		exp = Experience.objects.create(user=self.user, comapny='UPSA',
			                           duration='2012-2016', role='BECE',
			                           activities='I wrote the BECE')
		data = {'comapny': 'MEST', 'duration': '2012-2016',
				'role': 'full stack web developer', 'activities':'I develop web apps'}
		url = reverse('exp-api:exp-update', kwargs={'pk': exp.id})
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_experience_api_can_delete(self):
		exp = Experience.objects.create(user=self.user, comapny='UPSA',
			                           duration='2012-2016', role='BECE',
			                           activities='I wrote the BECE')
		url = reverse('exp-api:exp-delete', kwargs={'pk': exp.id})
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

