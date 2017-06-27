from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class EducationLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10


class EducationPageNumberPagination(PageNumberPagination):
	page_size = 2