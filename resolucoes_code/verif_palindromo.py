# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
def main():
    # Solicita a palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    # Remove espaços em branco e converte para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Verifica se a palavra é um palíndromo
    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")

if __name__ == "__main__":
    main()
