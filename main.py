from bomba_gasolina import BombaGasolina
from bomba_etanol import BombaEtanol

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
        bomba = BombaEtanol(valor_litro)
    else:
        bomba = BombaGasolina(valor_litro)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Abastecer por valor")
        print("2 - Abastecer por litro")
        if tipo == 2:
            print("3 - Abastecer por valor com aditivo")
            print("4 - Abastecer por litro com aditivo")
        print("0 - Sair")
        opcao = int(input("Digite o número correspondente à opção: "))

        if opcao == 0:
            break

        if opcao == 1:
            valor = float(input("Digite o valor para abastecimento: "))
            resultado = bomba.abastecer_por_valor(valor)
            if resultado == -1:
                print("Não há combustível suficiente para realizar o abastecimento.")
            else:
                print(f"Abastecido {resultado:.2f} litros.")

        elif opcao == 2:
            litros = float(input("Digite a quantidade de litros para abastecimento: "))
            resultado = bomba.abastecer_por_litros(litros)
            if resultado == -1:
                print("Não há combustível suficiente para realizar o abastecimento.")
            else:
                print(f"Valor a ser pago: R${resultado:.2f}.")

        elif tipo == 2 and opcao == 3:
            valor = float(input("Digite o valor para abastecimento com aditivo: "))
            resultado = bomba.abastecer_por_valor_com_aditivo(valor)
            if resultado == -1:
                print("Não há combustível suficiente para realizar o abastecimento.")
            else:
                print(f"Abastecido {resultado:.2f} litros com aditivo.")

        elif tipo == 2 and opcao == 4:
            litros = float(input("Digite a quantidade de litros para abastecimento com aditivo: "))
            resultado = bomba.abastecer_por_litro_com_aditivo(litros)
            if resultado == -1:
                print("Não há combustível suficiente para realizar o abastecimento.")
            else:
                print(f"Valor a ser pago com aditivo: R${resultado:.2f}.")

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()