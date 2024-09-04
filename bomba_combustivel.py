class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.valor_litro = valor_litro
        self.quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            print("Erro. O valor deve ser positivo.")
            return -1
        litros = valor / self.valor_litro
        if litros > self.quantidade_disponivel:
            print("Erro. Não há combustível suficiente.")
            return -1
        self.quantidade_disponivel -= litros
        return litros
    
    def abastecer_por_litros(self, litros):
        if litros <= 0:
            print("Erro. A quantidade de litros deve ser positiva.")
            return -1
        if litros > self.quantidade_disponivel:
            print("Erro. Não há combustível suficiente.")
            return -1
        valor = litros * self.valor_litro
        self.quantidade_disponivel -= litros
        return valor
    
    def get_valor_litro(self):
        return self.valor_litro
    
    def set_valor_litro(self, valor_litro):
        if valor_litro <= 0:
            print("Erro. O valor do litro deve ser positivo.")
            return
        self.valor_litro = valor_litro

    def get_quantidade_disponivel(self):
        return self.quantidade_disponivel
    
    def set_quantidade_disponivel(self, quantidade):
        if quantidade <= 0:
            print("Erro. A quantidade deve ser positiva.")
            return
        self.quantidade_disponivel = quantidade

class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro):
        super().__init__(valor_litro, 1000)

class BombaGasolina(BombaCombustivel):
    ADITIVO_PERCENTUAL = 0.05

    def __init__(self, valor_litro):
        super().__init__(valor_litro, 1000)
    
    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            print("Erro. O valor deve ser positivo.")
            return -1
        valor_com_aditivo = self.valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        litros = valor / valor_com_aditivo
        if litros > self.quantidade_disponivel:
            print("Erro. Não há combustível suficiente.")
            return -1
        self.quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0:
            print("Erro. A quantidade de litros deve ser positiva.")
            return -1
        valor_com_aditivo = self.valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        if litros > self.quantidade_disponivel:
            print("Erro. Não há combustível suficiente.")
            return -1
        valor = litros * valor_com_aditivo
        self.quantidade_disponivel -= litros
        return valor