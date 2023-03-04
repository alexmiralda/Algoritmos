from SimpleStack import*

pila = Stack(4)

print("   Haciendo push en la pila  ")
pila.push("w")
pila.push("a")
pila.push("s")
pila.push("d")
print("Pila: ", pila)

print("   Haciendo pop en la pila  ")
pila.pop()
pila.pop()
pila.pop()
pila.pop()
print("Pila: ", pila)

#Descomentar la excepcion que se desee probar(uno a la vez).

#print("   Mostrando la exception en un pop")
#pila.pop()
#print("Pila:", pila) 

"""Al hacer pop(sacar un elemento) en el stack vacio nos debe mostrar la excepcion"""



#print("   Mostrando la exception en un push")
#pila.push("t")
#pila.push("t")
#pila.push("t")
#pila.push("t")
#pila.push("t")
#print("Pila:", pila)

"""Al realizar push(colocar un elemento) más veces de la cantidad definida en el stack
,en este caso 4, nos debe mostrar la excepcion"""