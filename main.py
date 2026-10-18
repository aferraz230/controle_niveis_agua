
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e suas respectivas situações
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (CRÍTICO)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (ALERTA)", "cor": Fore.BLUE}
]


# Função responsável por definir a cor do alerta
def definir_cor(nivel):
    for item in niveis_agua:
        if item["nivel"] == nivel:
            return item["cor"], item["situacao"]

    return Fore.WHITE, "Nível inválido"


# Programa principal
print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===\n")

# Simulação dos cinco níveis do reservatório
for item in niveis_agua:
    cor, situacao = definir_cor(item["nivel"])

    mensagem = (
        f"Nível {item['nivel']}: {situacao}"
    )

    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
