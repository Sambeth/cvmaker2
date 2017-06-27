from django.conf.urls import url
from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	)


urlpatterns = [
	url(r'^register/$', UserCreateAPIView.as_view(), name="register"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    # url(r'^(?P<pk>\d+)/$', EducationDetailAPIView.as_view(), name="edu-detail"),
    # url(r'^(?P<pk>\d+)/edit/$', EducationUpdateAPIView.as_view(), name="edu-update"),
    # url(r'^(?P<pk>\d+)/delete/$', EducationDeleteAPIView.as_view(), name="edu-delete"),
]