# Um conjunto não-ordenado de pares chave: valor
# As chaves são únicas (tem que ser imutável)
# Valor não precisa ser imutável

pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict(nome = "Guilherme", idade = 28)
pessoa["telefone"] = "3333-1234"

print(pessoa)

# Dados podem ser acessados pelo valor da chave

print(pessoa["nome"])

# Pode armazenar qualquer tipo de objeto Python, desde que a chave imutável (string e números)

contatos = {
    "guilherme@email.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "lucas@email.com": {"nome": "Lucas", "telefone": "3333-2231"},
}

print(contatos["lucas@email.com"]["telefone"])

for chave, valor in contatos.items(): #retorna uma tupla / lista de tuplas com chave e valor
    print(chave, valor)

# Métodos: .copy(), .fromkeys(), .get(), .items(), .keys(), .pop(), .popitem(), setdefault()
# .update(), .values(retorna todos os valores), .in(verifica se existe a chave), .del()

copia = contatos.copy()
copia["lucas@email.com"] = {"nome": "Luquinhas"}
print(contatos)
print(copia)
print(contatos.fromkeys(["endereço"], "vazio"))
print(contatos.get("lucas@email.com", {}))# Caso não encontrar a chave, o segundo paramêtro garante que voltará um objeto vazio
print(contatos.items())
print(contatos.keys())
contatos.pop("lucas@email.com", {})
print(contatos)

contato = {"nome": "Lucas", "telefone": "3229-4002"}
contato.setdefault("nome", "Giovana")
print(contato)
contato.setdefault("idade", 26)
print(contato)

contatos.update({"lucas@email.com": {"nome" : "Luquitcha"}})
contatos.update({"guilherme@email.com": {"nome" : "Gui"}})
print(contatos)

resultado = "telefone" in contatos
result = "lucas@email.com" in contatos
result_nome = "nome" in contatos["lucas@email.com"]
print(resultado)
print(result)
print(result_nome)
del contatos["guilherme@email.com"]
del contatos["lucas@email.com"]["nome"]
print(contatos)
