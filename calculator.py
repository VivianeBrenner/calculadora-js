import os
import time


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    limpar_tela()
    print("╔════════════════════════════════════╗")
    print("║         CALCULADORA SIMPLES        ║")
    print("╠════════════════════════════════════╣")
    print("║                                    ║")
    print("║  [1] Soma (+)                     ║")
    print("║  [2] Subtração (-)                ║")
    print("║  [3] Multiplicação (*)            ║")
    print("║  [4] Divisão (/)                  ║")
    print("║  [5] Sair                         ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")


def calculator():
    while True:
        mostrar_menu()

        try:
            # Entrada do usuário
            operacao = input("\nEscolha uma operação (1-5): ")

            if operacao == "5":
                print("\nObrigado por usar a calculadora!")
                break

            if operacao not in ["1", "2", "3", "4"]:
                print("\nOperação inválida! Escolha entre 1 e 5.")
                time.sleep(2)
                continue

            limpar_tela()
            print("╔════════════════════════════════════╗")
            print("║         DIGITE OS NÚMEROS          ║")
            print("╚════════════════════════════════════╝")

            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realizando as operações
            if operacao == "1":
                resultado = num1 + num2
                print(f"\n{num1} + {num2} = {resultado}")
            elif operacao == "2":
                resultado = num1 - num2
                print(f"\n{num1} - {num2} = {resultado}")
            elif operacao == "3":
                resultado = num1 * num2
                print(f"\n{num1} * {num2} = {resultado}")
            elif operacao == "4":
                if num2 == 0:
                    print("\nErro: Não é possível dividir por zero!")
                    time.sleep(2)
                    continue
                resultado = num1 / num2
                print(f"\n{num1} / {num2} = {resultado}")

            # Perguntando se deseja continuar
            continuar = input("\nDeseja fazer outro cálculo? (s/n): ")
            if continuar.lower() != 's':
                print("\nObrigado por usar a calculadora!")
                break

        except ValueError:
            print("\nErro: Por favor, digite apenas números!")
            time.sleep(2)
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")
            time.sleep(2)


if __name__ == "__main__":
    calculator()