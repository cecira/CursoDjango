from django.urls import path
from .views import lista_de_clientes

urlpatterns = [
    path(' ',lista_de_clientes),
    path('adicionar_cliente/',adicionar_cliente)
    path('editar_cliente/<int:id>',editar_cliente)
]
