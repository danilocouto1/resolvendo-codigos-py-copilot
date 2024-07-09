# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
def main():
    # Solicita o primeiro número do usuário
    primeiro_numero = float(input("Digite o primeiro número: "))
    
    # Solicita o segundo número do usuário
    segundo_numero = float(input("Digite o segundo número: "))
    
    # Solicita a operação desejada
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    
    # Realiza a operação escolhida
    if operacao == '+':
        resultado = primeiro_numero + segundo_numero
    elif operacao == '-':
        resultado = primeiro_numero - segundo_numero
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero
    elif operacao == '/':
        # Verifica se o segundo número é diferente de zero para evitar divisão por zero
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    else:
        resultado = "Operação inválida."

    # Exibe o resultado da operação
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
