from rest_framework import permissions

class IsuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow user of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.email== request.user
