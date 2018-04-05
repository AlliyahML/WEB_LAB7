from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^student/$',views.full_student_listing),
    url(r'^students/new/$',views.add_student, name='student_new'),
]