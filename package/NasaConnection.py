from typing import Any
import aiohttp

from config import Settings

class Client:
    def __init__(self):
        self.http: aiohttp.ClientSession = aiohttp.ClientSession()
        self.url: str = Settings.API_URL

    async def Curiosity(self, sol:str, cam:str) -> dict[str, Any]:
        try:
            async with self.http.request(
                method="GET",
                url=f"{self.url}rovers/curiosity/photos?sol={sol}&camera={cam}&api_key=RSqpmvcy5lKi3luNx9qMJwJXUeYufYVhmuvgxtag",
            ) as request:
                
                data: dict[str, Any] = await request.json()
                status_code: int = request.status

                match status_code:
                    case 200:
                        return {"status": True, "payload": data["photos"]}

                    case _:
                        return {"status": False, "Error": data["code"]}
                    
        except aiohttp.ClientError as e:
            return {"status": False, "Error": "Deu erro meu bom!"}