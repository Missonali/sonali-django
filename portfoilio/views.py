from django.shortcuts import render,HttpResponse,redirect
import time
def index(request):
    return render(request,'index.html')