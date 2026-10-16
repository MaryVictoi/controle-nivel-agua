
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e suas situações
niveis_agua = [
    (1, "Muito baixo (crítico)"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito alto (alerta)")
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível de água."""

    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


def exibir_alerta(nivel, situacao):
    """Exibe a situação do reservatório com a cor correspondente."""

    cor = definir_cor(nivel)
    mensagem = f"Nível {nivel}: {situacao}"

    print(cor + mensagem + Style.RESET_ALL)


# Simulação do monitoramento do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel, situacao in niveis_agua:
    exibir_alerta(nivel, situacao)
