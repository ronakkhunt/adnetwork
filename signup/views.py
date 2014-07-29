# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Publisher
import datetime
import os
def p_signup(request):
	uname = request.POST.get('username')
	email = request.POST.get('email')
	passwd = request.POST.get('password')
	fname = request.POST.get('fname')
	lname = request.POST.get('lname')
	t = request.POST.get('utype')
	uidd=str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','').replace('.','')
	p = Publisher(username=uname, apid=uidd, email=email, password=passwd, type=t, first_name=fname, last_name=lname)
	p.save()
	
	p = Publisher.objects.get(username=uname)
	if p.username:
		return HttpResponseRedirect('/login/')
	return HttpResponse("Sign up Failed")
	
	#	return HttpResponse(uname+email+password)

def signup(request):
	return render(request,'signup.html',{'title':'Sign Up'})

def login(request):
	
	return render(request,'login.html',{'title':'Login'})

def p_login(request):
	uname = request.POST.get('username')
	password = request.POST.get('password')
	
	p1 = Publisher.objects.get(username=uname)
	if p1.password == password:
			return HttpResponse("Login Correct!!")
	return HttpResponse("Login Failde")
