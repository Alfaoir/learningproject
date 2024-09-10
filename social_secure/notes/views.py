from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from notes.form import UserRegistrationForm,UserLoginForm
from django.contrib import messages
from notes.form import UserLoginForm
from django.http import JsonResponse







# Create your views here.
 


def index(request):
    return render(request , template_name='notes/index.html')







def signup(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            if password != re_password:
                return JsonResponse({'error': 'Passwords do not match'}, status=400)
            user = User.objects.create_user(username=username, email=email, password=password)
            if user.is_active:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'User could not be created'}, status=400)
    return render(request, 'notes/signup.html', {'form': form})



# def Userlogin(request):
#     form = UserLoginForm()
#     data = {
#         'form':form
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password = password)
#         if user is not None:
#             login(request,user)
#             print(username,password)
#     return render(request , template_name='notes/login.html',context=data) 


def Userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Login successful!'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form is not valid!'})
    else:
        form = UserLoginForm()
    
    data = {
        'form': form
    }
    
    return render(request, 'notes/login.html', context=data)






def userlogintable(request):
    users = User.objects.all()  # Fetch all users from the User model
    return render(request, 'notes/tabledata.html', {'users': users})
