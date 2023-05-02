import os
import time

i = 0
os.system('cls')
print(' ' * 91 + 'Iniciando o programa...\n')
time.sleep(2)
text_env = ['LOADING','LOADING.','LOADING..','LOADING...']

while (i < 5):
    os.system('cls')
    time.sleep(0.5)
    j=0
    while (j < 4): 
        print(' ' * 91 + text_env[j]+'\n')
        time.sleep(0.5)
        os.system('cls')
        j = j + 1
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)
    i = i + 1


print('=' * 91 + 'CALCULADORA BÁSICA' + '=' * 73)
opção = int(input('\nVocê deseja ultilizar a calculadora? (1 ou 2)\nOpção 01: Sim \nOpção 02: Não \nOpção: '))
os.system('cls')
time.sleep(2)

while (opção != 2):
        print('\nQual operação você deseja execultar?')
        função = int(input('Opção 01: Soma \nOpção 02: Subtração \nOpção 03: Multiplicação \nOpção 04: Divisão \nOpção: '))
        match função: 
            case 1:
                #SOMA
                os.system('cls')

                n1 = float(input('Digite um valor: '))
                n2 = float(input('Digite outro valor: '))

                print(f'{n1} + {n2} = {n1+n2}')

                opção = int(input('\nVocê deseja continuar na calculadora? \nOpção 01: Sim \nOpção 02: Não \nOpção: '))

                os.system('cls')
                time.sleep(2)

            case 2:
                #SUBTRAÇÃO
                os.system('cls')

                n1 = float(input('Digite um valor: '))
                n2 = float(input('Digite outro valor: '))

                print(f'{n1} - {n2} = {n1-n2}')
            
                opção = int(input('\nVocê deseja continuar na calculadora? \nOpção 01: Sim \nOpção 02: Não \nOpção: '))

                os.system('cls')
                time.sleep(2)

            case 3:
                #MULTIPLICAÇÃO
                os.system('cls')

                n1 = float(input('Digite um valor: '))
                n2 = float(input('Digite outro valor: '))

                print(f'{n1} X {n2} = {n1*n2}')

                opção = int(input('\nVocê deseja continuar na calculadora? \nOpção 01: Sim \nOpção 02: Não \nOpção: '))   

                os.system('cls')
                time.sleep(2)

            case 4: 
                #Divisão
                os.system('cls')
                
                n1 = float(input('Digite um valor: '))
                n2 = float(input('Digite outro valor: '))

                if (n2 == 0):
                    i = 0
                    while (i < 1000):
                        print(' Error... ' * 100000)
                        time.sleep(0.01)
                        os.system('cls')
                        i = i + 1

                    break

                else:
                      print(f'{n1} / {n2} = {n1/n2 :.3f}')


                opção = int(input('\nVocê deseja continuar na calculadora? \nOpção 01: Sim \nOpção 02: Não \nOpção: '))

                os.system('cls')
                time.sleep(2)

print('\n' + ' '* 91 + 'Finalizando programa...\n')
time.sleep(2)
i = 0
while (i < 5):
    os.system('cls')
    time.sleep(0.5)
    j=0
    while (j < 4): 
        print(' ' * 91 + text_env[j]+'\n')
        time.sleep(0.5)
        os.system('cls')
        j = j + 1
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)
    i = i + 1


print('\n' + '*' * 91 + 'Calculadora desligada...' + '*' * 67)
time.sleep(5)
os.system('cls')
time.sleep(5)
