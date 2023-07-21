"""
    Escribir una función empaquetar para una lista, donde epaquetar significa indicar la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). 
    Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)].
"""

def empaquetar(lista):

    lista_empaquetada = []
    contador = 1
    longitud = len(lista) - 1
   
    for i in range(0, longitud):  
        if lista[i] == lista[i+1]:
            contador += 1
        else:
            lista_empaquetada.append((lista[i],contador))
            contador = 1   

        if i == longitud - 1:
            lista_empaquetada.append((lista[i+1],contador))

    return lista_empaquetada


print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3, 3, 8]))