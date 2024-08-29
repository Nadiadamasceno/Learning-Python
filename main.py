print ("Bem-Vindo a Calculadora de IMC com Orientação Nutricional!")  # Aqui vai exibir a mensagem de boas-vindas.

nome = input("Qual seu nome?")  # Aqui vai perguntar o nome do usuário e armazená-lo na variável 'nome'.

def calcular_imc(peso, altura):  # 'def' inicia a definição da função, 'calcular_imc' é o nome da função, e 'peso, altura' são os parâmetros da função.
    return peso / (altura ** 2)  # Retorna o valor do IMC calculado (por exemplo: 60 / 1.64 = 36,58 / 1.64 = imc 22.30).

peso = float(input('Informe seu peso em kg: '))  # Como o peso pode ter casas decimais, usamos 'float'. Aqui perguntamos o peso do usuário.
altura = float(input('Informe sua altura em metros: '))  # Como a altura pode ter casas decimais, usamos 'float'. Aqui perguntamos a altura do usuário.

imc = calcular_imc(peso, altura)  # Aqui criamos uma variável para armazenar o valor calculado do IMC.
print(f'Seu IMC é: {imc:.2f}')  # Exibimos o valor do IMC com duas casas decimais.

if imc < 16:  # Verifica se o IMC é menor que 16.
    print("Magreza grave")
elif 16.1 <= imc < 16.9:  # Verifica se o IMC está entre 16.1 e 16.9.
    print("Magreza moderada")
elif 17 <= imc < 18.5:  # Verifica se o IMC está entre 17 e 18.5.
    print("Magreza leve")
elif 18.6 <= imc < 24.9:  # Verifica se o IMC está entre 18.6 e 24.9.
    print("Peso ideal")
elif 25 <= imc < 29.9:  # Verifica se o IMC está entre 25 e 29.9.
    print("Sobrepeso")
elif 30 <= imc < 34.9:  # Verifica se o IMC está entre 30 e 34.9.
    print("Obesidade grau I")
elif 35 <= imc < 39.9:  # Verifica se o IMC está entre 35 e 39.9.
    print("Obesidade grau II ou severa")
else:  # Se o IMC for maior ou igual a 40.
    print("Obesidade grau III ou mórbida")

orientacao = input("Deseja orientação nutricional?")
#Falta continuar....