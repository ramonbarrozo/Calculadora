#Entrada de comandos
print("***Calculadora Simples***")
print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

num1 = float(input("Digite o Nº1:"));
num2 = float(input("Digite o Nº2:"));

opcao = input("Escolha a operação:");

if opcao == "1":
    print(f"Resultado: {num1+num2}");
elif opcao == "2":
    print(f"Resultado: {num1-num2}");
elif opcao == "3":
    print(f"Resultado: {num1*num2}");
elif opcao == "4":
    print(f"Resultado: {num1/num2}");
else:
    print("Opção inválida.");
