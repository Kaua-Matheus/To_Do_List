import sqlalchemy

from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository
from schemas.user_schema import RegisterUserSchema
from typing import Optional

class UserService:

    def __init__(self, repository: Optional[UserRepository] = None):
        self.repository = repository or UserRepository()
    

    async def register_user(self, db_session: AsyncSession, user_data: RegisterUserSchema):
        try:
            user_dict = user_data.model_dump(exclude_unset=True)

            created_user = await self.repository.create_user(db_session, user_dict)

            if created_user:
                # Exclude, only debug
                print("User created..")

        except sqlalchemy.exc.IntegrityError as ie:
            raise ValueError("The email is already in use")
        except Exception as e:
            raise e