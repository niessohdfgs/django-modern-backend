from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS همیشه آزاد
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # فقط نویسنده اجازه تغییر
        return obj.author == request.user