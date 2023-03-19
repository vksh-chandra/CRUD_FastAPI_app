from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from core.service import get_db
from core.contracts import schemas, models
from sqlalchemy.orm import Session
from application import oauth2
from core.logics import items

router = APIRouter(
    prefix="/item",
    tags=['Items'],
    # dependencies = Depends(oauth2.get_current_user)
)


# Create items
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Item, db : Session = Depends(get_db), current_users: schemas.Users = Depends(oauth2.get_current_user)):
    return items.create(request, db, current_users)


# fetch all items
@router.get('/', status_code=200, response_model=List[schemas.ShowItem])
def get_all(db: Session = Depends(get_db), current_user: schemas.Users = Depends(oauth2.get_current_user)):
    return items.get_all_item(db)


# Read Item
@router.get('/{id}', status_code=200, response_model=schemas.ShowItem)
def get_item(id: int, db: Session = Depends(get_db), current_users: schemas.Users = Depends(oauth2.get_current_user)):
    res = items.get_item(id, db)

    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    return res


# Update Item
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Item, db: Session = Depends(get_db), current_user: schemas.Users = Depends(oauth2.get_current_user)):
    res = items.update(id, request, db)

    if res == "error":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    return res


# Delete Item
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    res = items.delete_item(id, db)

    if res == "error":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    return "done"



