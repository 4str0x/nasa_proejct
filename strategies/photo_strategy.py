# strategies/photo_strategy.py
from abc import ABC, abstractmethod

class PhotoStrategy(ABC):
    @abstractmethod
    async def fetch_photos(self, client):
        pass