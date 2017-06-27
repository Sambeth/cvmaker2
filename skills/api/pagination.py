from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class SkillsLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10


class SkillsPageNumberPagination(PageNumberPagination):
	page_size = 2