from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "nick",
    "email": "nickmello@mail.ru",
}


user = User(**user_data)
print(user)


# invalid_user_data = {
#     "id": 'asd',
#     "username": "nick",
#     "email": "nickmello@mail.ru"
# }
#
# invalid_user = User(**invalid_user_data)
# print(invalid_user)