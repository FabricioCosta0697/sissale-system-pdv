from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.db.deps import get_db
from app.models.user import User
from app.schemas.auth import Token

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    token = create_access_token(subject=str(user.id), extra_claims={"role": user.role, "tenant_id": user.tenant_id})
    return Token(access_token=token)
