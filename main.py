class CuentaBancaria:
    todas_cuentas = []
    def __init__(self, tasa_interes, balance = 0):
      self.tasa_interes = tasa_interes
      self.balance = balance
      CuentaBancaria.todas_cuentas.append(self)

    def deposito(self, amount):
      self.balance += amount
      return self
        
    def retiro(self, amount):
      if (CuentaBancaria.puede_retirar(self.balance,amount)):
        self.balance -= amount
      else:
        print("Fondos insuficientes: cobrando una tarifa de $5")
        self.balance -= 5
      return self

    def mostrar_info_cuenta(self):
      print(f"Balance: ${self.balance}")
      return self
        
    def generar_interes(self):
      if (CuentaBancaria.puede_generar_interes(self.balance)):
        self.balance *= (1+self.tasa_interes)
      return self

    @classmethod
    def imprimir_todas_cuentas(cls):
      for cuenta in cls.todas_cuentas:
        cuenta.mostrar_info_cuenta()
    
    @staticmethod
    def puede_retirar(balance,amount):
      if(balance - amount >= 0):
        return True
      else:
        return False

    @staticmethod
    def puede_generar_interes(balance):
      if(balance > 0):
        return True
      else:
        return False

cuenta1 = CuentaBancaria(0.10)
cuenta2 = CuentaBancaria(0.11, 35000)

cuenta1.deposito(10000).deposito(15000).deposito(5000).retiro(15000).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(1000).deposito(1000).retiro(35000).retiro(3000).retiro(1995).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_cuentas()