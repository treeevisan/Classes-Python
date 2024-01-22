
from datetime import datetime
import pytz
import time
from random import randint

class ContaCorrente():
    
    """
    Cria um objeto ContaCorrente para gerenciar conta de clientes.
    
    Atributos:
        Nome (str): Nome completo
        CPF (int): somente numero CPF
        Ag (int): Agencia
        Conta (int): num de conta
        Saldo (float): Dinheiro disponivel na conta
        Transacoes (str): Historico de transcoes do cliente
        Limite (float): Limite em cheque especial do cliente
    """

    @staticmethod
    def _data_hora():
        fuso = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso)
        return horario.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, saldo, ag, conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite = None
        self.ag = ag
        self.conta = conta
        self._senha = '1234'
        self.transacoes = []
        self.cartoes = []

        print('Parabéns! Sua conta foi criada.')


    def consultar_saldo(self):
        print('\nSeu saldo atual é de: R$ {:,.2f} \n'. format(self.saldo))
    
        print('--'*20)

    def depositar(self, qtd):
        self.saldo += qtd
        self.consultar_saldo()
        self.transacoes.append((qtd,self.saldo, ContaCorrente._data_hora()))

    def _lim_conta(self):
        self.limite = -1000
        return(self.limite)

    def sacar(self, qtd):

        if self.saldo - qtd < self._lim_conta():
            print("Saldo insuficiente!/n") 
            self.consultar_saldo()
            print('--'*20)
        else:
            self.saldo -= qtd
            print('\nVocê fez um saque!\n')
            self.transacoes.append((-qtd,self.saldo,ContaCorrente._data_hora()))
            self.consultar_saldo()
            
    def consultar_historico(self):
        print('Seu extrato:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, destino):
        if self.saldo - valor < self._lim_conta():
                print("Saldo insuficiente!/n") 
                self.consultar_saldo()
                print('--'*20)
        else:
            self.saldo -= valor
            print('\nVocê fez uma transferencia de R${} para {}!\nSeu saldo é de:\n'.format(valor, destino.nome))
            self.transacoes.append((-valor,self.saldo,ContaCorrente._data_hora()))
            self.consultar_saldo()
            destino.saldo +=valor
            destino.transacoes.append((valor,self.saldo,ContaCorrente._data_hora()))


    #Método Getter
    @property
    def senha(self):
        return self._senha
    
    #Método Setter
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Senha alterada!')
        else:
            print('Senha inválida!')



class CartaoCredito():


    @staticmethod

    def _data_hora_cartao():
        fuso = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso)
        return '{}/{}'.format(horario.month, horario.year+4)

    def __init__(self, titular, conta): # O atributo conta é a classe conta, não o numero
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = CartaoCredito._data_hora_cartao()
        self.cvv = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.conta = conta
        conta.cartoes.append(self)



if __name__ == '__main__':
    # --------------------------------- // --------------------------- // -------------------
            
    ## Interface
            
    conta_renan = ContaCorrente('Renan', 46817267825, 500, 1, 2032)
    conta_mae = ContaCorrente('Shirley', 48920194392,100,1,4685)

    conta_renan.consultar_saldo()
    conta_mae.consultar_saldo

    # --------------------------------- // --------------------------- // -------------------

    ## Deposito

    conta_renan.depositar(10)
    time.sleep(3)

    # --------------------------------- // --------------------------- // -------------------

    ## Saque

    conta_renan.sacar(300)
    time.sleep(3)



    ## Transferencia e Extrato

    conta_renan.transferir(75, conta_mae)

    conta_mae.consultar_saldo()

    conta_renan.consultar_historico()
    conta_mae.consultar_historico()

    conta_mae.consultar_saldo()

    conta_mae.saldo

    # --------------------------------- // --------------------------- // -------------------

    ## Consulta cartoes

    print(conta_renan.cartoes[0].numero)

    # --------------------------------- // --------------------------- // -------------------

    ## Cartao de Credito

    cartao_renan = CartaoCredito('Renan',conta_renan)

    print(cartao_renan.validade)
    print(cartao_renan.numero)
    print(cartao_renan.cvv)


    cartao_mae = CartaoCredito('Shirley',conta_mae)
    print(cartao_mae.validade)
    print(cartao_mae.numero)
    print(cartao_mae.cvv)

    # --------------------------------- // --------------------------- // -------------------

    ## Senha

    print(conta_renan.senha)

    conta_renan.senha = '123' # Senha inválida

    conta_renan.senha = "9725" # Senha válida, alterada

    print(conta_renan.senha)

    # --------------------------------- // --------------------------- // -------------------

    #Consultar todos os valores das instancias da classeprint

    print(conta_renan.__dict__)
    print(cartao_renan.__dict__)

