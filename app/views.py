import re
from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# from app.models import Order
import random
# orderid = {}
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
        desc = request.POST.get('Details')
        file = request.POST.get('file')
        subject = "Welcome To tutorchamps"
        message = "Hello this is new ppost"
        print(email)
        recepient = str(email)
        send_mail(subject,message,'qamarqs786@gmail.com',[recepient],fail_silently=False)

        return render(request,'dashboard.html')

    return render(request,'services.html')





