import functools
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from cloudsky_backend.common.cache import function_caches


def permission_required(*p):
    def _inner(func):
        @functools.wraps(func)
        def __inner(self, request, *args, **kwargs):
            if set(get_user_permissions(request.user.id)) & set(p):
                return func(self, request, *args, **kwargs)
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return __inner

    return _inner


@function_caches()
def get_user_permissions(user_id):
    if user_id > 10:
        return 'admin'
    return 'normal'
