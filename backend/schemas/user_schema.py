from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str

class RegisterUserSchema(BaseModel):
    email: str