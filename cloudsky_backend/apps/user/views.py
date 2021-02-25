import logging

logger = logging.getLogger("django")
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.settings import api_settings

from cloudsky_backend.utils.pagination import StandardResultsSetPagination
from user import serializers
from user.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


class UserLoginView(APIView):
    """
    user login the system
    need username and password from formdata
    """

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserLoginView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_body = request.data
        username = form_body.get("username", "")
        password = form_body.get("password", "")
        if not username:
            return Response({
                "code": 400,
                "msg": "用户名不能为空!",
            })
        if not password:
            return Response({
                "code": 400,
                "msg": "密码不能为空!",
            })
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return Response({
                "code": 400,
                "msg": "用户不存在!",
            })
        if not user.check_password(password):
            return Response({
                "code": 400,
                "msg": "密码不正确!",
            })
        # sign token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # set_cache(user.id, )
        return Response({
            "code": 200,
            "msg": None,
            "data": {
                "username": user.username,
                "id": user.id,
                "token": token
            }
        })


class UserInfoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    pagination_class = StandardResultsSetPagination
    serializer_class = serializers.UserSerializer
    queryset = UserProfile.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            user = UserProfile.objects.get(id=pk)
        except UserProfile.DoesNotExist:
            return None
        return user

    def create(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializers(data=request.data,
                                                       context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer
        keyword = request.query_params.get("keyword", "")
        if keyword:
            queryset = UserProfile.objects.filter(username__contains=keyword).order_by('id')
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not instance:
            return Response({
                "code": 400,
                "msg": "修改的用户不存在"
            })
        serializer = serializers.UpdateUserSerialzer(instance, data=request.data,
                                                     partial=partial,
                                                     context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)


class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        id_datas = request.data.get("ids", [])
        if not id_datas:
            return Response({
                "code": 400,
                "msg": "缺少将删除的用户id！"
            })
        for o_id in id_datas:
            try:
                o_user = UserProfile.objects.get(id=o_id.get("id", 0))
            except UserProfile.DoesNotExist:
                return Response({
                    "code": 400,
                    "msg": "将要删除的用户不存在！"
                })
            o_user.is_active = False
            o_user.update_time = request.user.username
            o_user.save()
        return Response({
            "code": 200,
            "msg": None,
            "data": 1
        })


class UpdateUserPasswordView(APIView):
    """
    1: 修改别人密码，需要高权限
    2：修改自己密码，优先实现
    传入参数：
    password: 旧密码
    newpassword1： 新密码
    newassword2:  新密码

    校验：
    旧密码要验证是否输入正确
    新密码： 两次输入是否一致

    """

    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        post_data = request.data
        password = post_data.get('password', '')
        newpassword1 = post_data.get('newpassword1', '')
        newpassword2 = post_data.get('newpassword2', '')

        logger.debug("params: password=%s, newpassword1=%s, newpassword2=%s" % (password,
                                                                                newpassword1,
                                                                                newpassword2))
        if not all([password, newpassword1, newpassword2]):
            return Response({
                "code": 400,
                "msg": "参数不能为空!"
            })

        user = request.user

        # 验证密码是否正确
        if not user.check_password(password):
            return Response({
                "code": 400,
                "msg": "密码不正确!",
            })

        # 验证新密码是否一致
        if newpassword1 != newpassword2:
            return Response({
                "code": 400,
                "msg": "新密码输入不一致!"
            })

        ##更改密码
        user.set_password(newpassword1)
        user.save()

        return Response({
            "code": 200,
            "msg": "密码更改成功!",
            "data": 1
        })


class GetUserInfo(APIView):
    """通过token获取用户信息"""

    def get(self, request):
        user = request.user
        id = user.id
        name = user.username
        email = user.email
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        phone = user.phone
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            "id": id,
            "username": name,
            "email": email,
            "phone": phone,
            "token": token}
        )
