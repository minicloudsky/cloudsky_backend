"""cloudsky_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from user import views

urlpatterns = [
    # login view
    path('login/', views.UserLoginView.as_view(), name="用户登录"),
    path("get/", views.UserInfoViewSet.as_view({'get': 'list'}), name="获取所有用户信息"),
    path("create/", views.UserInfoViewSet.as_view({'post': 'create'}), name="新建用户"),
    path("delete/", views.DeleteUserView.as_view(), name="删除用户的接口"),
    re_path("update/(?P<pk>\d+)/$", views.UserInfoViewSet.as_view({'post': 'update'}), name="更新用户信息的接口"),
    path("update_password/", views.UpdateUserPasswordView.as_view(), name="更改用户密码的接口"),
    path("user_info/", views.GetUserInfo.as_view(), name="通过token获取用户信息"),
]
