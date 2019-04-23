from django.http import HttpResponse
from django.shortcuts import render
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})

def home(*args,**kwargs):
	return HttpResponse("yeah, it is my first app and it is working(without using template)")