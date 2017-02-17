from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^zhudi$',views.zhudi_table_list , name='zhudi_table_list'),
    url(r'zhudi/(?P<pk>\d+)/$',views.zhudi_table_detail , name='zhudi_table_detail'),
    url(r'zhudi/create/$',views.zhudi_table_create , name='zhudi_table_create'),
    url(r'zhudi/(?P<pk>\d+)/delete/$',views.zhudi_table_delete , name='zhudi_table_delete'),
    url(r'zhudi/create_session/$',views.zhudi_session_create , name='zhudi_session_create'),
    url(r'zhudi/delete_session/(?P<pk>\d+)$',views.zhudi_session_delete , name='zhudi_session_delete'),
	url(r'^zuxun$',views.zuxun_table_list , name='zuxun_table_list'),
	url(r'zuxun/(?P<pk>\d+)/$',views.zuxun_table_detail , name='zuxun_table_detail'),
	url(r'zuxun/create/$',views.zuxun_table_create , name='zuxun_table_create'),
	url(r'zuxun/(?P<pk>\d+)/delete/$',views.zuxun_table_delete , name='zuxun_table_delete'),
	url(r'zuxun/create_session/$',views.zuxun_session_create , name='zuxun_session_create'),
	url(r'zuxun/delete_session/(?P<pk>\d+)$',views.zuxun_session_delete , name='zuxun_session_delete'),

]