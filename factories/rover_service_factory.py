# factories/rover_service_factory.py
from clients.nasa_client import NasaClient
from strategies.curiosity_strategy import CuriositySolStrategy
from services.rover_service import RoverService
from config.config import Settings

def create_curiosity_service(sol: str, camera: str) -> RoverService:
    client = NasaClient(Settings.API_KEY)
    strategy = CuriositySolStrategy(sol, camera)
    return RoverService(client, strategy)