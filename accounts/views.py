from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
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
	if request.method=="POST":
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Congratulations {request.user.email}, your profile has been updated successfully!')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	context={
		'u_form':u_form,
		'p_form':p_form
		}
	return render(request,'accounts/profile.html',context)

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')