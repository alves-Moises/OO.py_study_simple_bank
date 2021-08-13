import cliente
from abc import abstractmethod

import functions

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
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
   
    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self, valor):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor = functions.verif_num()):
        self._saldo = valor
        


    
    def depositar(self,  valor = functions.verif_num()):
        
        self._saldo += valor   

    @abstractmethod
    def sacar(self, valor):
        pass









