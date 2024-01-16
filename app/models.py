from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(String(8000))
