import math

class Calculadora:
    def __init__(self, valor_atual = None):
        self.valor_tela = valor_atual

    '''Para as funções de soma e subtração escolhi utilizar *args' para que possa ser encaminhado
    qualquer quantidade de parâmetros a cada chamada das funções'''

    def soma(self, *args):
        total = 0
        for param in args:
            total += param
        self.valor_tela = total
        return total
    
    def subtracao(self, *args):
        total = args[0]
        args = list(args)
        args.remove(args[0])
        for param in args:
            total -= param
        self.valor_tela = total
        return total
    
    def divisao(self, value_1, value_2):
        total = value_1 / value_2
        self.valor_tela = total
        return total
    
    def multiplicacao(self, value_1, value_2):
        total = value_1 * value_2
        self.valor_tela = total
        return total
    
    def exponenciacao(self, value, expo):
        total = value ** expo
        self.valor_tela = total
        return total

    def modulo(self, value):
        total = abs(value)
        self.valor_tela = total
        return total

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
    executa_operacao(oper)

    print("+--------------------------------------------------------+")
    global going
    going = int(input("| Deseja repetir? Sim: 1 / Não: 0 \n"))


while going:
    inicia_programa()



