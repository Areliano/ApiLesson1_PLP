from django.http import response
from django.shortcuts import render
import requests

def home(request):
  #using APIs
  response = requests.get("https://api.github.com/events")
  data = response.json()
  result = data[0]["id"]

  #example2 of APIs
  response2 = requests.get("https://api.github.com/events")
  data2 = response2.json()
  result2 = data2[2]["id"]

  return render(request, 'templates/index.html', {'result': result, 'result2': result2})