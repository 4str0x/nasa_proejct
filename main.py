import asyncio
from factories.rover_service_factory import create_curiosity_service

async def main():
    service = create_curiosity_service(sol="1123", camera="fhaz")
    result = await service.get_photos()
    print(result)

asyncio.run(main())