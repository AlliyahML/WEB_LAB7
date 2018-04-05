import uuid
from django.db import models
from django.db.models import(
    UUIDField,
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField
)

class Student(models.Model): # creating a class,  models is coming from Models.py
    id = UUIDField(primary_key=True, default = uuid.uuid4, editable= False)

    name= CharField(max_length = 100)
    countrycode = CharField(max_length=3, blank = False, default = 'TTD')
    isActive = BooleanField(default= False)
    started=IntegerField()
    created= DateTimeField(auto_now_add=True)
    UNDERGRAD= "UG"
    POSTGRAD="PG"
    LEVEL_CHOICE= (
        (UNDERGRAD,"Undergraduate"),
        (POSTGRAD,"Postgraduate")
    )

    level = CharField(
        max_length=2,
        choices=LEVEL_CHOICE,
        default = UNDERGRAD,
    )

    def __str__(self):
        return "{}".format(self.name)

