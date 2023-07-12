

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import perfume

# Create your views here.
perfs = perfume.objects.all()


def index(request):
    return render(request, 'index.html', {'perfs': perfs})
