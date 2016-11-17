from django.shortcuts import render, HttpResponseRedirect
from .models import UserProfile, Payee
from .forms import CreateColleagueForm, EditNumberFormSet, CreateColleagueFormSet
from tablemoney.forms import MonthCreateForm
from django.core.urlresolvers import reverse
from django.contrib import messages


# from .forms import PayeeForm

# Create your views here.

def profile_list(request):
	profiles = UserProfile.objects.all()
	members = UserProfile.members.all()
	substitutes = UserProfile.substitutes.all()

	context = {
	'profiles':profiles,
	'members':members,
	'substitutes':substitutes,

	}

	return render(request, 'profile_list.html', context)


def profile_delete_list(request):
	profiles = UserProfile.objects.all()
	members = UserProfile.members.all()
	substitutes = UserProfile.substitutes.all()

	if request.method == 'GET':
		delete_pk = request.GET.get('pk')
		delete_colleagues = request.GET.get('delete')
		
		if delete_colleagues:
			UserProfile.objects.get(pk=delete_pk).delete()
			messages.add_message(request, messages.INFO, '已刪除人員')
			return HttpResponseRedirect(reverse(profile_delete_list))

	context = {
	'profiles':profiles,
	'members':members,
	'substitutes':substitutes,

	}

	return render(request, 'profile_delete_list.html', context)

def create_colleague(request):
	form = CreateColleagueForm()

	if request.method == "POST":
		form = CreateColleagueForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, '已新增人員')
			return HttpResponseRedirect('profile_list')

	last_members = UserProfile.members.all().order_by("-number")[0]
	last_substitutes = UserProfile.substitutes.all().order_by("-number")[0]

	context = {
	'form':form,
	'last_members':last_members,
	'last_substitutes':last_substitutes,
	}
	return render(request, 'create_colleague.html', context)

def edit_profile(request):
	profiles = UserProfile.objects.all()
	formset = CreateColleagueFormSet(queryset=profiles)

	if request.method =='POST':
		formset = CreateColleagueFormSet(request.POST)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				form.save()
				messages.add_message(request, messages.INFO, '人員資料編輯完成')
			return HttpResponseRedirect(reverse(profile_list))

	context = {
	'formset': formset,
	'profiles': profiles,
	}
	return render(request, 'edit_profile.html', context)

def edit_member_number(request):
	members = UserProfile.members.all()
	formset = EditNumberFormSet(queryset=members)

	if request.method =='POST':
		formset = EditNumberFormSet(request.POST)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				form.save()
				messages.add_message(request, messages.INFO, '編號更改完成')
			return HttpResponseRedirect(reverse(profile_list))

	context = {
	'formset': formset,
	'members': members,
	}
	return render(request, 'edit_member_number.html', context)

def edit_substitute_number(request):
	substitutes = UserProfile.substitutes.all()
	formset = EditNumberFormSet(queryset=substitutes)

	if request.method =='POST':
		formset = EditNumberFormSet(request.POST)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				form.save()
				messages.add_message(request, messages.INFO, '編號更改完成')
			return HttpResponseRedirect(reverse(profile_list))

	context = {
	'formset': formset,
	'substitutes':substitutes,
	}
	return render(request, 'edit_substitute_number.html', context)