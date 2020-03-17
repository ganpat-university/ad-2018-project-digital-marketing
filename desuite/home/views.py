from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html',{'titles':'django'})


def profile(request):
    return HttpResponse("Profile Page")
