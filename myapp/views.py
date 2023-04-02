from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    videos = VideoUploader.objects
    context = {
        'videos' :videos
    }
    return render(request,'myapp/index.html',context)


def hom(request):
    return render(request,'myapp/base.html')



def pay(request):
    return render(request,'myapp/pay.html')


def paya(request):
    return render(request,'myapp/confirm.html')

def pay1(request):
    return render(request,'myapp/pa.html')


def paya1(request):
    return render(request,'myapp/conf.html')



def index1(request):
    video = VideoUploader1.objects
    context = {
        'video' :video
    }
    return render(request,'myapp/index1.html',context)


def index2(request):
    video1 = VideoUploader2.objects
    context = {
        'video1' :video1
    }
    return render(request,'myapp/index2.html',context)