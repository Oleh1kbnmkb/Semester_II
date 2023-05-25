weather = {
    'coord': {'lon': 30.5167, 'lat': 50.4333}, 
    'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
    'base': 'stations', 
    'main': {
        'temp': 293.55, 
        'feels_like': 293.24, 
        'temp_min': 291.82, 
        'temp_max': 293.55, 
        'pressure': 1023, 
        'humidity': 61
        }, 
    'visibility': 10000, 
    'wind': {
        'speed': 1.34, 
        'deg': 358, 
        'gust': 5.36
    }, 
    'clouds': {'all': 19}, 
    'dt': 1684567426, 
    'sys': {
        'type': 2, 
        'id': 2003742, 
        'country': 'UA', 
        'sunrise': 1684548267, 
        'sunset': 1684604682
    }, 
    'timezone': 10800, 
    'id': 703448, 
    'name': 'Kyiv', 
    'cod': 200
}

min_temperature = weather['main']['temp_min'] - 273
print(min_temperature)
max_temperature = weather['main']['temp_max'] - 273
print(max_temperature)
temperature = weather['main']['temp'] - 273
print(temperature)


wind_speed = weather['wind']['speed'] * 3.6
print(wind_speed)

country = weather['sys']['country']
print(country)
