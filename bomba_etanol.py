from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
