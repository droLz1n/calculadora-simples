# Calculadora no terminal
from rich import print
#from rich.panel import Panel
#from rich.align import Align
from rich.traceback import install
install()


print(
    f"Está é uma [bold green]CALCULADORA SIMPLES[/] utilize apenas números [bold yellow]INTEIROS[/].")

while True:
    print(
        f"Digite a operação que deseja realizar, usando os símbolos: [bold cyan]+[/], [bold cyan]-[/], [bold cyan]*[/], [bold cyan]/[/], [bold cyan]%[/].\nCaso deseje encerrar a calculadora digite [bold red]999[/].\n")

    operacao = input("Selecione a operação: ")

    if operacao == "999":
        print(f"Encerrando a [bold red]calculadora...[/]")
        break
    elif operacao == "+":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        soma = numero1 + numero2
        print(
            f"A soma entre {numero1} + {numero2} é igual a [bold blue]{soma}[/].")
    elif operacao == "-":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        subtracao = numero1 - numero2
        print(
            f"A subtração entre {numero1} - {numero2} é igual a [bold blue]{subtracao}.[/]")
    elif operacao == "*":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        multiplicacao = numero1 * numero2
        print(
            f"A multiplicação entre {numero1} e {numero2} é igual a [bold blue]{multiplicacao}[/].")
    elif operacao == "/":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        if numero2 == 0:
            print(f"[bold red]ERRO!!![/] Não é possível dividir um número por 0.")
        else:
            divisao = numero1 / numero2
            print(
                f"A divisão entre {numero1} e {numero2} é igual a [bold blue]{divisao:.0f}[/].")
    elif operacao == "%":
        numero1 = int(input(f"Digite o valor: "))
        valor_porcentagem = int(
            input(f"Digite a porcentagem desejada (apenas o número, sem o símbolo): "))
        porcentagem = numero1 * (valor_porcentagem / 100)
        print(
            f"{valor_porcentagem} de {numero1} é igual a [bold blue]{porcentagem:.2f}[/].")
    else:
        print(f"Opção inválida. Tente novamente!!!")

    continuar = input("Deseja efetuar outra operação? (s/n): \n").lower()

    if continuar != "s":
        print("[bold yellow]Encerrando a calculadora...[/]")
        break
