from rest_framework.permissions import BasePermission


class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.author
