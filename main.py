from datetime import datetime
from fastapi import FastAPI
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise
from model import User, UserIn_Pydantic, User_Pydantic
import json


app = FastAPI()

 #________________hier wird eine  Connection inerzializerd und mit der DatenBank verbunden_______________#


register_tortoise(
    app,
    db_url='sqlite://tortoise.db',
    modules={"models":["model"]},
    generate_schemas=True,
    add_exception_handlers=True
)

 


@app.post('/create/new_user')
async def create(user: UserIn_Pydantic):


#________________hier wird eine  user inerzializerd und in der DatenBank gespeichert_______________#


    new_object = await User.create(**user.dict(exclude_unset=True)) 
    return await User_Pydantic.from_tortoise_orm(new_object)





@app.get('/user/data')
async def read():


#________________hier wird alle  user aus der DatenBank abgrufen__________________#


    return await User_Pydantic.from_queryset(User.all()) 





@app.get('/user/{user_id}')
async def read_by_id(user_id:int):


#__________________hier wird eine  user mit seiner ID aus der DatenBank abgrufen______________#


    return await User_Pydantic.from_queryset_single(User.get(id=user_id)) 





@app.put('/user/{user_id}')
async def update(user_id:int, user: UserIn_Pydantic):



#_______________hier wird eine  user mit seiner ID aus der DatenBank abgrufen und geändert_________________#


    updated_data = await User.filter(id= user_id).update(**user.dict(exclude_unset=True))
    return f'The User with Id: {user_id} has been Successful updated: {updated_data}'



@app.delete('/user/{user_id}')
async def delete(user_id:int):


#_______________hier wird eine  user mit seiner ID aus der DatenBank gelöscht________________#



    delete_data = await User.filter(id= user_id).delete() 
    return f'The User with Id: {user_id} has been Successful deleted: {delete_data}'