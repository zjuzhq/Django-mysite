# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os

def uploadfile(request):
    if request.method=='POST':
        obj=request.FILES.get("zqfile")
        f=open('./media/'+obj.name,'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        return HttpResponse('ok')
    filelist=os.listdir('./media/')
    return render(request,'uploadfile.html',{'filelist':filelist})

def ok(request):
    return HttpResponse('okkk')