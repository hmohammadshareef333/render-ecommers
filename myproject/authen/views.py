from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def login_(request):

    login_nav=True

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'wrong.html')



    return render(request,'login_.html',{'login_nav':login_nav})

def register(request):
    login_nav=True

    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        u=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username)
        u.set_password(password)
        u.save()
        return redirect('login_')

    return render(request,'register.html',{'login_nav':login_nav})


def logout_(request):

    logout(request)

    return redirect('login_')


def profile(request):

    return render(request,'profile.html')