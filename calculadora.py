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
        return "Erro!!"

#Criação do menu
print("PUC PR - Calculadora ADS - Com menu")
print("Selecione a operação:")
print("1.Somar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")
