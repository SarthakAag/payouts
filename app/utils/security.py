from passlib.context import CryptContext

# PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

BCRYPT_MAX_BYTES = 72


def _bcrypt_normalize(password: str) -> bytes:
    encoded = password.encode("utf-8")
    if len(encoded) > BCRYPT_MAX_BYTES:
        raise ValueError(
            f"Password too long for bcrypt (max {BCRYPT_MAX_BYTES} bytes). "
            "Please choose a shorter password."
        )
    return encoded


def hash_password(password: str):
    normalized = _bcrypt_normalize(password)
    return pwd_context.hash(normalized)


def verify_password(plain_password: str, hashed_password: str):
    normalized = _bcrypt_normalize(plain_password)
    return pwd_context.verify(normalized, hashed_password)