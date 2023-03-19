from sqlalchemy.orm import Session
from core.contracts import schemas, models

def get_all_item(db: Session):
    items = db.query(models.Item).all()
    return items


def create(request: schemas.Item, db: Session, current_user : str):
    new_item = models.Item(name= request.name, description = request.description, price = request.price, username=current_user)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_item(id: int, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    return item


def update(id: int, request: schemas.Item, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id)

    if not item.first():
        return "error"

    item.update(request.dict())
    db.commit()
    return "Updated"


def delete_item(id: int, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id)

    if not item.first():
        return "error"
    
    item.delete(synchronize_session=False)
    db.commit()
    return "Item Deleted"
