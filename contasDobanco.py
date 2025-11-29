class ContasP:
    def __init__(self, numero, valorINI=0):
        self.numero = numero
        self.saldo = valorINI
        
        
    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    def debitar(self, valor_INI):
        if valor_INI > 0 and valor_INI <= self.saldo:
            self.saldo -= valor_INI
            return True
        else:
            print("Valor inválido para débito ou saldo insuficiente")
            return False
    
    def creditar(self, valor_INI):
        if valor_INI > 0:
            self.saldo += valor_INI
            return True
        else:
            print("Valor inválido para crédito")
            return False