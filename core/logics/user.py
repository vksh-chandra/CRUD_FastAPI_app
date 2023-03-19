from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from core.service.hashing import Hash
from core.contracts import schemas, models


def create(request: schemas.Users, db: Session):
    try:
        hash_password = Hash.get_password_hashed(request.password) 
        new_user = models.Users(username = request.username,
                            email = request.email, 
                            full_name = request.full_name, 
                            hashed_password = hash_password, 
                            disabled = request.disabled
                            )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        return None
        
        
def show(username: str, db: Session):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        return None
    return user