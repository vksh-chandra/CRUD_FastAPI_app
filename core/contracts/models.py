from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from core.service import Base
from sqlalchemy.orm import relationship

#we wil create a structre of database table here
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    username = Column(String, ForeignKey('users.username'))

    creator = relationship("Users", back_populates = "items")


class Users(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key = True, index = True)
    email = Column(String, unique = True, index=True)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)

    items = relationship("Item", back_populates = "creator")

