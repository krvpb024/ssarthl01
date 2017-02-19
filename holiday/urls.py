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
    # url(r'^holiday_create$',views.holiday_create , name='holiday_create'),
	# url(r'^$',views.holiday_list , name='holiday_list'),
    # url(r'(?P<pk>\d+)/$',views.holiday_detail , name='holiday_detail'),
    # url(r'(?P<month_pk>\d+)/edit_holiday$',views.edit_holiday , name='edit_holiday'),


    url(r'^holiday_month_from_docx$',views.holiday_month_from_docx , name='holiday_month_from_docx'),
    url(r'^holiday_list_from_docx$',views.holiday_list_from_docx , name='holiday_list_from_docx'),
    url(r'^holiday_detail_from_docx/(?P<pk>\d+)/$',views.holiday_detail_from_docx , name='holiday_detail_from_docx'),
]
