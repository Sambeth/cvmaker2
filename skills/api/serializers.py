from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from ..models import Skill

from accounts.api.serializers import UserDetailSerializer


class SkillListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='skill-api:skill-detail',
		lookup_field='pk',
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Skill
		fields = ['url',
				  'id',
				  'user',
				  'title',
				  'content']


class SkillCreateUpdateSerializer(ModelSerializer):

	class Meta:
		model = Skill
		fields = ['title',
		          'content']


class SkillDetailSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='skill-api:skill-delete',
		lookup_field='pk',
		)
	user = UserDetailSerializer(read_only=True)

	class Meta:
		model = Skill
		fields = ['id',
				  'user',
				  'title',
				  'content',
				  'delete_url']


