from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from ..models import Skill


class SkillListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='skill-api:skill-detail',
		lookup_field='pk',
		)
	user = SerializerMethodField()

	class Meta:
		model = Skill
		fields = ['url',
				  'id',
				  'user',
				  'title',
				  'content']

	def get_user(self, obj):
		return str(obj.user.username)


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
	user = SerializerMethodField()

	class Meta:
		model = Skill
		fields = ['id',
				  'user',
				  'title',
				  'content',
				  'delete_url']

	def get_user(self, obj):
		return str(obj.user.username)


