"""
TaskTracker - Fase 2 (Entrega Intermediária) - Bootcamp II
Aplicação CLI para cadastro e visualização de tarefas.

Autora: Heloisa Rodrigues
"""

from datetime import datetime

# ----------------------------- Constantes ----------------------------- #
STATUS_PADRAO = "Pendente"
LARGURA_LINHA = 40

# Chave = entrada normalizada (minúscula); valor = forma padronizada salva.
PRIORIDADES = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


# ------------------------ Funções de validação ------------------------ #
def obter_titulo_valido():
    """Pede o título até que seja informado um texto não vazio."""
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ser vazio ou conter apenas espaços. "
              "Tente novamente.\n")


def obter_prioridade_valida():
    """Pede a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES:
            return PRIORIDADES[entrada]
        print("Erro: prioridade inválida. Digite exclusivamente "
              "'Alta', 'Média' ou 'Baixa'.\n")


def obter_data_limite():
    """
    Pede a data limite (opcional). Se for informada, deve estar no
    formato DD/MM/AAAA e ser uma data real. Enter deixa em branco.
    """
    while True:
        data = input("Digite a data limite (DD/MM/AAAA) ou Enter para pular: ").strip()
        if not data:
            return ""
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA "
                  "(ex: 25/12/2026).\n")


# ------------------------- Funcionalidades ---------------------------- #
def cadastrar_tarefa(tarefas):
    """Coleta os dados, valida e adiciona a nova tarefa à lista."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    titulo = obter_titulo_valido()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = obter_prioridade_valida()
    data_limite = obter_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PADRAO,
    }
    tarefas.append(tarefa)
    print(f"\nSucesso: tarefa '{titulo}' cadastrada com sucesso!\n")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- LISTA DE TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.\n")
        return

    for i, t in enumerate(tarefas, start=1):
        print(f"Tarefa #{i}")
        print(f"  • Título:      {t['titulo']}")
        print(f"  • Descrição:   {t['descricao'] or 'Sem descrição'}")
        print(f"  • Prioridade:  {t['prioridade']}")
        print(f"  • Data Limite: {t['data_limite'] or 'Não informada'}")
        print(f"  • Status:      {t['status']}")
        print("-" * LARGURA_LINHA)
    print(f"Total: {len(tarefas)} tarefa(s).\n")


def exibir_menu():
    print("=== TASKTRACKER - MENU PRINCIPAL ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []

    try:
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção (1-3): ").strip()

            if opcao == "1":
                cadastrar_tarefa(tarefas)
            elif opcao == "2":
                listar_tarefas(tarefas)
            elif opcao == "3":
                print("\nEncerrando o TaskTracker. Até logo!")
                break
            else:
                print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.\n")
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C ou Ctrl+D: encerra sem mostrar erro técnico
        print("\n\nEncerrando o TaskTracker. Até logo!")


if __name__ == "__main__":
    main()