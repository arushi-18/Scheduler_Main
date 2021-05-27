from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Congratulations {username}, your account has been created successfully!')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request,"accounts/register.html",{'form':form})

@login_required
def profile(request):
	return render(request,'accounts/profile.html')

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')