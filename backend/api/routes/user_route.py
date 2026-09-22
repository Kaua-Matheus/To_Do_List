from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from services.user_service import UserService
from schemas.user_schema import UserSchema, RegisterUserSchema

from db.session import get_db_session

router = APIRouter()
user_service = UserService()

@router.post("/register", response_model=UserSchema)
async def register_user(user_data: RegisterUserSchema, db_session: AsyncSession = Depends(get_db_session)):
    try:
        return await user_service.register_user(db_session, user_data)
    except Exception as e:
        raise e