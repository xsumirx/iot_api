from django.shortcuts import render
from django.http.response import HttpResponse
from .models import User

# Create your views here.

def create_user(request):

    listUsers = User.objects.all()

    name = ""

    for p in listUsers:
        name += p



    return HttpResponse("Yess it worked" + name)
