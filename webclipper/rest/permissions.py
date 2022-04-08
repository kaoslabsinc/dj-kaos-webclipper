from rest_framework.permissions import IsAdminUser

from ..models import WebClip


class WebClipPermissions(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj: WebClip):
        default_perm = super(WebClipPermissions, self).has_object_permission(request, view, obj)
        return default_perm or request.user == obj.owner


__all__ = [
    'WebClipPermissions',
]
