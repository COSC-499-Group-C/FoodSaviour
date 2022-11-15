from django.shortcuts import render, redirect
from .Forms.newUser import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import OrgGroups, Organizations
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/admin")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def home_page_request(request):
    if request.user.is_authenticated:
        return render(request=request, template_name="home.html", context={"username": request.user.username})
    else:
        return render(request=request, template_name="home.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request=request, template_name="home.html")


# Working on it
def org_page_request(request):
    if request.method == "GET":
        org_id = OrgGroups.objects.get(user_id=request.user.id)
