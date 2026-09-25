import sqlalchemy

from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository
from schemas.user_schema import RegisterUserSchema
from utils.logger import logger
from utils.encrypt import hash_password

from typing import Optional

class UserService:

    def __init__(self, repository: Optional[UserRepository] = None):
        self.repository = repository or UserRepository()
    

    async def register_user(self, db_session: AsyncSession, user_data: RegisterUserSchema):
        try:
            user_dict = user_data.model_dump(exclude_unset=True)

            user_dict["password"] = hash_password(user_dict["password"])

            # Returned as a dict
            created_user = await self.repository.create_user(db_session, user_dict)

            if created_user:

                logger.log(f"Created user {created_user["email"]}", level="warn", detail=True)

                return created_user

        except sqlalchemy.exc.IntegrityError as ie:
            raise ValueError("The email is already in use")
        except Exception as e:
            raise e