import re
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(requset):
    return render(requset,'blog.html')

def homework(request):
    if request.method =='POST':
        email = request.POST.get('email')
        phone = request.POST.get('if-phone')
        subject = request.POST.get('subject')
        deadline = request.POST.get('deadline')
        desc = request.POST.get('desc')
        file = request.POST.get('file')



        return render(request,'dwashboard.html')

    return render(request,'services.html')





