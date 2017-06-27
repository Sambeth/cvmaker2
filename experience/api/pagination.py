from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class ExperienceLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10


class ExperiencePageNumberPagination(PageNumberPagination):
	page_size = 2