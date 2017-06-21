from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# Create your views here.

def index(request):

	responsJson = requests.get("http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b1b15e88fa797225412429c1c50c122a1").json()
	temprature = responsJson["main"]["temp"]

	return HttpResponse(temprature)
