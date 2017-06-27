from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView,
	)

from .serializers import (
	SkillCreateUpdateSerializer,
	SkillListSerializer,
	SkillDetailSerializer)

from rest_framework.permissions import (
	IsAuthenticated,
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)

from .pagination import (
	SkillsLimitOffsetPagination,
	SkillsPageNumberPagination
	)

from .permissions import IsOwnerOrReadOnly

from ..models import Skill


class SkillListAPIView(ListAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillListSerializer
	permission_class = [IsAuthenticated]
	filter_backends = [SearchFilter, OrderingFilter]
	serach_fields = ['title', 'content']
	pagination_class = SkillsLimitOffsetPagination


class SkillCreateAPIView(CreateAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillCreateUpdateSerializer
	permission_class = [IsAuthenticated]

	def perform_create(self, serializer):
		return serializer.save(user=self.request.user)


class SkillDetailAPIView(RetrieveAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillDetailSerializer
	permission_class = [IsAuthenticated]


class SkillUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillCreateUpdateSerializer
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		return serializer.save(user=self.request.user)


class SkillDeleteAPIView(DestroyAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillDetailSerializer
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]