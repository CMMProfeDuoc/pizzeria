"""
Una pizzeria se instala en DUOC. Es su trabajo crear un programa para realizar pedidos

Para esto, el programa debe mostrar la lista de pizzas (dada a usted) y el precio de cada una de estas.
Luego, debe preguntar al usuario que tipo de usuario es.

Una vez que el usuario elije todas las pizas que desee comprar, se le aplicarán
descuentos segun lo siguiente:

Si el usuario es tipo "estudiante": 20% de descuento al total de la compra
Si el usuario es tipo "profesor": 10% de descuento al total de la compra

Si lleva 3 pizzas "Napolitanas", solo paga 2
Si lleva 2 pizzas de "Pepperoni", 10% de descuento al total de la compra

Los descuentos se acumulan.

Una vez que un usuario compra sus pizzas, se puede pasar a otro usuario o finalizar el programa.
El programa debe mostrar el total de las ganancias (las ventas totales de todos los usuarios)

Puede asumir que el usuario ingresa bien los datos
NO puede usar ninguna libreria
"""

#Pizas y precios de cada una
# Tradicional 12000
# Pepperoni 14000
# Margarita 12500
# Napolitana 11000
# Carnes 17000

pizzas = [["Tradicional",12000],["Pepperoni",14000],["Margarita",12500],["Napolitaba",11000],["Carnes",17000]]
jugos = [["Piña",1000],["Frambuesa",1100]]

def imprimirLista (lista:list, nombre_lista:str) -> None:
	print("----",nombre_lista,"----")
	for elemento in lista:
		print(lista.index(elemento)+1, elemento[0], "$ ", elemento[1])

def comprarItem (lista:list) ->
	tam_lista = len(lista)
	sel = int(input(">> "))-1
	if (sel in range(0,tam_lista)):
		print("Ha seleccionado",lista[sel][0])
		return lista[sel][1]
	else:
		print("Compra no valida")
		return 0