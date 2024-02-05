from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def registerRequest(request):
    return render(request,'base.html')
    # return HttpResponse("Register Page")

