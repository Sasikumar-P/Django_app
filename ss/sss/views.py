from django.shortcuts import render
from models import *
from django.http import HttpResponseRedirect
from sss.forms import ContactForm
# Create your views here.

def home(request):
	return render(request, 'home.html')


def add(request):
	if request.method == 'POST':
		author = Author.objects.create(first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email=request.POST.get('email'),phonenumber =request.POST.get('phonenumber'),address=request.POST.get('adddress'),state=request.POST.get('sttate'),city=request.POST.get('ciity'),country=request.POST.get('couuntry'))
		author.save()
		return render(request, 'new2.html')
	else:
		return render(request, 'home.html')

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	if request.method == 'POST':
		publisher = Publisher.objects.create(name=request.POST.get('name'), address=request.POST.get('address'), city=request.POST.get('city'), state_province=request.POST.get('state'), website=request.POST.get('web'))
		publisher.save()
		return render(request, 'home.html')
	else:
		return render(request, 'new2.html')
def index2(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	if request.method == 'POST':
		publisher = Page.objects.create(title=request.POST.get('title'), url=request.POST.get('url'), views=request.POST.get('views'))
		publisher.save()
		return render(request, 'home.html')
	else:
		return render(request, 'new.html')
	
	
  
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
		
			return HttpResponseRedirect('new3.html')
	else:
		form = ContactForm()
	return render(request, 'home.html', {'form' : form})
