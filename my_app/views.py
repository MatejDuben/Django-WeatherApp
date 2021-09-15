from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
  your_API_key = ''   #here you need add your API KEY from openweathermap
  url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
  city = 'Bratislava'
  weather = requests.get(url.format(city, your_API_key)).json()
  #print(weather)

  types = ['cloud',  'thunderstorm','rain', 'clear', 'calm']

  context = {
      'city': weather['name'],
      'desc': weather['weather'][0]['description'],
      'icon': weather['weather'][0]['icon'],
      'state':  weather['sys']['country'],
      'temp': weather['main']['temp'],
      'feelTemp': weather['main']['feels_like'],
      
      'cloud':types[0],
      'thunderstorm':types[1],
      'rain':types[2],
      'clear_sky':types[3],
      'calm':types[3],
  }




  if request.method == "GET":
    if request.GET.get('add-city'):
      new_city = request.GET.get('add-city')
      
      url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
      city = new_city
      try:
        weather = requests.get(url.format(city, your_API_key)).json()  
        types = ['cloud',  'thunderstorm','rain', 'clear', 'calm']

        context = {
          'city': weather['name'],
          'desc': weather['weather'][0]['description'],
          'icon': weather['weather'][0]['icon'],
          'state':  weather['sys']['country'],
          'temp': weather['main']['temp'],
          'feelTemp': weather['main']['feels_like'],
          
          'cloud':types[0],
          'thunderstorm':types[1],
          'rain':types[2],
          'clear_sky':types[3],
          'calm':types[3],
        }
          
        return render(request, 'index.html', context)
      
      except:
        
        print("ERR")
        context['err_message'] = [f'The city, "{new_city}" not found.',"probably you wrote incorrect name of city or this city don't exists."]
        print(context.get('err_message')[0])
            
        
        


    

  return render(request, 'index.html', context)

  