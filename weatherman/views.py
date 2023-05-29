from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    api_id = '9059c6a0de3144bc21a5dd21f3aa50d2'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    URL2 = 'https://geo.ipify.org/api/v2/country,city'
    api_id2 = 'at_nKYAgarxTzixcfRy2H5EOyGlzmEM0'
    params2 = {'apiKey':api_id2}
    
    params = {'q':'College Station', 'appid':api_id, 'units': 'metric'}
    
    req = requests.get(url=URL, params=params)
    req2 = requests.get(url=URL2, params=params2)
    
    reqs = req.json()
    reqs2 = req2.json()
    
    
    description = reqs['weather'][0]['description']
    icon = reqs['weather'][0]['icon']
    temp = reqs['main']['temp']
    
    ip_address = reqs2['ip']
    city = reqs2['location']['city']
    
    params_city_automatic = {'q':city, 'appid':api_id, 'units':'imperial'}
    req_automatic = requests.get(url=URL, params=params_city_automatic)
    
    reqs4 = req_automatic.json()
    
    description_automatic = reqs4['weather'][0]['description']
    icon_automatic = reqs4['weather'][0]['icon']
    temp_automatic = reqs4['main']['temp']
    
    
    return render(request, 'weatherman/index.html', {'description':description_automatic, 'icon': icon_automatic, 'temp':temp_automatic, 'ip_address':ip_address, 'city':city})
