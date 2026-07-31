from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.crud import get_user_by_id, get_user_by_email, get_user_by_username


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    user_id: int | None = None,
    email: str | None = None,
    username: str | None = None,
):
    """
    Dependency to get the current user by ID, email, or username.
    """
    if user_id:
        user = await get_user_by_id(db, user_id)
    elif email:
        user = await get_user_by_email(db, email)
    elif username:
        user = await get_user_by_username(db, username)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Must provide user_id, email, or username",
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
