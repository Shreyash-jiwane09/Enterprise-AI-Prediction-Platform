"""
Health router for the Enterprise AI Prediction Platform.

This module contains health-related API endpoints used to verify
that the application is running correctly.
"""

from fastapi import APIRouter

from app.constants import DEFAULT_HEALTH_STATUS
from app.types import ResponseMessage

router = APIRouter(
    prefix="",
    tags=["Health"],
)


@router.get("/health")
async def get_health_status() -> ResponseMessage:
    """
    Check the health status of the application.

    Returns:
        ResponseMessage: A message indicating the application
        is running successfully.
    """
    return {
        "status": DEFAULT_HEALTH_STATUS,
    }