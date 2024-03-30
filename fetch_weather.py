from aiohttp import ClientSession

async def fetch_weather(city) -> str:
        async with ClientSession() as session:
            api_key: str = '799a68dd333c2cdc39c1a33d8d930a6e'

            params = {'q': city, 'APPID': api_key}
            url = f'http://api.openweathermap.org/data/2.5/weather' 

            async with session.get(url=url, params=params) as response:
                weather_json = await response.json()
                return weather_json