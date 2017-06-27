from django.conf.urls import url
from .views import (
	SkillCreateAPIView,
	SkillListAPIView,
	SkillDetailAPIView,
	SkillUpdateAPIView,
	SkillDeleteAPIView
	)


urlpatterns = [
	url(r'^$', SkillListAPIView.as_view(), name="skill-list"),
    url(r'^create/$', SkillCreateAPIView.as_view(), name="skill-create"),
    url(r'^(?P<pk>\d+)/$', SkillDetailAPIView.as_view(), name="skill-detail"),
    url(r'^(?P<pk>\d+)/edit/$', SkillUpdateAPIView.as_view(), name="skill-update"),
    url(r'^(?P<pk>\d+)/delete/$', SkillDeleteAPIView.as_view(), name="skill-delete"),
]