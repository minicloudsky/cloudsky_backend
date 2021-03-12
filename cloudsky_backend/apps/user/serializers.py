import re
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from cloudsky_backend.common.common_serializers import BaseSerializer
from user.models import UserProfile


class BaseUserSerialzer(serializers.ModelSerializer):
    def validate_mobile(self, value):
        if not value:
            return value
        if re.match(r"^1[3456789]\d{9}$", value):
            return value
        raise serializers.ValidationError("手机号格式不正确！")


class CreateUserSerializers(BaseUserSerialzer):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "password", "email", "phone",)
        extra_kwargs = {
            "username": {'min_length': 6, },
            "id": {"read_only": True},
            "password": {
                "write_only": True,
                "required": False
            }
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        user_dict = {"username": validated_data["username"],
                     "email": validated_data.get("email", ""),
                     "phone": validated_data.get("phone", "")}
        if password:
            user_dict['password'] = password
        user = UserProfile.objects.create_user(**user_dict)
        user.createBy = self.context["request"].user.username
        user.save()
        return user


class UpdateUserSerialzer(BaseSerializer):
    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = ("create_by", "create_time", "update_time", "password", "update_by")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "first_name", "last_name", "email",
                  "sex", "phone", "adress", "create_time", "update_time"]
