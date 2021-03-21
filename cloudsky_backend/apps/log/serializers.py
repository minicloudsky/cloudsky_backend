from cloudsky_backend.common.common_serializers import BaseSerializer
from log.models import ApiLog


class LogSerializer(BaseSerializer):
    class Meta:
        model = ApiLog
        fields = "__all__"
