# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
def main():
    # Solicita a string do usuário
    string = input("Digite uma string: ")
    
    # Solicita o número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Repete a string o número de vezes informado
    string_repetida = string * numero
    
    # Exibe a string repetida
    print("String repetida:", string_repetida)

if __name__ == "__main__":
    main()
