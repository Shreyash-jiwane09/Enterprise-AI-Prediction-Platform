"""
Application entry point for the Enterprise AI Prediction Platform.

This module creates the FastAPI application instance and registers
all API routers.
"""

from fastapi import FastAPI

from app.metadata import APP_DESCRIPTION, APP_TITLE, APP_VERSION
from app.routers.health import router as health_router
from app.routers.root import router as root_router
from app.routers.users import router as users_router

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(users_router)