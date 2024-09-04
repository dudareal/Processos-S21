from bomba_combustivel import BombaCombustivel

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

def main():
    print("Escolha o tipo de bomba:")
    print("1 - Etanol")
    print("2 - Gasolina")
    tipo = int(input("Digite o número correspondente ao tipo de bomba: "))

    if tipo not in [1, 2]:
        print("Opção inválida!")
        return

    valor_litro = float(input("Digite o valor do litro: "))

    if tipo == 1:
       BombaEtanol = BombaEtanol(valor_litro)
    else:
        BombaGasolina = BombaGasolina(valor_litro)