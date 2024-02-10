from rest_framework.permission import Basepermission,SAFE_METHODS


class IsAuthenticatedOrReadOnly(Basepermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (request.user and request.user.is_authenticatesd)