"""
Main application entry point.
"""

from fastapi import FastAPI

from app.metadata import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
)
from app.types import ResponseMessage
from app.constants import DEFAULT_HEALTH_STATUS

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
async def get_root() -> ResponseMessage:
    """
    Return the root endpoint response for the Enterprise AI Prediction Platform.

    Returns:
    ResponseMessage: Welcome message for API consumers.
    """
    return {
        "message": "Welcome to Enterprise AI Prediction Platform"
    }


@app.get("/health")
async def get_health_endpoint() -> ResponseMessage:
    """ 
    Return the current application health status.

    Returns:
        ResponseMessage: Health status information.
    """
    
    return {
        "status": DEFAULT_HEALTH_STATUS
    }
    