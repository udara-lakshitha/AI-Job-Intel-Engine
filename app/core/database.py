from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class Base(DeclarativeBase):
    pass

class ProcessedJob(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    job_key: Mapped[str] = mapped_column(String(255), unique = True, nullable = False)
    title: Mapped[str] = mapped_column(String)
    company: Mapped[str] = mapped_column(String)

DATABASE_URL = "sqlite+aiosqlite:///./job_intel.db"

engine = create_async_engine(DATABASE_URL)

session = async_sessionmaker(bind = engine, expire_on_commit = False)
