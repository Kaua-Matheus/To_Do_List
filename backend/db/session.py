from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base)

async def get_db_session():
    async with AsyncSessionLocal() as db_session:
        yield db_session