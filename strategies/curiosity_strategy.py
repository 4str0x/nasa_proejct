# strategies/curiosity_strategy.py
from strategies.photo_strategy import PhotoStrategy

class CuriositySolStrategy(PhotoStrategy):
    def __init__(self, sol: str, camera: str):
        self.sol = sol
        self.camera = camera

    async def fetch_photos(self, client):
        return await client.get("curiosity", {"sol": self.sol, "camera": self.camera})