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
	url(r'^month_create/$', views.month_create, name='month_create'),
	url(r'^(?P<pk>\d+)/edit_work_day/$', views.edit_work_day, name='edit_work_day'),
    url(r'^(?P<pk>\d+)/table_money_pay/$', views.table_money_pay, name='table_money_pay'),
]
