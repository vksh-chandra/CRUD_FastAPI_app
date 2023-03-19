from core.service import token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

"""
Let's validate the user
"""

def get_current_user(token_data: str = Depends(oauth2_scheme)):
    check_credential_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "Could not validate credential",
        headers={"WWW-Authenticate":"Bearer"},
    )

    return token.verify_token(token_data, check_credential_exception)
