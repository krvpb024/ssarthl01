"""ssarthl01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.table_money_list, name='table_money_list'),
	url(r'(?P<pk>\d+)/$', views.table_money_detail, name='table_money_detail'),
	# url(r'^month_create/$', views.month_create, name='month_create'),
    url(r'^(?P<pk>\d+)/table_money_pay/$', views.table_money_pay, name='table_money_pay'),
    url(r'^(?P<pk>\d+)/extra_table_money_pay/$', views.extra_table_money_pay, name='extra_table_money_pay'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>\d+)/add_extra_table_money$',views.add_extra_table_money , name='add_extra_table_money'),
    url(r'^(?P<pk>\d+)/delete_extra_table_money_list$', views.delete_extra_table_money_list, name='delete_extra_table_money_list'),
]
