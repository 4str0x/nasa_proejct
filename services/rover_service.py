# services/rover_service.py
from adapters.nasa_adapter import NasaPhotoAdapter

class RoverService:
    def __init__(self, client, strategy):
        self.client = client
        self.strategy = strategy

    async def get_photos(self):
        status, data = await self.strategy.fetch_photos(self.client)
        if status == 200:
            return {"status": True, "photos": NasaPhotoAdapter.adapt(data)}
        return {"status": False, "error": data.get("error", "Unknown error")}