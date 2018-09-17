from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .namer import company, author

#app_name = 'profiles'

def home(request):
	context = {'company': company}
	template = 'home.html'
	return render(request,template,context)
	#return render(request,'home.html',{})

def about(request):
	#context = locals()
	template = 'about.html'
	return render(request,template,{'company': company, 'my_profile': author})

@login_required
def userProfile(request):
	user = request.user
	context = {'user': user }
	template = 'profile.html'
	return render(request,template,context)

def cheat(request):
	#context = locals()
	template = 'cheat.html'
	return render(request,template,{})



