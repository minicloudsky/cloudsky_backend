from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import get_authorization_header
from django.utils.deprecation import MiddlewareMixin
import time
from django.http import HttpResponseBadRequest

class TokenAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware for utilizing token based authentication.

    This is similar way as rest_framework's TokenAuthentication
    rest_framework.authtoken is required in settings.INSTALLED_APPS

    User should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a

    Will mark the user from token as t_user
        * avoid rewrite by SessionAuthenticationMiddleware
    """
    def _get_token(self, request):
        token = b""
        auth = get_authorization_header(request).split()
        if not auth or len(auth) != 1:
            return token
        try:
            return auth[0].decode()
        except UnicodeError:
            return token

    def process_request(self, request):
        # if hasattr(request, 'method') and request.method not in ['GET', 'POST', 'HEAD']:
        #     return HttpResponseBadRequest()
        t_key = self._get_token(request)
        if t_key:
            try:
                token = Token.objects.select_related('user').get(key=t_key)
                if token.user.is_active:
                    user = token.user
                    request.user = user
            except Token.DoesNotExist:
                pass

