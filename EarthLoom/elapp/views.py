from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_type = request.POST.get('login_type')  # Assuming you have this field in your form
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, login the user
            login(request, user)
            # Redirect to dashboard based on login type
            if login_type == 'farmer':
                return redirect('dashboard')  # Replace 'farmer_dashboard' with your actual URL name
            elif login_type == 'customer':
                return redirect('dashboard')  # Replace 'customer_dashboard' with your actual URL name
        else:
            # Authentication failed, show error message
            messages.error(request,'Invalid username or password. Please try again.')
    # If request method is GET or authentication failed, render the sign-in form
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        full_name = request.POST.get('fullName')
        contact = request.POST.get('contact')
        birthday_date = request.POST.get('birthdayDate')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        # Create a new user with password
        myuser = User.objects.create_user(username=username, password=password)
        myuser.user_type = user_type
        myuser.full_name = full_name
        myuser.save()
        # Log in the user
        messages.success(request, 'Account has been created successfully!!!')
        return redirect('signin')  # Redirect to the login page after successful signup
    return render(request, 'signup.html')


def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def edit(request):
    return render(request,'edit.html')

def newpass(request):
    return render(request,'newpass.html')

def helps(request):
    return render(request,'helps.html')

def report(request):
    return render(request,'report.html')

def info(request):
    return render (request,'info.html')

def vegetable(request):
    return render (request,'vegetable.html')

def fruits(request):
    return render (request,'fruits.html')

def dryfruit(request):
    return render (request,'dryfruit.html')

def store(request):
    return render (request,'store.html')

def offers(request):
    return render (request,'offers.html')