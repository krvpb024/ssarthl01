from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^profile_list$', views.profile_list, name='profile_list'),
	url(r'^profile_delete_list$', views.profile_delete_list, name='profile_delete_list'),
	url(r'^create_colleague$', views.create_colleague, name='create_colleague'),
	url(r'^edit_member_number$', views.edit_member_number, name='edit_member_number'),
	url(r'^edit_substitute_number$', views.edit_substitute_number, name='edit_substitute_number'),
	url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
]

