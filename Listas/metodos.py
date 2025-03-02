#append  adiciona elementos à lista

lista1 = []

lista1.append(1)
lista1.append(30)

#copy cria uma lista com os mesmos valores de outra mas com um id diferente

lista2 = lista1.copy()

#count conta quantas vezes um objeto aparece na sua lista

cores = ["Azul", "Amarelo", "Amarelo", "Amarelo", "Azul", "Vermelho", "Verde", "Amarelo"]

print(cores.count("Azul"))

#extend coloco mais de um elemento de uma vez na lista

lista1.extend([-6, -9, -10])
print(lista1)

#index  vejo em que posição está um objeto dentro da lista, a primeira ocorrência.

lista1.index(-10)

#pop  retira o último elemento selecionado quando está sem o indíce

lista1.pop() 
lista1.pop(2)

#remove remove o objeto desejado, a primeira ocorrência

lista1.remove(-9)

#reverse Ele espelha a lista, os últimos objetos se tornam o primeiro

cores.reverse()

#sort  ordena os objetos em ordem alfabética

cores.sort()
cores.sort(reverse=True) #inverte a ordem alfabética
cores.sort(key=lambda x: len(x)) #vai ordenar da menor palavra até a maior
cores.sort(key=lambda x: len(x), reverse=True) #vai ordenar da maior palavra até a menor

#len pega o tamanho das coisas

len(cores) #vai retornar o tamanho da lista
len("Ei pessoal") #Retorna o tamanho da string

#sorted serve para a ordenar, igual ao sort porém é uma função.

sorted(cores)