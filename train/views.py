from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import ZhuDiTable, ZuXunTable, ZhuDi, ZuXun
from .forms import ZhuDiTableForm, ZuXunTableForm, ZhuDiSessionForm, ZuXunSessionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def zhudi_table_detail(request, pk):
	zhudi = get_object_or_404(ZhuDiTable, pk=pk)
	date = zhudi.date.split('.')[1] + zhudi.date.split('.')[2]
	session = zhudi.session
	title = str(date) + ' ' + str(session)


	context = {
	'zhudi': zhudi,
	'title': title,
	}
	return render(request, 'zhudi_table_detail.html', context)

@login_required
def zhudi_table_list(request):
	zhudis = ZhuDiTable.objects.all()


	context = {
	'zhudis': zhudis,

	}
	return render(request, 'zhudi_table_list.html', context)

@login_required
def zhudi_session_create(request):
	form = ZhuDiSessionForm()
	zhudi_sessions = ZhuDi.objects.all()

	if request.method == 'POST':
		form = ZhuDiSessionForm(request.POST)

		if form.is_valid():
			new_session = form.save(commit=False)
			new_session.save()
			messages.add_message(request, messages.INFO, '項目新增完成')
			return HttpResponseRedirect(reverse(zhudi_session_create))

	context = {
		'zhudi_sessions': zhudi_sessions,
		'form': form,
	}

	return render(request, 'zhudi_session_create.html', context)

@login_required
def zhudi_session_delete(request, pk):
	zhudi_session = get_object_or_404(ZhuDi, pk=pk)
	if zhudi_session:
		zhudi_session.delete()
		messages.add_message(request, messages.INFO, '項目刪除完成')
		return HttpResponseRedirect(reverse(zhudi_session_create))

	context = {

		'zhudi_session': zhudi_session,
	}

	return render(request, 'zhudi_session_create.html', context)

@login_required
def zhudi_table_create(request):
	form = ZhuDiTableForm()

	if request.method == 'POST':
		form = ZhuDiTableForm(request.POST, request.FILES)

		if form.is_valid():
			fileform = form.save(commit=False)
			unform_date = form.cleaned_data['date']
			unform_date = unform_date.split('/')
			unform_date[0] = str(int(unform_date[0]) - 1911)
			form_date = '.'.join(unform_date)

			fileform.date = form_date
			fileform = form.save(commit=False)

			files = request.FILES.getlist('img')
			fileform.img = files[0]
			fileform.img2 = files[1]
			fileform.save()


		fileform.save()
		return HttpResponseRedirect('/train/zhudi/' + str(fileform.pk))

	return render(request, 'zhudi_table_create.html', {'form': form})

@login_required
def zhudi_table_delete(request, pk):
	zhudi = get_object_or_404(ZhuDiTable, pk=pk)

	if zhudi:
		zhudi.delete()
		messages.add_message(request, messages.INFO, '表格刪除完成')
		return HttpResponseRedirect(reverse(zhudi_table_list))

	context = {
	'zhudi': zhudi,

	}
	return render(request, 'zhudi_table_detail.html', context)

@login_required
def zuxun_table_detail(request, pk):
	zuxun = get_object_or_404(ZuXunTable, pk=pk)

	context = {
	'zuxun': zuxun,

	}
	return render(request, 'zuxun_table_detail.html', context)

@login_required
def zuxun_table_list(request):
	zuxuns = ZuXunTable.objects.all()


	context = {
	'zuxuns': zuxuns,

	}
	return render(request, 'zuxun_table_list.html', context)

@login_required
def zuxun_session_create(request):
	form = ZuXunSessionForm()
	zuxun_sessions = ZuXun.objects.all()

	if request.method == 'POST':
		form = ZuXunSessionForm(request.POST)


		if form.is_valid():
			new_session = form.save(commit=False)
			new_session.save()
			messages.add_message(request, messages.INFO, '項目新增完成')
			return HttpResponseRedirect(reverse(zuxun_session_create))

	context = {
		'zuxun_sessions': zuxun_sessions,
		'form': form,

	}

	return render(request, 'zuxun_session_create.html', context)

@login_required
def zuxun_session_delete(request, pk):
	zuxun_session = get_object_or_404(ZuXun, pk=pk)
	if zuxun_session:
		zuxun_session.delete()
		messages.add_message(request, messages.INFO, '項目刪除完成')
		return HttpResponseRedirect(reverse(zuxun_session_create))

	context = {

		'zuxun_session': zuxun_session,
	}

	return render(request, 'zuxun_session_create.html', context)


@login_required
def zuxun_table_create(request):
	form = ZuXunTableForm()

	if request.method == 'POST':
		form = ZuXunTableForm(request.POST, request.FILES)

		if form.is_valid():
			fileform = form.save(commit=False)

			sessions = form.cleaned_data['session']
			fileform.session = ''
			i = 0
			for session in sessions:
				if i == 0:
					fileform.session += str(session)
					i += 1
				else:
					fileform.session += '、' + str(session)

			unform_date = form.cleaned_data['date']
			unform_date = unform_date.split('/')
			unform_date[0] = str(int(unform_date[0]) - 1911)
			form_date = '.'.join(unform_date)

			fileform.date = form_date
			fileform = form.save(commit=False)

			files = request.FILES.getlist('img')
			fileform.img = files[0]
			fileform.img2 = files[1]
			fileform = form.save(commit=False)


		fileform.save()
		return HttpResponseRedirect('/train/zuxun/' + str(fileform.pk))

	return render(request, 'zuxun_table_create.html', {'form': form})

@login_required
def zuxun_table_delete(request, pk):
	zuxun = get_object_or_404(ZuXunTable, pk=pk)

	if zuxun:
		zuxun.delete()
		messages.add_message(request, messages.INFO, '表格刪除完成')
		return HttpResponseRedirect(reverse(zuxun_table_list))

	context = {
	'zuxun': zuxun,

	}
	return render(request, 'zuxun_table_detail.html', context)
