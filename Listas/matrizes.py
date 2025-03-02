matriz = [

    ["","A", "B", "C"],
    [1, "1A", "1B", "1C"],
    [2, "2A", "2B", "2C"],

]

print(matriz[0][2])

#Fatiamento

lista = ["p", "y", "t", "h", "o", "n"]
parte1_da_lista = lista[0:4]

print(parte1_da_lista)

#percorrendo a lista

avioes = ["A330", "A350", "Boeing 777", "Boeing 787"]

for indice, aviao in enumerate(avioes):
    print(f"{indice}: {aviao}")

#filtro

numeros = range(11)

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)