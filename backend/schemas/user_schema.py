from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    email: str

class RegisterUserSchema(BaseModel):
    email: str
    password: str