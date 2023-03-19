from datetime import datetime, timedelta
from jose import jwt, jwk, JWTError
from core.contracts import schemas 

SECRET_KEY = "BY9-yXXFwaOnkpzKPv5sKEMxaRkqRtOjJFDRJLfYbAI"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 30


def create_access_token(payload: dict, expire_time: timedelta | None = None):
    to_encode = payload.copy()
    if expire_time:
        expire = expire_time + datetime.utcnow()
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str, check_credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("username")
        email: str = payload.get("unique_name")

        if username is None:
            raise check_credential_exception
        token_data = schemas.TokenData(username=username, email=email)
        return username
    except JWTError:
        raise check_credential_exception