import requests
from django.shortcuts import render
from . import models
from . import forms
# Create your views here.


def home(request):

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2d73c89d314d4d9767f754e00e639a87'
    cities = models.City.objects.all()
    
    if request.method == "POST":
        form = forms.CityForm(request.POST)
        form.save()
    
    form = forms.CityForm()
    
    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        data = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        
        weather_data.append(data)
    
        print('weather_data', weather_data)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'home.html', context)