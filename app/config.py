from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # See https://docs.pydantic.dev/usage/settings/
    name: str = Field("FastAPI-Demo", env="NAME")
    version: str = Field("0.0.1", env="VERSION")
    debug_mode: str = Field(False, env="DEBUG_MODE")


settings = Settings()