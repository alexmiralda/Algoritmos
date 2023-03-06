class Colas(object):

    #Creamos una lista 
    def __init__ (self, max):
        self.__items = [] * max

    #Metodo para mostrarlos
    def mostrar (self):
        print(self.__items)
    
    #Inserta elementos a la derecha
    def insder (self, item): 
        self.__items.append(item)

    #Inserta elementos a la izquierda
    def insIzq(self, item): 
        if self.__items == None:
            self.item.append(item)
        else:
              n = len(self.__items)
              self.__items.insert(0, item)
    
    #Remueve el elemento de la izquierda 
    def remIzq (self):
        try:
            return self.__items.pop(0)
        except:
            raise ValueError("La cola está vacía")
        
    #Remueve el elemento de la derechca    
    def remder (self):
        try:
            n = len(self.__items)
            p = n - 1
            return self.__items.pop(p)
        except:
            raise ValueError("La cola está vacía")
           
    #Verifica si la cola esta vacia    
    def isEmpty(self): 
        n = len(self.__items)
        if n == 0:
            return True
        else:
            return False
        
    #Verifica si la cola esta llena 
    def isFull(self): 
         j = len(self.__items) - 1
         if -1 >= j:
             return True
         else:
             return False

    #Toma el elemento de la derecha y lo lleva a la izquierda
    def peekder(self):
         n = len(self.__items)
         p = n - 1
         self.__items.insert(0, self.__items[p])
         self.__items.pop()

    #Toma el elemento de la izquierda y lo lleva a la derecha     
    def peekIzq(self):
         n = len(self.__items)
         p = n 
         self.__items.insert(p, self.__items[0])
         self.__items.pop(0)
            
             