from django.urls import path 
from . import views 

urlpatterns =[
    path('',views.note_list),
    path('notes/<int:pk>',views.note_particular),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),

]