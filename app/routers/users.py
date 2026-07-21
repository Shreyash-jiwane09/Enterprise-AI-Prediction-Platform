"""
User router for the Enterprise AI Prediction Platform.

This module contains user-related API endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

USERS = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie@example.com",
    },
]


@router.get("")
async def get_users() -> list[dict[str, object]]:
    """
    Retrieve all users.

    Returns:
        list[dict[str, object]]: A list containing all users.
    """
    return USERS


@router.get("/{user_id}")
async def get_user(user_id: int) -> dict[str, object]:
    """
    Retrieve a user by their unique identifier.

    Args:
        user_id: The unique identifier of the user.

    Returns:
        dict[str, object]: The matching user if found.
    """
    for user in USERS:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail=f"User with ID {user_id} not found.",
    )