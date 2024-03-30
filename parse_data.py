from time_handlers import get_time
from datetime import datetime
from localizations import translate

async def parse_data(data, language='en') -> str:
    #* Парсинг всей необходимой информации

    city_name = data['name']
    wind_speed = data['wind']['speed']
    weather = data['weather'][0]['main']
    temp = str(int(int(data['main']['temp']) - 273))
    temp_feels_like = str(int(int(data['main']['feels_like']) - 273))
    weather_description = data['weather'][0]['description']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
    offset = int(data['timezone'])
    current_time = get_time(offset)

    return (f'''Weather in {city_name} right now is:\n
    Wind speed: {wind_speed} m/s
    Weather: {weather}, {weather_description} 
    Temperature: {temp}°C
    Feels like: {temp_feels_like}°C
    Atmosphere pressure: {pressure}
    Humidity: {humidity} %
    Sunrise: {sunrise}
    Sunset: {sunset} 
    Current time: {current_time}
                        ''')