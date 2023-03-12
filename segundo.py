from sys import exit

from main_valores import soma, diminuir, multiplicacao, divisao,mensagem

while True:
    print("Escolha um dos valores:")
    valor = input("1 (+) 2 (-) 3 (*) 4(/) 5 (Sair)")
    try:
        if valor == '1':
            valor1 = int(input("Escolha um valor: "))
            valor2 = int(input("Escolha outro valor: "))
            resultado_soma = soma(valor1, valor2)
            print("Resultado da soma: ", resultado_soma)
    
        elif valor == '2':
            valor3 = int(input("Escolha um valor: "))
            valor4 = int(input("Escolha outro valor: "))
            resultado_menos = diminuir(valor3, valor4)
            print("Resultado da subtração: ", resultado_menos)
        
        elif valor == "3":
            valor5 = int(input("escolha um valor: "))
            valor6 = int(input("escolha um valor: "))
            resultado_multiplicacao = multiplicacao(valor5, valor6)
            print("Resultado da multiplicação: ", resultado_multiplicacao)
        
   
        elif valor == "4":
            valor7 = int(input("escolha um valor: "))
            valor8 = int(input("escolha um valor: "))
            resultado_divisao =int(divisao(valor7, valor8))
            print("Resultado da divisao: ", resultado_divisao)
            
        elif valor == "5":
            exit(mensagem)    
        else:
            print("Opção inválida. Tente novamente.")
    except ZeroDivisionError:
            print("NAO TEM COMO DIVIDIR POR ZERO")
    except ValueError:
            print("Digite apenas numeros")
    except Exception:
        print("Ocorreu erro inesperado")
    
        
   