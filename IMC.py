

def classificar_imc(imc):
    if imc < 16:
        return "Baixo peso (Grau I)"
    elif 16 <= imc <= 16.99:
        return "Baixo peso (Grau II)"
    elif 17 <= imc <= 18.49:
        return "Baixo peso (Grau III)"
    elif 18.5 <= imc <= 24.99:
        return "Peso adequado"
    elif 25 <= imc <= 29.99:
        return "Sobrepeso"
    elif 30 <= imc <= 34.99:
        return "Obesidade (Grau I)"
    elif 35 <= imc <= 39.99:
        return "Obesidade (Grau II)"
    else:
        return "Obesidade (Grau III)"


pessoas = []


n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(n):
    print(f"\nCadastro {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    
    imc = peso / (altura ** 2)
    
    pessoas.append([nome, idade, imc])

print("\n--- Resultados ---")
for p in pessoas:
    nome, idade, imc = p
    categoria = classificar_imc(imc)
    print(f"{nome} - {idade} anos - {categoria}")
    