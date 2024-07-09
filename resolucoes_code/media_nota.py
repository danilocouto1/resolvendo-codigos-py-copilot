# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.
def main():
    # Solicita as três notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcula a média das três notas
    media = (nota1 + nota2 + nota3) / 3
    
    # Exibe a média
    print(f"A média das três notas é: {media:.2f}")

if __name__ == "__main__":
    main()
