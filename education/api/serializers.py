from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from ..models import Education

from accounts.api.serializers import UserDetailSerializer


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
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Education
		fields = ['url',
				  'user',
				  'id',
				  'institution',
			      'duration',
			      'certificate']


class EducationDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='edu-api:edu-delete',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Education
		fields = ['user',
		          'id',
				  'institution',
			      'duration',
			      'certificate',
			      'delete_url']