from Colas import *

qd = Colas(1)

#Inserta los elementos a la derecha
print("Inserta elementos a la derecha")
qd.insder(19)
qd.insder(36)
qd.insder(65)
qd.insder(74)
qd.insder(40)
qd.mostrar()
print("")

#Inserta los elemtos a la izquierda
print("Inserta elementos a la izquierda")
qd.insIzq(9)
qd.insIzq(51)
qd.insIzq(10)
qd.insIzq(8)
qd.mostrar()
print("")

#Remueve un elemento de la derecha
print("Remueve un elemento de la derecha")
qd.remder()
qd.mostrar()
print("")

#Remueve un elemento de la izquierda
print("Remueve un elemento de la izquierda")
qd.remIzq()
qd.mostrar()
print("")

#Realiza un intercambio, el ultimo pasa primero
print("Realiza un intercambio, el ultimo pasa primero")
qd.intderecha()
qd.mostrar()
print("")

#Realiza un segundo intercambio, el ultimo pasa primero
print("Realiza un segundo intercambio, el ultimo pasa primero")
qd.intderecha()
qd.mostrar()
print("")

#Realiza un intercambio, el primero pasa a ultimo
print("Realiza un intercambio, el primero pasa a ultimo")
qd.intizquierda()
qd.mostrar()
print("")

#Realiza un segundo intercambio, el primero pasa a ultimo
print("Realiza un segundo intercambio, el primero pasa a ultimo")
qd.intizquierda()
qd.mostrar()
print("")

#Prueba de peekderecha
print("Devuelve el valor del ultimo: (peek derecha)")
qd.peekderecha()
print("")

#Prueba de peekizquierda
print("Devuelve el valor del primero: (peek izquierda)")
qd.peekizquierda()
print("")

#Comprueba si la lista esta vacia
print("Comprueba si la lista esta vacia: ")
print(qd.isEmpty())
print("")

#Comprueba si la cola esta llena
print("Comprueba si la cola esta llena: ")
print(qd.isFull())
print("")

