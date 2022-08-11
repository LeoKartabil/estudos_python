from Calculadora import *

''' Aqui ficam definidos os valores que serão utilizados para executar as operações matemáticas,
    sendo estes os dois últimos números do meu RU'''
ru = [2,7]
going = 1

''' Estou utilizando um objeto 'switcher' para chamar as funções da classe Calculadora.
    Por padrão passo os dois valores de ru.
    Para a execução do módulo é somado os valores de ru.'''
def executa_operacao(oper):
    calc = Calculadora()
    switcher = {
        1: calc.soma(ru[0], ru[1]),
        2: calc.subtracao(ru[0], ru[1]),
        3: calc.multiplicacao(ru[0], ru[1]),
        4: calc.exponenciacao(ru[0], ru[1]),
        5: calc.modulo(calc.soma(ru[0], ru[1]))
    }
    print(f'| Resultado igual a {switcher[oper]}')

def inicia_programa():
    print("+--------------------------------------------------------+")
    print("| Escolha a operacao a ser executada:")
    print("| 1: Soma")
    print("| 2: Subtracao")
    print("| 3: Multiplicacao")
    print("| 4: Exponenciacao")
    print("| 5: Modulo [soma dos dois valores em ru]")
    print("+--------------------------------------------------------+")
    print(f"| Valores {ru[0]} e {ru[1]} definidos para a execucao das operacoes!")
    print("+--------------------------------------------------------+")
    oper = int(input("| Operacao escolhida: "))
    print("+--------------------------------------------------------+")
    executa_operacao(oper)
    print("+--------------------------------------------------------+")
    
    global going
    going = int(input("| Deseja repetir? Sim: 1 / Não: 0 \n >>"))
    if going != 0 and going != 1:
        going = 0
        print("+--------------------------------------------------------+")
        print('Operação inválida, encerrando programa...')
        print("+--------------------------------------------------------+")

while going:
    inicia_programa()