#Primeiro método

nome = "Lucas"
idade = 26
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Lucas", "idade": 26}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}."
      .format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade.".format(**dados))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")