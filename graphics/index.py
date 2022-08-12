import matplotlib.pyplot as plt
import numpy as np

a, b, c = 3, 2, 7 # Três últimos digitos do RU

class Calculo:
  def __new__(self, x):
    global a, b, c
    y = (a * x) + (x * b) - c
    return y

v1, v2, v3 = Calculo(5), Calculo(7), Calculo(9) #Calculo para 5, 7 e 9 e armazeno em v1, v2 e v3

values = [v1, v2, v3]

x = 15*np.array(range(len(values)))

plt.plot( x, values, 'bo') #Pontos azuis em cada valor
plt.plot( x, values, 'k:', color='black') #Linha pontilhada preta

plt.axis([-1, 31, 15, 40])
plt.title("Quantidade de acessos em 30 minutos")

plt.grid(True)
plt.xlabel("Eixo X :: tempo em minutos")
plt.ylabel("Eixo Y :: quantidade de acessos")
plt.show()