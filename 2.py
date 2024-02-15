try:
    numero = int(input('Digite um'))
    divisao = 10/numero
except ZeroDivisionError:
    print('divisão por zero detectada')
except ValueError:
    print('o valor digitado não é um numero')
finally:
    print('obrigado por usar nosso software')