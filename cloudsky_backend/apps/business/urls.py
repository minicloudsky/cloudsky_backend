from django.conf.urls import url

from business import views

urlpatterns = [
    url(r'^get_data/$', views.GetDataView.as_view(), name='get_data'),
    url(r'^get_some_thing/$', views.GetSomeThingView.as_view(), name='get some things'),
]
