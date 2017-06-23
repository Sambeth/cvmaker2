from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
	message = 'you must be the owner of this object'

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user == request.user
