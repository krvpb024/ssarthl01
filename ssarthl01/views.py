from django.shortcuts import render, render_to_response
from tablemoney.models import TableMoney, Month
from userprofile.models import UserProfile
import datetime


# Create your views here.

def index(request):
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