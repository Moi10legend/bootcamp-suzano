pessoa = {"nome": "Moisés", "Idade": 18, "Cidade": "Recife"}

#adicionando uma chave ao dicionário

pessoa["Telefone"] = "(81) 985559400"

#acessando um valor do dicionário

print(pessoa["Cidade"])

#percorrendo um dicionário

for chave, valor in pessoa.items:
    print(chave, valor)

#métodos

#.clear() apaga todos os valores do dicionário

#.copy() faz uma cópia do dicionário com id diferente

#.fromkeys() cria chaves no dicionário

pessoa.fromkeys(["Estado", "Sexo"]) #cria chaves sem valores
pessoa.fromkeys(["Cor favorita"], "Branco") #cria chaves com valores

#.get() acessa valores no dicionário, que diferente acessando por slice, se a chave não existir o get não para o programa.

pessoa.get("Telefone")
pessoa.get("Religião", {}) #passa um valor default se a chave não existir

#.items() retorna uma lista de tuplas dos objetos do dicionário

pessoa.items()

#.keys() retorna só as chaves do dicionário

pessoa.keys()

#.pop()  remove uma chave do dicionário

pessoa.pop("Telefone", "Não encontrou") #É passado um valor por default caso não encontre a chave.

#popitem() remove a primeira chave

#setdefault() análisa se um valor passado está no dicionário, se não estiver ele adiciona, se estiver ele retorna o valor que já existe.

pessoa.setdefault("Nome", "Fernanda")

#.update() nos deixa atualizar um dicionário com outro dicionário

pessoa.update({"Outra pessoa": {"Nome": "Lacazette", "Idade": 38}})

#.values( ) nos retorna apenas os valores do dicionário

pessoa.values()

#in verifica s euma chave existe no dicionário

"Idade" in pessoa #nos retorna true, pois a chave existe no dicionário

#del deleta uma chave ou valor passado

del pessoa ["Outra pessoa"]["Idade"]