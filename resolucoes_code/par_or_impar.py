# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
def main():
    # Solicita um número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

if __name__ == "__main__":
    main()
