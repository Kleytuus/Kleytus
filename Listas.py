from audioop import reverse

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[2:5]) #Exepciones de datos
print(lista[5:])

lista = [1,2,3,4,5,6,7,8,9,10]
lista.insert(2, "nuevo") #Inserta un dato en una ubicación especifica
lista.append("final") #Agrega un dato al final
print(lista)

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = ["a", "b"]
lista.extend(lista2) #Junta listas
print(lista)

numeros = [4,2,61,6,7,43]
numeros.sort() #menor a mayor
numeros.reverse() #mayor a menor
print(numeros)

numeros = [4,2,61,6,7,43]
print(numeros.index(61)) #La ubicacion del dato

numeros = [4,2,61,6,7,43]
print(numeros.pop()) #Elimina todos los datos y deja el último
eliminar = numeros.pop(2)
print(numeros)
print(eliminar)