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