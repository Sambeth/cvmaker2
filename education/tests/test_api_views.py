from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Education


class EducationAPITest(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create(username='phyll',
										email='phyll@gmail.com',
				                        is_active=True,
				                        is_superuser=True,
				                        is_staff=True)
		self.client.force_authenticate(user=self.user)

	def test_education_api_can_create(self):
		url = reverse('edu-api:edu-create')
		data = {'institution': 'UPSA', 'duration': '2012-2016',
				'certificate': 'WASSCE'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_education_api_can_get_detail(self):
		edu = Education.objects.create(user=self.user, institution='UPSA',
			                           duration='2012-2016', certificate='BECE')
		url = reverse('edu-api:edu-detail', kwargs={'pk': edu.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, edu)

	def test_eduaction_api_can_update(self):
		edu = Education.objects.create(user=self.user, institution='UPSA',
			                           duration='2012-2016', certificate='BECE')
		data = {'institution': 'KNUST', 'duration': '2012-2016',
				'certificate': 'WASSCE'}
		url = reverse('edu-api:edu-update', kwargs={'pk': edu.id})
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_education_api_can_delete(self):
		edu = Education.objects.create(user=self.user, institution='UPSA',
			                           duration='2012-2016', certificate='BECE')
		url = reverse('edu-api:edu-delete', kwargs={'pk': edu.id})
		response = self.client.delete(url, format='json', follow=True)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)