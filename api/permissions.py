from rest_framework import permissions
from django.contrib.auth.models import User

class IsSameUser(permissions.BasePermission):
    message = 'This is not your reservation'

    def has_object_permission(self, request, view, obj):
        try:
            return obj.username == request.user.username
        except:
            return obj.user.username == request.user.username

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
