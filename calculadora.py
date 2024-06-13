def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2;
    elif operacao == 2:
        return num1 - num2;
    elif operacao == 3:
        return num1 * num2;
    elif operacao == 4:
        return num1 / num2 if num2 !=0 else "Divisão por zero não permitida";
    else: 
        return 0
    
# Testando a função
print(calculadora(6, 2, 1))  # Soma: 8
print(calculadora(6, 2, 2))  # Subtração: 4
print(calculadora(6, 2, 3))  # Multiplicação: 12
print(calculadora(6, 2, 4))  # Divisão: 3.0
print(calculadora(6, 2, 7))  # Operação inválida: 0
print(calculadora(6, 0, 4))  # Divisão por zero: 'Divisão por zero não permitida'

