"""
Root router for the Enterprise AI Prediction Platform.

This module contains the root endpoint that provides a welcome
message and basic information about the API.
"""

from fastapi import APIRouter

from app.types import ResponseMessage

router = APIRouter(
    tags=["Root"],
)


@router.get("/")
async def get_root() -> ResponseMessage:
    """
    Return the root endpoint response for the Enterprise AI Prediction Platform.

    Returns:
        ResponseMessage: A welcome message for API consumers.
    """
    return {
        "message": "Welcome to the Enterprise AI Prediction Platform API!"
    }