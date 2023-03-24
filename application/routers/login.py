from fastapi import APIRouter, Depends, HTTPException, status

from core.contracts import models, schemas
from core.service import get_db
from core.service import token
from core.service.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

ACCESS_TOKEN_EXPIRE_MINUTE = 30

router = APIRouter(
    tags=["Authentications"]
)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.Users).filter(models.Users.username==form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user name or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not Hash.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},)
    
    # We will create access token with expire time
    token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    payload = {"username": user.username}
    access_token = token.create_access_token(payload, token_expire)
    return {"access_token": access_token, "token_type": "bearer"}