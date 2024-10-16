class ContaBancaria:
    def __init__(self, titular, saldo, agencia, conta_corrente):
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia
        self.conta_corrente = conta_corrente
    
    def deposito(self, valor, nome_transferencia):
        self.saldo = self.saldo + valor
        print(f"Você recebeu uma transferência de {nome_transferencia} no valor de R${valor},00\n"
              f"O novo saldo da sua conta é R${self.saldo},00")

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        print(f"Você sacou R${valor},00\n"
              f"Seu saldo agora é RS{self.saldo},00")

# Exemplo de uso
conta = ContaBancaria("Felipe", 350, "9876", "12345-67")
conta.titular
conta.deposito(129, "Jonathan Calleri") # Deposita transferencia na conta
conta.sacar(52) # Saca dinheiro da conta