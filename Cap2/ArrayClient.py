import Array
maxSize = 10  # Max size of the array
arr = Array.Array(maxSize)  # Create an array object
arr.insert(7)  # Insert 10 items
arr.insert(999)
arr.insert(7)
arr.insert("baz")
arr.insert(7)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("fuego")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()
print("Search for 12 returns", arr.search(12))
print("Search for 12.34 returns", arr.search(12.34))
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))
print("Setting item at index 3 to 33")
arr.set(3, 33)
print("El numero mayor es: ", arr.get_max())
print("El numero mayor se borro: ", arr.delete_max_num())
print("La lista ordenada queda de la siguiente forma:") 
print("La lista sin repetidos queda asi: ", arr.remove_dupes()) 


#print("Mostrar prueba: ", arr.mostrar())   
#print("Array after deletions has", len(arr), "items")
#arr.traverse()
#print("La lista que queda es: ", arr.mostrar())