from rest_framework import permissions

class EhSUperUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True