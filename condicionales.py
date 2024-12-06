lista= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
lista.extend([21,22,23])
for i in range(len(lista)):
    print(lista[i])

elemento = input("agregar elemntos a la lista\n")
lista.append(float(elemento))
print(lista)