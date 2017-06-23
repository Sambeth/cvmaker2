from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class ProfileLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10


class ProfilePageNumberPagination(PageNumberPagination):
	page_size = 2