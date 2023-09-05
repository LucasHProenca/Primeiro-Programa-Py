frutas = ["laranja", "maçã", "uva"]

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

print(frutas[0])
print(frutas[-1])
print(frutas[-2])

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])#linha
print(matriz[0][0])#linha, #elemento
print(matriz[0][-1])#linha, #elemento
print(matriz[-1][-1])#linha, #elemento
print(matriz)

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])#start
print(lista[:2])#stop
print(lista[1:3])#start, stop
print(lista[0:3:2])#start, stop e step
print(lista[::])#start e stop = : portanto volta tudo
print(lista[::-1])#start e stop = : porem step = -1 portanto volta tudo só que ao contrário

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares = [numero for numero in numeros if numero % 2 == 0] #valor que retorna, iteração, condicional
print(pares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros] #valor que retorna, iteração
print(quadrado)

quadrado.clear()
print(quadrado)
print(pares.copy()) #spread operator, faz uma cópia com outro id da lista
print(pares.count(2))
pares.extend([6, 8]) # mescla uma lista na outra
print(pares)
print(pares.index(34)) # retorna o primeiro indice do argumento passado

pares_1 = [12, 14]
pares.extend(pares_1)
print(pares)
print(pares_1)

print(pares.pop()) #pilha de pratos, remove sempre o ultimo prato a menos que vc especifique qual vc quer
print(pares.pop())
print(pares.pop())
print(pares.pop(0))

pares.remove(6)
print(pares)
pares.reverse()
print(pares)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # volta em ordem alfabética
print(linguagens)

linguagens.sort(reverse=True) #volta em ordem contrária a alfabética
print(linguagens)

linguagens.sort(key = lambda x: len(x)) 
#lambda é uma função não nomeada (anônima), len = length, volta a lista ordenada da menor string pra maior
print(linguagens)

linguagens.sort(key = lambda x: len(x), reverse=True) 
#lambda é uma função não nomeada (anônima), len = length, volta a lista ordenada da maior string pra mmenor
print(linguagens)

print(len(linguagens)) # quantidade de elementos da lista
