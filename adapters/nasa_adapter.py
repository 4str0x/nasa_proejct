# adapters/nasa_adapter.py
class NasaPhotoAdapter:
    @staticmethod
    def adapt(data: dict) -> list[dict]:
        return data.get("photos", [])