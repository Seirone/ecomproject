from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

#app_name = 'contact'

def contact(request):
	title = 'Contact Us'
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		#print(request.POST)
		#print(form.cleaned_data['email'])
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject ='Message from Seirone Global'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		title = 'Thanks!'
		confirm_message = 'Thanks for the message, we will get back to you.'
		form = None
		
	context = {'title': title, 'form': form, 'confirm_message': confirm_message,}	
	#context = locals()
	template = 'contact.html'
	return render(request,template,context)