class Array(object):
    
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially
    
    def __len__(self):  # Special def for len()func
        return self.__nItems  # Return number of items
    
    def get(self, n):  # Return the value at indexn
    
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds and 
            return self.__a[n]  # only return item if in bounds
        
    def set (self, n, value):  # Set the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds, and
            self.__a[n] = value  # only set item if in bounds

    def insert(self, item):  # Insert item at end
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
        
        for k in range(j, self.__nItems):  # Move items from
            self.__a[k] = self.__a[k+1]  # right over 1
            return True  # Return success flag
        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a functionfunction
            (self.__a[j])
            
#Ejercicios 
#2.1
#2.2
#2.4

    #Ejercicio 2.1
    def get_max(self): #Obtiene el numero mayor de la lista

        mayor = self.__a[0]

        for j in range(self.__nItems):

            if self.__a[j] > mayor:
                mayor = self.__a[j]

        return mayor
    
    #Ejercicio 2.2
    def delete_max_num(self): #Elimina el numero mayor de la lista
        mayor = self.__a[0]

        for j in range (self.__nItems):

            if self.__a[j] > mayor:
                mayor = self.__a[j]
                del self.__a[j]       

        #for j in range(self.__nItems):

            #print(self.__a[j])

        return self.__a
    
    #Ejercicio 2.4
    def remove_dupes(self):  #Elimina los duplicados de la lista

        self.__a = list(set(self.__a)) #Convertimos la lista a un conjunto para eliminarlos

        return self.__a

    

    #def orden (self):
        #for j in range(self.__nItems):
            #j=0
           # while j < self.__a[j]:
            #    self.__a[0] == j
        #return self.__a

    #def mostrar(self):

        #for j in range(self.__nItems):

            #print(self.__a[j])

        #return self.__a

    


    