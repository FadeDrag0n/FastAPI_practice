import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra= 'forbid')

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {'success': True, 'message': 'User added!'}

@app.get("/users")
def get_users() -> list[UserSchema]:
    return users

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)