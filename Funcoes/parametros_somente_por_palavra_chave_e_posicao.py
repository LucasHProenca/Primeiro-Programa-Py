def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio", 2007, "ABC-1234", marca="Fiat", motor ="1.6", combustivel="Flex")