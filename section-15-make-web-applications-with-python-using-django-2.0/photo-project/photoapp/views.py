from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Photo
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.


def index(request):
    all_photo = Photo.objects.all()
    context = {
        'all_photo': all_photo
    }
    return render(request, 'photoapp/index.html', context)


def detail(request, photo_id):
    all_photo = Photo.objects.get(id= photo_id)
    context = {
        'photo' : all_photo
    }
    return render(request, 'photoapp/detail.html', context)