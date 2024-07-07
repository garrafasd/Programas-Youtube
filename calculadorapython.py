#Uma calculadora simples em python!

num1 = 0 #Declaração Numero 1
num2 = 0 #Declaração Numero 2
operaçao = 0 #Declaração operador

num1 = int(input("Qual seria o primeiro número? ")) #Atribuição do que o usuário digitar a num1
num2 = int(input("Qual seria o segundo número? "))  #Atribuição do que o usuário digitar a num2
operaçao = int(input("""
[1]Somar
[2]Subtrair
[3]Multiplicar
[4]Dividir
Qual é a sua escolha? >""")) #Atribiução do que o usuário digitar a operaçao

if operaçao == 1:
    #Somar
    print(f"O resultado de {num1} + {num2} é {num1 + num2}")
elif operaçao == 2:
    #Subtrair
    print(f"O resultado de {num1} - {num2} é {num1 - num2}")
elif operaçao == 3:
    #Multiplicar
    print(f"O resultado de {num1} * {num2} é {num1 * num2}")
elif operaçao == 4:
    #Dividir
    if num1 == 0 or num2 == 0:
        #Evitar divisão por 0
        print("Divisão por 0 não permitida!")
    else:
        print(f"O resultado de {num1} / {num2} é {num1 / num2}")

print("Tchau! Volte sempre!") #Despedida




