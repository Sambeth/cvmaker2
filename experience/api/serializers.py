from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from ..models import Experience

from accounts.api.serializers import UserDetailSerializer


class ExperienceListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='exp-api:exp-detail',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Experience
		fields = [
			'url',
			'id',
			'user',
			'comapny',
			'duration',
			'role',
			'activities'
		]


class ExperienceCreateUpdateSerializer(ModelSerializer):

	class Meta:
		model = Experience
		fields = [
			'comapny',
			'duration',
			'role',
			'activities'
		]


class ExperienceDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='exp-api:exp-delete',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Experience
		fields = [
			'id',
			'user',
			'comapny',
			'duration',
			'role',
			'activities',
			'delete_url'
		]