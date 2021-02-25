from django.conf.urls import url
from . import views

urlpatterns = [
    # find all
    url(r'^get_log/$', views.LogView.as_view(), name="获取日志接口"),
]
