import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    crunchbase_token: str = os.getenv("CRUNCHBASE_TOKEN", "")
    
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
