from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from ..models import Profile, Direct

from accounts.api.serializers import UserDetailSerializer

class ProfileCreateUpdateSerializer(ModelSerializer):

	class Meta:
		model = Profile
		fields = [
			'first_name',
			'last_name',
			'other_names',
			'date_of_birth',
			'nationality',
			'marital_status'
		]


class ProfileListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='bio-api:profile-detail',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Profile
		fields = [
			'url',
			'id',
			'user',
			'first_name',
			'last_name',
			'other_names',
			'date_of_birth',
			'nationality',
			'marital_status',
		]


class ProfileDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='bio-api:profile-delete',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Profile
		fields = [
			'id',
			'user',
			'first_name',
			'last_name',
			'other_names',
			'date_of_birth',
			'nationality',
			'marital_status',
			'delete_url'
		]


class DirectCreateUpdateSerializer(ModelSerializer):

	class Meta:
		model = Direct
		fields = [
			'address',
			'location',
			'phone_number',
			'email',
			'website',
			'github',
		]


class DirectListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='bio-api:direct-detail',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Direct
		fields = [
			'url',
			'id',
			'user',
			'address',
			'location',
			'phone_number',
			'email',
			'website',
			'github',
		]


class DirectDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='bio-api:direct-delete',
		lookup_field='pk'
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Direct
		fields = [
			'id',
			'user',
			'address',
			'location',
			'phone_number',
			'email',
			'website',
			'github',
			'delete_url'
		]