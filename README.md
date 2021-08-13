# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo:

 - Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. 

 - O *cliente* tem uma *conta* (poupança ou corrente) e pode _sacar/depositar_ nessa conta. 

 - *Contas corrente* tem um limite extra. 

 - *Banco* tem _clientes_ e _contas_.

*Dicas:* 
 - Criar classe *Cliente* que herda da classe *Pessoa* (Herança) 
 - *Pessoa* tem _nome_ e _idade_ (com *getters*) 
 - *Cliente* tem _conta_ (Agregação da classe *ContaCorrente* ou *ContaPoupanca*)

------------------------------------------------------------------------------------

## A fazer:

 - Criar classes *ContaPoupanca* e *ContaCorrente* que herdam de *Conta* 

 - *ContaCorrente* deve ter um limite extra 

 - *Conta* têm _agência_, _número da conta_ e _saldo_ 

 - *Contas* devem ter método para _depósito_ 
 
 - *Conta* (super classe) deve ter o método _sacar_ abstrato (Abstração e polimorfismo - as subclasses que implementam o método sacar)

 - Criar classe *Banco* para AGREGAR classes de clientes e de contas (Agregação) 
 
 - *Banco* será responsável autenticar o cliente e as contas da seguinte maneira: Banco tem contas e clentes (Agregação) 
    * Checar se a agência é daquele banco 
    * Checar se o cliente é daquele banco 
    * Checar se a conta é daquele banco

 - Só será possível sacar se passar na autenticação do banco (descrita acima)