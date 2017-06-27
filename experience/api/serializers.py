from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from ..models import Experience


class ExperienceListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='exp-api:exp-detail',
		lookup_field='pk'
		)
	user = SerializerMethodField()

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

	def get_user(self, obj):
		return str(obj.user.username)


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
	user = SerializerMethodField()

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

	def get_user(self, obj):
		return str(obj.user.username)