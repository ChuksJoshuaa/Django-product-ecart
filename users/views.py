from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import userform
from django.contrib import messages

# Create your views here.
def user_registerview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to log in")
            return redirect('prod-user_login')

    else:
        form = userform()
    context = {
        "form": form
    }
    return render(request, "prod-user_register.html", context)
