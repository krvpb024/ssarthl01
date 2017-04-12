from django.shortcuts import render, render_to_response, HttpResponseRedirect
from tablemoney.models import TableMoney, Month
from userprofile.models import UserProfile
from django.contrib.auth import get_user_model, login, logout
from .forms import UserLoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime, re, json
from ssarthl01.settings import BASE_DIR, MEDIA_ROOT
from holiday.models import HolidayFromDocx

User = get_user_model()

# Create your views here.


def index(request):
	members = UserProfile.members.all()
	substitutes = UserProfile.substitutes.all()

	def get_holiday(date):
		year = date.strftime("%Y")
		month = date.strftime("%m")
		date = date.strftime("%d")

		year = str(int(year) - 1911)
		if re.match(r'0\d{1}', month):
			month = month.replace("0", "")
		date = int(date) -1

		year_month = year + month
		member_duty = []
		substitutes_duty = []



		holidays = HolidayFromDocx.objects.filter(identify=year_month)
		for holiday in holidays:
			dict_holiday = json.loads(holiday.date)
			if not dict_holiday[date]:
				if holiday.name in [x for x in members]:
					member_duty.append(holiday.name.name)
				else:
					substitutes_duty.append(holiday.name.name)

		if "張力家" in member_duty:
			member_duty.remove("張力家")
			supervisor = "張力家"
		elif "陳柏瑞" in member_duty:
			member_duty.remove("陳柏瑞")
			supervisor = "陳柏瑞"
		elif "游皓中" in member_dufty:
			member_duty.remove("游皓中")
			supervisor = "游皓中"
		else:
			supervisor = ""
		return member_duty, substitutes_duty, supervisor


	today_member_duty, today_substitutes_duty, today_supervisor = get_holiday(datetime.datetime.now())
	tomorrow_member_duty, tomorrow_substitutes_duty, tomorrow_supervisor = get_holiday(datetime.date.today() + datetime.timedelta(days=1))

	day_off = []
	back = []

	for member in members:
		if member.name in today_member_duty or member.name == today_supervisor:
			print("第一",member)
			if member.name not in tomorrow_member_duty and member.name != tomorrow_supervisor:
				print("第二",member)
				day_off.append(member.name)
		elif member.name not in today_member_duty and member.name != today_supervisor:
			print("第三", member)
			if member.name in tomorrow_member_duty or member.name == tomorrow_supervisor:
				print("第四",member)
				back.append(member.name)


	for substitute in substitutes:
		if substitute.name in today_member_duty:
			if substitute.name not in tomorrow_substitutes_duty:
				print(substitute)
				day_off.append(substitute.name)
		elif substitute.name not in today_substitutes_duty:
			if substitute.name in tomorrow_substitutes_duty:
				print(substitute)
				back.append(substitute.name)

	print("day_off",day_off)
	print("back",back)
	# tomorrow = datetime.date.today() + datetime.timedelta(days=1)
	# tomorrow_year = tomorrow.strftime("%Y")
	# tomorrow_month = tomorrow.strftime("%m")
	# tomorrow_date = tomorrow.strftime("%d")
	#
	# tomorrow_year = str(int(year) - 1911)
	# if re.match(r'0\d{1}', tomorrow_month):
	# 	tomorrow_month = tomorrow_month.replace("0", "")
	# tomorrow_date = int(date) -1
	#
	# tomorrow_year_month = tomorrow_year + tomorrow_month




	context = {
		'today_member_duty':today_member_duty,
		'today_substitutes_duty':today_substitutes_duty,
		'tomorrow_member_duty':tomorrow_member_duty,
		'tomorrow_substitutes_duty':tomorrow_substitutes_duty,
		'today_supervisor':today_supervisor,
		'tomorrow_supervisor':tomorrow_supervisor,
		'day_off':day_off,
		'back':back,

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
