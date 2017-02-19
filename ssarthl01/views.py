from django.shortcuts import render, render_to_response, HttpResponseRedirect
from tablemoney.models import TableMoney, Month
from userprofile.models import UserProfile
from django.contrib.auth import get_user_model, login, logout
from .forms import UserLoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from ssarthl01.settings import BASE_DIR, MEDIA_ROOT

User = get_user_model()

# Create your views here.


def index(request):
	print(BASE_DIR)
	members = UserProfile.members.all().exclude(number=1)
	substitutes = UserProfile.substitutes.all()
	try:
		captain = UserProfile.members.get(number=1)
	except UserProfile.DoesNotExist:
		captain = ''


	now = datetime.datetime.now().year


	context = {
		'members':members,
		'substitutes':substitutes,
		'captain':captain,
		'now':now,
	}



	return render(request, 'index.html', context)


def user_login(request, *args, **kwargs):

	form = UserLoginForm()

	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			user_obj = User.objects.get(username__iexact=username)
			login(request, user_obj)
			return HttpResponseRedirect(reverse(index))
	return render(request, "login.html", {"form":form})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse(user_login))
