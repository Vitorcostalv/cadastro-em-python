
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota,view responsavel, nome de referencia
    # Manter em mente oque vem depois 
    #facebook.com/testecadastro
    #usuarios.com
    path('',views.home, name='home'),
]
