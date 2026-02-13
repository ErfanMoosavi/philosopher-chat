from pydantic import BaseModel


class UserCredentials(BaseModel):
    username: str
    password: str


class UserNameUpdate(BaseModel):
    name: str


class UserAgeUpdate(BaseModel):
    age: int


class ChatCreate(BaseModel):
    chat_name: str
    philosopher_id: int


class ChatRef(BaseModel):
    chat_name: str


class ChatInput(BaseModel):
    input_text: str
