def calcular_moedas(valor):
    moedas = [100, 50, 25, 10, 5, 1]
    resultado = {}

    for moeda in moedas:
        qtd = valor // moeda  
        if qtd > 0:
            resultado[moeda] = qtd
            valor = valor % moeda  

    return resultado

valor = int(input("Digite o valor em centavos: "))
moedas_usadas = calcular_moedas(valor)

print(f"Para {valor} centavos, a menor quantidade de moedas é:")
for moeda, qtd in moedas_usadas.items():
    if moeda == 100:
        print(f"{qtd} moeda(s) de 1 real")
    else:
        print(f"{qtd} moeda(s) de {moeda} centavos")
        