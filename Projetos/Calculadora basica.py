def soma (a,b):
    return a+b
def subtracao (a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    if b!=0:
        return a/b
    else:
        return "Erro: Divisão por zero não é permitida."
def potencia(a,b):
    return a**b

def calculadora():
    operacoes= {'+':soma, '-':subtracao, '*':multiplicacao, '/':divisao, '**':potencia}
    print('Calculadora Simples')
    print('Operações disponiveis: + | - | * | / | **')

    while True:
        num1 = float(input('Digite o primeiro número: '))
        operador = input('Digite o operador ( + | - | * | / | **): ')
        num2 = float(input('Digite o segundo número: '))

        if operador in operacoes:
            resultado = operacoes[operador](num1,num2)
            print('Resultado: ',resultado)
        else:
            print('Operador inválido!')

        continuar = input('Deseja continuar?(S/N):')
        if continuar.upper()!='S':
            break
    print('Calculadora encerrada.')
calculadora()

