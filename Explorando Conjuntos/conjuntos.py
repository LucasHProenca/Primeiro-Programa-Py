#Elimina elementos duplicados de uma lista
#Não confiar na ordenação
#Não tem como acessar os valores de um set, precisa transformar ele numa lista primeiro
#For e enumerate funcionam no set

numeros = set([1, 2, 3, 4, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

lista_numeros = list(numeros)
print(lista_numeros[0])

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {2, 3, 4, 5}
conjunto_d = {6, 7}
#Métodos: .union, .intersection, .difference, .symmetric_difference, .issubset, 
# .issuperset, isdisjoint, .add, .clear, .copy, .discard (se o elemento não existe ele não da erro), 
# .pop (remove da esquerda pra direita), .remove (se o elemento não existe da erro), .len, .in

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.issubset(conjunto_c))
print(conjunto_c.issubset(conjunto_b))
print(conjunto_b.issuperset(conjunto_c))
print(conjunto_c.issuperset(conjunto_b))
print(conjunto_c.isdisjoint(conjunto_d))
conjunto_a.add(30)
print(conjunto_a)
conjunto_a.discard(30)
print(conjunto_a)
