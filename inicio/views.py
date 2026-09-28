from django.shortcuts import render

# Create your views here.
def index(request):
	productos = [
		{'id': 1, 'nombre': 'Producto 1', 'descripcion': 'Descripción del producto 1', 'precio': 10.99, 'stock': 5},
		{'id': 2, 'nombre': 'Producto 2', 'descripcion': 'Descripción del producto 2', 'precio': 11.99, 'stock': 15},
		{'id': 3, 'nombre': 'Producto 3', 'descripcion': 'Descripción del producto 3', 'precio': 12.99, 'stock': 25},
	]
	return render(request, 'inicio/default.html', {'productos': productos})