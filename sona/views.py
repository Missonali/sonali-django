from django.shortcuts import render, HttpResponse, redirect
from sona.models import contact2
import time
def index(request):
    if request.method=="POST":
        name=request.POST['fname']
        email=request.POST['femail']
        number=request.POST['num']
        message=request.POST['msg']
        mydata=contact2(name=name,email=email,number=number,message=message)   
        mydata.save() 
    return render(request,'index.html')

# Create your views here.
