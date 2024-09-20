from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .form import SoldierForm,BioForm,StudentForm
from .models import SoldierModel,BioModel,StudentModel
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView









from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)




def crudtest(request):
    context = {}
    
    if request.method == 'POST':
        form = SoldierForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'notes/crud.html', {'success': 'Soldier created successfully!'})
    else:
        form = SoldierForm()
        soldiers = SoldierModel.objects.all()
        context['form'] = form
        context['soldiers'] = soldiers
    
    return render(request, 'notes/crud.html', context)
 
def delete_soldier(request,id):
     obj = get_object_or_404(SoldierModel, id = id)
     obj.delete()
     return redirect('crudtest')
        
def index(request):
    return render(request , template_name='notes/index.html')

def update_view(request,id):
    
    context ={}
    
    obj = get_object_or_404(SoldierModel,id=id)
    form = SoldierForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        form.save()  
    
    context['form'] = form
    
    return render(request, 'notes/test.html', {'form': form } )



def crudtest2(request):
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            # do something with the form data
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            location = form.cleaned_data['location']
            favouritecar = form.cleaned_data['favouritecar']
            notes = form.cleaned_data['notes']
            form.save()
            
    else:
        form = BioForm()
    return render(request, 'notes/crud2.html', {'form': form})


def crudtest3(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # do something with the form data
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            form.save()
            
    else:
        form = StudentForm()
    return render(request, 'notes/crud3.html', {'form': form})


def logout(request):
    return render(request , template_name='notes/logout.html')



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def base(request):
    return render(request , template_name='notes/base.html')



def aboutus(request):
    return render(request , template_name='notes/about.html')


# def LoginView(request):
#     return render(request , template_name='registration/login.html')


def sign(request):
    return render(request , template_name='notes/signup.html')








   






