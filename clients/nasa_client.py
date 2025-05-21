# clients/nasa_client.py
import aiohttp

class NasaClient:
    BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers"

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get(self, rover: str, params: dict):
        url = f"{self.BASE_URL}/{rover}/photos"
        params["api_key"] = self.api_key

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()
                return resp.status, data