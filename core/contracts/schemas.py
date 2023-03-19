from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name: str
    description: str
    price : float


class Item(ItemBase):
    class Config():
        orm_mode = True


class Users(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    password: str


class ShowUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    # items : List[Item] = []
    
    class Config():
        orm_mode = True


class ShowItem(BaseModel):
    name: str
    description: str
    creator : ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str


# paylaod define kr rahe yaha
class TokenData(BaseModel):
    username: str | None = None

