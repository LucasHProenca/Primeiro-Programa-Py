saldo = 1000
saque = 200
limite = 100

result = saldo >= saque and saque <= limite

print(result)

result1 = saldo > saque or saque <= limite

print(result1)

contatos_emergencia = []

print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500")

conta_especial = True

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))