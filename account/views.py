from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.forms import CustomUserCreationForm, CustomUserChangeForm
# Authentication function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def registerRequest(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already authenticated")    
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST' or request.method == 'post':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                    # Redirect to a success page or login page
                return HttpResponse('Your request Has been Created...')  # Assuming you have a URL named 'login'
    return render(request, 'register.html', {'form': form})


def loginRequest(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already loggedIn....")   
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username, password=password)

            if customer is not None:
                login(request, customer)
                return HttpResponse('Successfully Loggin...')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")


    return render(request, 'login.html')

def logoutRequest(request):
    logout(request)
    messages.info(request,'You have successfully logged out')
    return HttpResponse('Successfully Logout...')
