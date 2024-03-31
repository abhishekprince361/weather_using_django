import datetime
import requests
from django.shortcuts import render


def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        return render(request, "search.html")
        # city = "New Delhi"

    api_key = '40228924c4a3846ff0dd11a7ba543e17'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        data = requests.get(url).json()

        photos = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        day = datetime.date.today()
        temp_dict = {'humidity': humidity,
                     'speed': wind_speed,
                     'temp': temp,
                     'day': day,
                     'city': city,
                     'photos': photos,
                     }
        return render(request, "index.html", temp_dict)

    except:
        mydict = {
            'city': city,
            'day': datetime.date.today(),
            'boolean_temp': True,
        }
        return render(request, "search.html", mydict)
