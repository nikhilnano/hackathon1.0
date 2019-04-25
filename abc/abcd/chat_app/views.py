from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import chat as info
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})
def chat(request):
	return render(request,"addchat.html",{})
def home(*args,**kwargs):
	return HttpResponse("yeah, it is my first app and it is working(without using template)")
def register(request,*args,**kwargs):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username1 = form.cleaned_data.get('username')
			return redirect('login/')
	else:
		form = UserRegisterForm()
	return render(request,"register.html",{'form':form})
def show_chat(request):
    all_message=info.objects.all()
    return render(request,"show.html",{'ichat':all_message})
def add_chat1(request): 
	print("hello")
	message1     =   request.POST["message"]
	username1   =   request.user.username
	infor=info(message=message1,username1=username1)
	infor.save()
	all_message=info.objects.all()
	return render(request,"show.html",{'ichat':all_message})
def show_chats(request):
    all_message=info.objects.all()
    return render(request,"chats.html",{'ichat':all_message})