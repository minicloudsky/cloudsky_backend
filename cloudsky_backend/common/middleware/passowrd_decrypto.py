from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import get_authorization_header
from django.utils.deprecation import MiddlewareMixin
import time
from common.utils import PrpCrypt
import logging
logger = logging.getLogger("project")


class DecryptoMiddleware(MiddlewareMixin):
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
        password_dict = {}
        for key, value in request.POST.items():
            if key.find("password") >-1 and value:
                password_dict[key] = value
        if password_dict:
            try:
                login_key = request.session['login_key']
                login_iv = request.session['login_iv']
                pc = PrpCrypt(login_key, login_iv)  # 初始化密钥
                postdata = request.POST.copy()
                #request.POST['password1'] = "1234"
                for k, v in password_dict.items():
                    decrypt_v = pc.decrypt(v)
                    password_dict[k] = decrypt_v or v
                    postdata[k] = decrypt_v or v
                request.POST = postdata
                request._post = postdata
                #request._body = simplejson.dumps(postdata)
            except Exception as e:
                logger.info(str(e))
