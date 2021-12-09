from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from user.models import UserMicky
from .forms import UserMickyForm

def myHomeView(request, *args, **kwargs):
    pass

def register(request):
    form = UserMickyForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.save()
        form = UserMickyForm()

    context = {
        'form': form
    }
    return render(request, "userMickyCreate.html", context)
# Create your views here.
