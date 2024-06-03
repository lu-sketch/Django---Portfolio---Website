from django.shortcuts import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


""" These are the html pages for the 'personal' app of the project.
This part consits of a home, about, and contact page
The contact page also consits of a contact form that the user
can choose to complete."""


def home(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def education(request):
    return render(request, 'personal/education.html')

def contact(request):
    return render(request, 'personal/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Create a new Contact object and save it
            new_contact = Contact.objects.create(first_name=first_name, email=email, message=message)
            print(new_contact.first_name)
            return render(request, 'personal/home.html')  
    else:
        form = ContactForm()
    return render(request, 'personal/contact.html', {'form': form})


