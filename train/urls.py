from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.zhudi_table_list , name='zhudi_table_list'),
    url(r'(?P<pk>\d+)/$',views.zhudi_table_detail , name='zhudi_table_detail'),
    url(r'create/$',views.zhudi_table_create , name='zhudi_table_create'),

]
