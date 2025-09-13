# PUC-PR Atividade Formativa ADS
# Aluno Heber Leite da Rocha


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"


def main():
    while True:
        print("\n--- Calculadora ---")
        print("Selecione a operação:")
        print("1.Somar")
        print("2.Subtrair")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Sair")

        choice = input("Digite sua escolha (1/5): ")

        if choice == '5':
            print("Obrigado por usar a calculadora!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Escolha inválida!")

            again = input("Deseja continuar? (s/n): ")
            if again.lower() != 's':
                print("FIM")
                break


if __name__ == '__main__':
    main()
