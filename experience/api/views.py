from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)

from .serializers import (
	ExperienceListSerializer,
	ExperienceCreateUpdateSerializer,
	ExperienceDetailSerializer
	)
from .pagination import (
	ExperienceLimitOffsetPagination,
	ExperiencePageNumberPagination
	)

from .permissions import IsOwnerOrReadOnly

from ..models import Experience


class ExperienceListAPIView(ListAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceListSerializer
	permission_class = [IsAuthenticated]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['comapny', 'role', 'activities']
	pagination_class = ExperienceLimitOffsetPagination


class ExperienceCreateAPIView(CreateAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceCreateUpdateSerializer
	permission_class = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ExperienceDetailAPIView(RetrieveAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceDetailSerializer
	permission_class = [IsAuthenticated]


class ExperienceUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceCreateUpdateSerializer
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ExperienceDeleteAPIView(DestroyAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceDetailSerializer
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]