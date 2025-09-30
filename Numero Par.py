pares = [] 

print("Digite números inteiros. Digite 'fim' para encerrar.")

while True:
    entrada = input("Número: ")

    if entrada.lower() == "fim": 
        break

    try:
        n = int(entrada)

        if n % 2 != 0:
            print("Erro: o número digitado é ímpar.")
        else:
            pares.append(n)
            print("Número par adicionado!")

    except ValueError:
        print("Erro: digite apenas números inteiros ou 'fim' para encerrar.")

print("\nNúmeros pares digitados:", pares)