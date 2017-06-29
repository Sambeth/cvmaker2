from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AccountsTestAPIView(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create_user(username='phyll',
										email='phyll@gmail.com',
										password='realstuff23')
		self.client.force_authenticate(user=self.user)

	def test_user_can_register(self):
		url = reverse('users-api:register')
		data = {'username': 'sam', 'email': 'sam@gmail.com',
				'email2': 'sam@gmail.com', 'password':'realstuff23'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_user_can_login(self):
		data = {'username':'phyll',
				'password':'realstuff23'}
		url = reverse('users-api:login')
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)