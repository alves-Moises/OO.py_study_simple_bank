from validation import conta

class contaCorrente(conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)
        self.limite = 500
        
    def sacar(self, valor):
        pass
    