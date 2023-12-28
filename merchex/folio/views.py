from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #bands = Band.objects.all()
    dd = 15
    return render(request, 'folio/index.html', {'d': dd})
