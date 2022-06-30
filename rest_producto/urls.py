from django.urls import path
from rest_producto.views import lista_productos, detalle_producto

#Detalle y lista de los productos creados 29/06 20:56

urlpatterns =[
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
]
