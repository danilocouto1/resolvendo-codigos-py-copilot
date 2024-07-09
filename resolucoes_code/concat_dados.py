# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
def main():
    # Solicita o primeiro dado do usuário
    primeiro_dado = input("Digite o primeiro dado: ")
    
    # Solicita o segundo dado do usuário
    segundo_dado = input("Digite o segundo dado: ")
    
    # Concatena os dois dados
    dados_concatenados = primeiro_dado + segundo_dado
    
    # Exibe a string concatenada
    print("String concatenada:", dados_concatenados)

if __name__ == "__main__":
    main()
