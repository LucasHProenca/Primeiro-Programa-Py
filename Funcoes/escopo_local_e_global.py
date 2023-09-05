# Não é uma boa prática!.
salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    salario += bonus
    return salario, lista_aux

lista = [1]

salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)