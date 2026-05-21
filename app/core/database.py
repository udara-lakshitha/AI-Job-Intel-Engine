from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

class Base(DeclarativeBase):
    pass

class UserSpecification(Base):
    __tablename__ = "user_specifications"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    email: Mapped[str] = mapped_column(String(255), nullable = False, unique = True)
    skills: Mapped[str] = mapped_column(Text, nullable = False)
    qualifications: Mapped[str] = mapped_column(Text, nullable = False)
    is_subscribed: Mapped[bool] = mapped_column(Boolean, default = True)

class JobPost(Base):
    __tablename__ = "job_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    job_key: Mapped[str] = mapped_column(String(255), unique = True, nullable = False)
    title: Mapped[str] = mapped_column(String(255), nullable = False)
    company: Mapped[str] = mapped_column(String(255), nullable = False)
    url: Mapped[str] = mapped_column(String(500), nullable = False)
    requirements: Mapped[str] = mapped_column(Text, nullable = False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, default = lambda: datetime.now() + timedelta(days = 7))

class UserJobMatch(Base):
    __tablename__ = "user_job_matches"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user_specifications.id", ondelete = "CASCADE"),
        nullable = False
    )
    job_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("job_posts.id", ondelete = "CASCADE"),
        nullable = False
    )
    is_notified: Mapped[bool] = mapped_column(Boolean, default = False)

engine = create_async_engine(settings.DATABASE_URL)
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
