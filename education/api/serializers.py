from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from ..models import Education


class EducationCreateUpdateSerializer(ModelSerializer):

	class Meta:
		model = Education
		fields = ['institution',
			      'duration',
			      'certificate']


class EducationListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='edu-api:edu-detail',
		lookup_field='pk'
		)
	user = SerializerMethodField()

	class Meta:
		model = Education
		fields = ['url',
				  'user',
				  'id',
				  'institution',
			      'duration',
			      'certificate']

	def get_user(self, obj):
		return str(obj.user.username)


class EducationDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='edu-api:edu-delete',
		lookup_field='pk'
		)
	user = SerializerMethodField()

	class Meta:
		model = Education
		fields = ['user',
		          'id',
				  'institution',
			      'duration',
			      'certificate',
			      'delete_url']

	def get_user(self, obj):
		return str(obj.user.username)