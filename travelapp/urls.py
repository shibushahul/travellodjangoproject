from . import views
from django.urls import path
urlpatterns=[
    path('',views.demo,name='demo'),
    path('about/',views.about,name='about'),









    # path('add/',views.addition,name='addition'),
    # path('sub/',views.subtraction,name='subtraction'),
    # path('multiple/',views.multiplication,name='multiplication'),
    # path('div/',views.division,name='division')
    # # path('contact/',views.contact,name='contact')
]