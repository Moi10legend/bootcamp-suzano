#set  retira os elementos repetidos de uma lista

set([1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9])
set("Raposa")

numeros = {1, 2, 3, 4}

#Conversão de set para lista

numeros = list(numeros)

#Métodos de conjuntos

#union faz a união de dois conjuntos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

#intersection pega a interceção de dois conjuntos

conjunto_c = {1, 3, 5}
conjunto_a.intersection(conjunto_c)

#difference retira todos os itens em comum nos dois conjuntos

conjunto_a.difference(conjunto_c)

#symmetric_difference retira todos os elementos da intersecção de dois conjuntos

conjunto_a.symmetric_difference(conjunto_c)

#issubset verifica se um conjunto está contido em outro

conjunto_d = {-5, 0, 1, 2, 4, 8, 9, 10 }
conjunto_a.issubset(conjunto_d) #retorna true pois o conjunto a está contido em b

#issuperset verifica se todos os elementos de um conjunto está no outro, o contrário do issubset

conjunto_d.issuperset(conjunto_a) #Todos os elementos de A estão em D?

#isdisjoint verifica se há nenhum elemento em comum com outro conjunto

conjunto_a.isdisjoint(conjunto_b) #retorna true pois nenhum elemento de A está em B e vice versa.

#add adiciona elementos que já não estejam no conjunto

conjunto_d.add(35)

#clear limpa todos os elementos do conjunto

conjunto_e = {"oi", "Olá", "hello"}
conjunto_e.clear()

#copy faz uma cópia do conjunto com id diferente

conjunto_a_copy = conjunto_a.copy()

#discard descarta um valor em específico

conjunto_a_copy.discard(1)

#pop remove o primeiro item da lista

conjunto_d.pop()

#remove mesma coisa do discard, só irá dar erro quando pedimos para remover um elemento que não existe

conjunto_d.remove(-5)

#len retira o tamanho do conjunto 

len(conjunto_d)

#in verifica se um elemento está em um conjunto

1 in conjunto_d