"""
User router for the Enterprise AI Prediction Platform.

This module contains user-related API endpoints.
"""

from fastapi import APIRouter, HTTPException, status, Response
from app.schemas.user import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

USERS = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "password": "secret123"
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


@router.get("",
            response_model=list[UserResponse])
async def get_users() -> list[dict[str, object]]:
    """
    Retrieve all users.

    Returns:
        list[dict[str, object]]: A list containing all users.
    """
    return USERS


@router.get("/{user_id}",
             response_model=UserResponse,)
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


@router.post(
        "",
         status_code=status.HTTP_201_CREATED,)
async def create_user(user: dict[str, str]) -> dict[str, object]:
    """
    Create a new user.

    Args:
        user: The user data received in the request body.

    Returns:
        dict[str, object]: The created user.
    """
    new_id = len(USERS) + 1

    new_user = {
        "id": new_id,
        "name": user["name"],
        "email": user["email"],
    }

    USERS.append(new_user)

    return new_user


@router.put("/{user_id}")
async def update_user(
    user_id: int,
    user: dict[str, str],
) -> dict[str, object]:
    """
    Replace an existing user.
    """
    for existing_user in USERS:
        if existing_user["id"] == user_id:

            existing_user["name"] = user["name"]
            existing_user["email"] = user["email"]

            return existing_user

    raise HTTPException(
        status_code=404,
        detail=f"User with ID {user_id} not found."
    )


@router.patch("/{user_id}")
async def patch_user(
    user_id: int,
    user: dict[str, str],
) -> dict[str, object]:
    """
    Partially update an existing user.
    """
    for existing_user in USERS:
        if existing_user["id"] == user_id:

            if "name" in user:
                existing_user["name"] = user["name"]

            if "email" in user:
                existing_user["email"] = user["email"]

            return existing_user

    raise HTTPException(
        status_code=404,
        detail=f"User with ID {user_id} not found."
    )


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
) -> Response:
    """
    Delete an existing user.
    """
    for existing_user in USERS:
        if existing_user["id"] == user_id:

            USERS.remove(existing_user)

            return Response(
                status_code=status.HTTP_204_NO_CONTENT,
            )

    raise HTTPException(
        status_code=404,
        detail=f"User with ID {user_id} not found."
    )