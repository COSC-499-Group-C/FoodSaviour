from django.shortcuts import render, redirect
from .Forms.newUser import NewUserForm
from .Forms.MetricForms import PredictionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import OrgGroups, Organizations, WasteType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import registered_org_user


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def home_page_request(request):
    if request.user.is_authenticated:
        fullname = request.user.first_name + " " + request.user.last_name
        return render(request=request, template_name="home_loggedin.html", context={"username": fullname})
    else:
        return render(request=request, template_name="home.html")


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            messages.info(request, "Invalid username or password.")
    return render(request=request, template_name="login.html")
    


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request=request, template_name="home.html")


@registered_org_user
def org_page_request(request):
    if request.method == "GET":
        org_id = OrgGroups.objects.filter(user_id=request.user.id).first().group_id
        organization_name = Organizations.objects.filter(id=org_id).first().name
        return render(request=request, template_name="org_page.html", context={"Organization": organization_name})
    else:
        redirect("/login")


def metrics_page_request(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/tracker")
    form = PredictionForm()
    return render(request=request, template_name="metrics.html",
                  context={"form": form, "username": request.user.username})


def tracker(request):
    return render(request=request, template_name="tracker.html")
