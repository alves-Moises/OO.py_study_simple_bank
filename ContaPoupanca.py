from validation import conta

class contaPoupanca(conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)
        self.limite = 400
    