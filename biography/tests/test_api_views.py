from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Profile, Direct


class ProfileAPITestView(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create(username='phyll',
										email='phyll@gmail.com',
				                        is_active=True,
				                        is_superuser=True,
				                        is_staff=True)
		self.client.force_authenticate(user=self.user)

	def test_profile_api_can_create_a_bio(self):
		url = reverse('bio-api:profile-create')
		data = {'first_name': 'Kweku', 'last_name': 'Poku',
				'other_names': 'Boafo', 'date_of_birth': '1992-02-12',
				'nationality': 'Togolese', 'marital_status': 'MARRIED'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_profile_api_get_a_bio(self):
		p = Profile.objects.create(user=self.user, first_name='Phyllis',
			                       last_name='Boatemaah', other_names='Sambeth',
			                       date_of_birth='1992-12-30', nationality='Ghanaian',
			                       marital_status='Single')
		url = reverse('bio-api:profile-detail', kwargs={'pk': p.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, p)

	def test_profile_api_can_update_a_bio(self):
		p = Profile.objects.create(user=self.user, first_name='Phyllis',
			                       last_name='Boatemaah', other_names='Sambeth',
			                       date_of_birth='1992-12-30', nationality='Ghanaian',
			                       marital_status='Single')
		data = {'first_name': 'Kweku', 'last_name': 'Poku',
				'other_names': 'Boafi', 'date_of_birth': '1992-02-12',
				'nationality': 'Togolese', 'marital_status': 'COMPLICATED'}
		url = reverse('bio-api:profile-update', kwargs={'pk': p.id})
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_profile_api_can_delete_a_bio(self):
		p = Profile.objects.create(user=self.user, first_name='Phyllis',
			                       last_name='Boatemaah', other_names='Sambeth',
			                       date_of_birth='1992-12-30', nationality='Ghanaian',
			                       marital_status='Single')
		url = reverse('bio-api:profile-delete', kwargs={'pk': p.id})
		response = self.client.delete(url, format='json', follow=True)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class DirectAPITestView(APITestCase):

	def setUp(self):
		self.client = APIClient(enforce_csrf_checks=True)
		self.user = User.objects.create(username='phyll',
			                            email='phyll@gmail.com',
			                            is_active=True,
			                            is_superuser=True,
			                            is_staff=True)
		self.client.force_authenticate(user=self.user)

	def test_direct_api_can_a_bio(self):
		url = reverse('bio-api:direct-create')
		data = {'address': 'P. O. Box GP 21571', 'location': 'Christian Village',
				'phone_number': '0207388175', 'email': 'phyll@gmail.com',
				'website': 'http://google.com', 'github': 'http://github.com/Phyll'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_direct_api_can_get_a_bio(self):
		d = Direct.objects.create(user=self.user, address='P. O. Box GP 21571',
								  location='Christian Village', phone_number='0207388175',
								  email='phyll@gmail.com', website='http://google.com',
								  github='http://github.com/Phyll')
		url = reverse('bio-api:direct-detail', kwargs={'pk': d.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_direct_api_can_update_a_bio(self):
		d = Direct.objects.create(user=self.user, address='P. O. Box GP 21571',
								  location='Christian Village', phone_number='0207388175',
								  email='phyll@gmail.com', website='http://google.com',
								  github='http://github.com/Phyll')
		data = {'address': 'P. O. Box GP 21571', 'location': 'Christian Village',
				'phone_number': '0207388175', 'email': 'phyll@gmail.com',
				'website': 'http://google.com', 'github': 'http://github.com/Phyll'}
		url = reverse('bio-api:direct-update', kwargs={'pk': d.id})
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_direct_api_can_delete_a_bio(self):
		d = Direct.objects.create(user=self.user, address='P. O. Box GP 21571',
								  location='Christian Village', phone_number='0207388175',
								  email='phyll@gmail.com', website='http://google.com',
								  github='http://github.com/Phyll')
		url = reverse('bio-api:direct-delete', kwargs={'pk': d.id})
		response = self.client.delete(url, format='json', follow=True)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# address = models.CharField(max_length=200)
	# location = models.CharField(max_length=200)
	# phone_number = models.IntegerField().
	# email = models.EmailField()
	# website = models.URLField(max_length=200)
	# github = models.URLField(max_length=200)