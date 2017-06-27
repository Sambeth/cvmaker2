from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	IsAuthenticated,
	)

from .permissions import IsOwnerOrReadOnly

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)

from .pagination import (
	EducationLimitOffsetPagination, 
	EducationPageNumberPagination
	)

from .serializers import (
	EducationCreateUpdateSerializer,
	EducationListSerializer,
	EducationDetailSerializer
	)

from ..models import Education


class EducationCreateAPIView(CreateAPIView):
	queryset = Education.objects.all()
	serializer_class = EducationCreateUpdateSerializer
	permission_class = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class EducationListAPIView(ListAPIView):
	queryset = Education.objects.all()
	serializer_class = EducationListSerializer
	permission_class = [IsAuthenticated]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['institution', 'certificate']
	pagination_class = EducationLimitOffsetPagination


class EducationDetailAPIView(RetrieveAPIView):
	queryset = Education.objects.all()
	serializer_class = EducationDetailSerializer


class EducationUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Education.objects.all()
	serializer_class = EducationCreateUpdateSerializer
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class EducationDeleteAPIView(DestroyAPIView):
	queryset = Education.objects.all()
	serializer_class = EducationDetailAPIView
	permission_class = [IsAuthenticated, IsOwnerOrReadOnly]