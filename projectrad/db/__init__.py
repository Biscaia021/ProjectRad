from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(320))
    hash: Mapped[str] = mapped_column(String(128))

