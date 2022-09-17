from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator




class User(Model):
    id                                    =fields.IntField(pk =True)
    email                                 = fields.CharField(max_length=50)
    username                              = fields.CharField(max_length=50, unique=True)
    password                              = fields.CharField(max_length=255)
    data_joind                            = fields.DateField()


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn',exclude_readonly=True)