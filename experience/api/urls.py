from django.conf.urls import url
from .views import (
	ExperienceCreateAPIView,
	ExperienceListAPIView,
	ExperienceDetailAPIView,
	ExperienceUpdateAPIView,
	ExperienceDeleteAPIView
	)


urlpatterns = [
	url(r'^$', ExperienceListAPIView.as_view(), name="exp-list"),
    url(r'^create/$', ExperienceCreateAPIView.as_view(), name="exp-create"),
    url(r'^(?P<pk>\d+)/$', ExperienceDetailAPIView.as_view(), name="exp-detail"),
    url(r'^(?P<pk>\d+)/edit/$', ExperienceUpdateAPIView.as_view(), name="exp-update"),
    url(r'^(?P<pk>\d+)/delete/$', ExperienceDeleteAPIView.as_view(), name="exp-delete"),
]