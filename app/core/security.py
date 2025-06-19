from datetime import timedelta
from jose import jwt
from passlib.context import CryptContext
from typing import Optional

# -------- ajustes --------
SECRET_KEY = "troque-por-uma-chave-secreta-grande"
ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
# -------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta:  Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = timedelta(minutes=expires_delta)
    else:
        expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": (jwt.datetime.utcnow() + expire)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
