from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, Depends, status, APIRouter, HTTPException

from core.logics import user
from core.service import engine, SessionLocal, get_db
from core.contracts import schemas
from core.service.hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# Sign up to start
@router.post("/", response_model=schemas.ShowUser)
async def sign_up(request: schemas.Users, db:Session = Depends(get_db)):
    new_user = user.create(request=request, db=db)
    if new_user == None:
        raise HTTPException(status_code=400, detail="User already exist")
    else:
        return new_user
    

@router.get("/{username}", response_model=schemas.ShowUser)
async def show(username: str, db: Session = Depends(get_db)):
    # Fetch users data from database
    user_res = user.show(username=username, db=db)
    if user_res == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the username {username} is not available")
    else:
        return user_res
