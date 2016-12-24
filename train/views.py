from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import ZhuDiTable, ZuXunTable
from .forms import ZhuDiTableForm

# Create your views here.

def zhudi_table_detail(request, pk):
	zhudi = get_object_or_404(ZhuDiTable, pk=pk)

	context = {
	'zhudi': zhudi,

	}
	return render(request, 'zhudi_table_detail.html', context)

def zhudi_table_list(request):
	zhudis = ZhuDiTable.objects.all()
	

	context = {
	'zhudis': zhudis,

	}
	return render(request, 'zhudi_table_list.html', context)

def zhudi_table_create(request):
	form = ZhuDiTableForm()

	if request.method == 'POST':
		form = ZhuDiTableForm(request.POST, request.FILES)

		if form.is_valid():
			fileform = form.save(commit=False)
			files = request.FILES.getlist('img')
			fileform.img = files[0]
			fileform.img2 = files[1]
			other_files = request.FILES.getlist('img3')
			for other_file in other_files:
				fileform.img3 = other_file
				fileform.save()


			return HttpResponseRedirect('/train/' + str(fileform.pk))

	return render(request, 'zhudi_table_create.html', {'form': form})











