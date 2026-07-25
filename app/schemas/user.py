from pydantic import BaseModel


class UserResponse(BaseModel):
    """
    Response model for a user.
    """

    id: int
    name: str
    email: str