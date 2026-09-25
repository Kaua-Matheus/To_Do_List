from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User

class UserRepository:

    # View Operations

    async def get_user_by_id(self, db: AsyncSession, user_id: int) -> User:
        try:
            return await db.get(User, user_id)
            
        except Exception as e:
            raise e


    # Create Operations

    async def create_user(self, db: AsyncSession, user_data: dict) -> User:
        try:
            new_user = User(**user_data)
            await db.add(new_user)
            await db.commit()
            await db.refresh(new_user)

            # Test
            # return new_user.__dict__
            return new_user

        except Exception as e:
            await db.rollback()
            raise e
        
    # Delete Operations

    async def delete_user(self, db: AsyncSession, user_id: int) -> bool:
        try:

            user = await db.get(User, user_id)
            if user is None:
                return False
            
            await db.delete(user)
            await db.commit()
            return True

        except Exception as e:
            raise e
