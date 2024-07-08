'''
Exercicio 46
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
import time
print()

i = int(float(10))
f = int(float(-1))
passo = int(float(-1))
for c in range(i,f,passo):
    print(f'Os valores até chegar a zero é {c}')
    sleep(1)
print('FIM')
