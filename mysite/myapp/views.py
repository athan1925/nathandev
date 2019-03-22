from django.shortcuts import render
from .models import Contact
import requests
import json

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'myapp/index.html', context)
    else:
        firstname = 'Jonathan'
        lastname = 'Dela Cruz'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'myapp/index.html', context)

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'myapp/contact.html')
    else:
        return render(request, 'myapp/contact.html')

def about(request):
    return render(request, 'myapp/about-us.html')

def portfolio(request):
    return render(request, 'myapp/portfolio.html')

def services(request):
    return render(request, 'myapp/services.html')



