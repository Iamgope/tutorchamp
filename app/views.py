from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(requset):
    return render(requset,'blog.html')


def signup(request):
    pass

