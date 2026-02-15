from django.urls import path
from .views.auth_view import login_method, register_method
from .views.main_view import index_method,about_method,create_product

urlpatterns = [ 
    path('login/',login_method, name="login"),
    path('register/',register_method, name="register"),
    path('',index_method, name="index"),
    path('about/',about_method),
    path('create/',create_product, name="create")
]
