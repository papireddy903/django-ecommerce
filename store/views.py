from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import RegisterForm

def home(request):
    products = Product.objects.all()
    return render(request, "home.html",{"products":products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # messages.success(request, "Successfully logged in ")
            return redirect('home')
        else:
            # messages.error(request, "Invalid Credentials. Please try again")
            return redirect('login') 
    else:
        return render(request, 'login.html',{} )
            

        
    

def logout_user(request):
    logout(request)
    # messages.success(request, "Successfully logged out..")
    return redirect('home')


def register_user(request):
    # form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 

            user = authenticate(request, username=username, password=password) 
            login(request, user) 
            # messages.success(request,"Account registered..")
            return redirect('home')
        else:
            # messages.error(request, "There's a problem while creating account..")
            return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()

        
        
    return render(request, "register.html",{"form":form})


def products_page(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product}) 

def user_profile(request):
    return render(request, 'user_profile.html', {}) 

def orders(request):
    return render(request, "orders.html", {})

def cart(request):
    return render(request, 'cart.html', {})