import cliente

clientes = [cliente(192)]

class pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    @property
    def getNome(self):
        return self.__nome

    @property 
    def getIdade(self):
        return self.__idade

class cliente(pessoa):
    def __init__(self, conta, nome, idade):
        super().__init__(nome, idade)
        self.conta &= conta

class banco(clientes, len(clientes)):
    print()


class conta():       
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    
    @property
    def depositar():
        ''

    @property
    def sacar():
        ''

class contaCorrente(conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)
        self.limite = 500
    

class contaPoupanca(conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)
        self.limite = 400
    







