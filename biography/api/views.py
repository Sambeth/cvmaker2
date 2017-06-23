from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from .pagination import (
	ProfileLimitOffsetPagination, 
	ProfilePageNumberPagination
	)

from ..models import Profile, Direct

from .serializers import (
	ProfileListSerializer,
	ProfileDetailSerializer,
	ProfileCreateUpdateSerializer,
	DirectListSerializer,
	DirectDetailSerializer,
	DirectCreateUpdateSerializer,
	)


# profile model
class ProfileCreateAPIView(CreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProfileListAPIView(ListAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ["first_name", "last_name", "nationality", "marital_status"]
	pagination_class = ProfileLimitOffsetPagination


class ProfileDetailAPIView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileDetailSerializer


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileCreateUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class ProfileDeleteAPIView(DestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileDetailSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# direct model
class DirectCreateAPIView(CreateAPIView):
	queryset = Direct.objects.all()
	serializer_class = DirectCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class DirectListAPIView(ListAPIView):
	queryset = Direct.objects.all()
	serializer_class = DirectListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ["location"]
	pagination_class = ProfileLimitOffsetPagination


class DirectDetailAPIView(RetrieveAPIView):
	queryset = Direct.objects.all()
	serializer_class = DirectDetailSerializer


class DirectUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Direct.objects.all()
	serializer_class = DirectCreateUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class DirectDeleteAPIView(DestroyAPIView):
	queryset = Direct.objects.all()
	serializer_class = DirectDetailSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]