from django.conf.urls import url
from .views import (
	EducationCreateAPIView,
	EducationListAPIView,
	EducationDetailAPIView,
	EducationUpdateAPIView,
	EducationDeleteAPIView
	)


urlpatterns = [
	url(r'^$', EducationListAPIView.as_view(), name="edu-list"),
    url(r'^create/$', EducationCreateAPIView.as_view(), name="edu-create"),
    url(r'^(?P<pk>\d+)/$', EducationDetailAPIView.as_view(), name="edu-detail"),
    url(r'^(?P<pk>\d+)/edit/$', EducationUpdateAPIView.as_view(), name="edu-update"),
    url(r'^(?P<pk>\d+)/delete/$', EducationDeleteAPIView.as_view(), name="edu-delete"),
]