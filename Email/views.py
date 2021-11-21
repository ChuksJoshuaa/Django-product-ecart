from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def email_view(request):
    form = ContactMeForm()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            subject = "Contact form inquiry"
            body = {
                'Name': form.cleaned_data['Name'],
                'Email': form.cleaned_data['Email'],
                'Phone_number': form.cleaned_data['Phone_number'],
                'Subject': form.cleaned_data['Subject'],
                'Message': form.cleaned_data['Message'],
            }
            message = '\n\n'.join(body.values())
            sender = form.cleaned_data['Email']
            recipient = ['chuksmbanasoj@gmail.com']
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Your message has been successfully sent")
            return redirect('prod-email')
    context = {
        'form': form,
    }
    return render(request, "prod_email.html", context)