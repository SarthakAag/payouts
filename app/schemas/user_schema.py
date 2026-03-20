from pydantic import BaseModel, constr

class RegisterUser(BaseModel):
    full_name: str
    delivery_partner_id: str
    email: str
    password: constr(min_length=6, max_length=72)
    platform: str
    age: int


class LoginUser(BaseModel):
    email: str
    password: constr(min_length=6, max_length=72)
