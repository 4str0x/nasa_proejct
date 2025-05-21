from pydantic_settings import BaseSettings

class _Settings(BaseSettings):
    # Configurações do JWT
    API_KEY: str
    API_URL: str

Settings = _Settings(_env_file=".env")  # type: ignore