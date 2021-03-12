from cloudsky_backend.common.common_serializers import BaseSerializer
from log.models import Log


class LogSerializer(BaseSerializer):
    class Meta:
        model = Log
        fields = "__all__"
