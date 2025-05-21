import asyncio

from package import NasaConnection

async def main():
    Client = NasaConnection.Client()

    dados = await Client.Curiosity(cam="FHAZ", sol="1250")

    print(dados)


if __name__ == "__main__":
    asyncio.run(main())