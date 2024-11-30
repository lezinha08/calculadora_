def calcular():
    print("Bem-vindo à calculadora!")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    # Escolher a operação
    operacao = input("Digite o número da operação desejada: ")
    
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida! Tente novamente.")
        return

    try:
        # Solicitar os números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realizar a operação
        if operacao == '1':
            resultado = num1 + num2
            simbolo = "+"
        elif operacao == '2':
            resultado = num1 - num2
            simbolo = "-"
        elif operacao == '3':
            resultado = num1 * num2
            simbolo = "*"
        elif operacao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                return
            resultado = num1 / num2
            simbolo = "/"
        
        # Exibir o resultado
        print(f"Resultado: {num1} {simbolo} {num2} = {resultado}")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
        
# Executar a calculadora
if __name__ == "_main_":
    calcular()