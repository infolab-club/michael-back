from django.shortcuts import render, HttpResponse

from api.models import *
from .service import parseDatasetToBd
from .forms import ParseForm

def index(request):
    form = ParseForm()
    if request.method == "POST":
        form = ParseForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                parseDatasetToBd(request.FILES['dataset'], request.POST['datetime_format'])
            except Exception as e:
                return HttpResponse(f"Failed \n{e}")
        else:
            return HttpResponse(str(form.errors))
        return HttpResponse("success")
    else:
        form = ParseForm()
    return render(request, 'form.html', {'form': form})