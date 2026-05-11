import os

from fastapi import FastAPI


def get_settings() -> dict:
    return {
        "app_name": os.getenv("APP_NAME", "Mergington FastAPI Service"),
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "0.1.0"),
    }


app = FastAPI()


@app.get("/")
def root() -> dict:
    settings = get_settings()
    return {
        "message": "Service is running",
        "app": settings["app_name"],
        "environment": settings["environment"],
        "version": settings["version"],
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}