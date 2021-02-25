from django.conf.urls import url

from user import views

urlpatterns = [
    # login view
    url(r'^login/$', views.UserLoginView.as_view(), name="用户登录"),
    url(r"^get/$", views.UserInfoViewSet.as_view({'get': 'list'}), name="获取所有用户信息"),
    url(r"^create/$", views.UserInfoViewSet.as_view({'post': 'create'}), name="新建用户"),
    url(r"^delete/$", views.DeleteUserView.as_view(), name="删除用户的接口"),
    url(r"^update/(?P<pk>\d+)/$", views.UserInfoViewSet.as_view({'post': 'update'}), name="更新用户信息的接口"),
    url(r"^update_password/", views.UpdateUserPasswordView.as_view(), name="更改用户密码的接口"),
    url(r"^user_info/", views.GetUserInfo.as_view(), name="通过token获取用户信息"),

]
