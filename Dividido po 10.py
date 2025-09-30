
while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        print("Programa encerrado.")
        break 

    try:
        numero = int(entrada)  
        resultado = 10 / numero
    except ValueError:
        print("Erro: O valor digitado não é um número inteiro válido.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"Resultado da divisão: {resultado}")

        