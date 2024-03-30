from aiohttp import ClientSession
from config import config
import asyncio

async def fetch_cat_image():
    async with ClientSession() as session:
            api_key: str = config.bot_token.get_secret_value()

            params = {}
            url = f'https://api.thecatapi.com/v1/images/search' 

            async with session.get(url=url, params=params) as response:
                response = await response.json()
                return response

async def main():
     result = await fetch_cat_image()
     print(result[0]['url'])

asyncio.run(main())