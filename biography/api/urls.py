from django.conf.urls import url
from .views import (
	ProfileCreateAPIView,
	ProfileListAPIView,
	ProfileDetailAPIView,
	ProfileUpdateAPIView,
	ProfileDeleteAPIView,
	DirectCreateAPIView,
	DirectListAPIView,
	DirectDetailAPIView,
	DirectUpdateAPIView,
	DirectDeleteAPIView
	)


urlpatterns = [
    url(r'^$', ProfileListAPIView.as_view(), name="profile-list"),
    url(r'^create/$', ProfileCreateAPIView.as_view(), name="profile-create"),
    url(r'^(?P<pk>\d+)/$', ProfileDetailAPIView.as_view(), name="profile-detail"),
    url(r'^(?P<pk>\d+)/edit/$', ProfileUpdateAPIView.as_view(), name="profile-update"),
    url(r'^(?P<pk>\d+)/delete/$', ProfileDeleteAPIView.as_view(), name="profile-delete"),
    url(r'^direct/$', DirectListAPIView.as_view(), name="direct-list"),
    url(r'^direct/create/$', DirectCreateAPIView.as_view(), name="direct-create"),
    url(r'^direct/(?P<pk>\d+)/$', DirectDetailAPIView.as_view(), name="direct-detail"),
    url(r'^direct/(?P<pk>\d+)/edit/$', DirectUpdateAPIView.as_view(), name="direct-update"),
    url(r'^direct/(?P<pk>\d+)/delete/$', DirectDeleteAPIView.as_view(), name="direct-delete"),
]