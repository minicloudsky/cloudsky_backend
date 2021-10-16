import logging

# from django.core.cache import cache
# from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cloudsky_backend.common.db import fetchall_to_dict

# cache = get_redis_connection("default")
from cloudsky_backend.common.user_permissions import permission_required

logger = logging.getLogger("cloudsky_backend_project")


# Create your views here.
class GetDataView(ListAPIView):
    permission_classes = [IsAuthenticated]

    @permission_required('admin')
    def get(self, request, *args, **kwargs):
        keyword = request.query_params.get('keyword') or ''
        page = request.query_params.get('page') or 1
        page_size = request.query_params.get('page_size') or 5
        page = int(page)
        page_size = int(page_size)
        metadata = []
        if metadata:
            return Response(data=metadata, status=status.HTTP_200_OK)


class GetSomeThingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query_sql = """
        
        """
        data = fetchall_to_dict(query_sql, db='')
        return Response(data={'data': data, 'msg': 'ok', 'code': 200},
                        status=status.HTTP_200_OK)
