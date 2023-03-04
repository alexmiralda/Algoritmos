from SimpleStack import *

stack = Stack(100) # Create a stack to hold letters

word = input("Word to reverse: ")

word = word.lower() #Convierte toda la palabra a minusculas
word = word.replace(" ", "") #Quita los espacios
                                 #Reemplaza lo de la izquierda, por lo de la derecha
word = word.replace("á", "a")
word = word.replace("é", "e")
word = word.replace("í", "i") #Quita las tildes 
word = word.replace("ó", "o")
word = word.replace("ú", "u")

for letter in word: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(letter)
reverse = '' # Build the reversed version

while not stack.isEmpty(): # by popping the stack until empty
    reverse += stack.pop()
    reverse = reverse.lower()
    reverse = reverse.replace(" ", "")

print('The reverse of', word, 'is', reverse)

def palindromo(word):
    
    word = word.lower() #Convierte toda la palabra a minusculas
    word = word.replace(" ", "") #Quita los espacios
                                 #Reemplaza lo de la izquierda, por lo de la derecha
    word = word.replace("á", "a")
    word = word.replace("é", "e")
    word = word.replace("í", "i") #Quita las tildes 
    word = word.replace("ó", "o")
    word = word.replace("ú", "u")
    
    #RECONOCER
    
    a = 0
    b = len(word) - 1

    for i in range(0, len(word)):
        if word[a] == word[b]:
            a += 1        
            b -= 1
        else:
            return print("No es palindromo")     
    return print("Si es palindromo")


print(palindromo(word))
