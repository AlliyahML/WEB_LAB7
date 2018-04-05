import uuid
from django.db import models
from django.db.models import(
   UUIDField,
   CharField,
   IntegerField, 
   BooleanField,
   DateTimeField
)

class Courses(models.Model):
    id= UUIDField(primary_key=True,default = uuid.uuid4, editable= False)
    name =CharField(max_length= 20)
    credit = IntegerField(default=3)
    isActive= BooleanField(default= True)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)
