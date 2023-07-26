from pydantic_settings import BaseSettings

class MySettings(BaseSettings):
    HOST: str = ""
    PORT: int
    RELOAD:bool

    class Config:
        env_file = ".env"

    def __init__(self):
        super().__init__(**self.dict())

settings = MySettings()