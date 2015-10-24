# -*- coding: UTF-8 -*-
import datetime

from peewee import *

zidian_db_path = "test.db"
db = SqliteDatabase(zidian_db_path)


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

db.connect()
db.create_tables([User, Tweet])

##################################################
# 直接保存
huey = User(username='huey')
huey.save()

# 关联保存
charlie = User.create(username='charlie')
Tweet.create(user=charlie, message='My first tweet')
##################################################