from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User

class UserRepository:

    async def create_user(self, db_session: AsyncSession, user_data: dict):
        try:
            new_user = User(**user_data)
            db_session.add(new_user)
            await db_session.commit()
            await db_session.refresh(new_user)

            return new_user

        except Exception as e:
            await db_session.rollback()
            raise e
