"""
TaskTracker - Fase 2 (Entrega Intermediária) - Bootcamp II
Aplicação CLI para cadastro e visualização de tarefas.

Autora: Heloisa Rodrigues
"""


def cadastrar_tarefa(tarefas):
    """Coleta os dados e adiciona a nova tarefa à lista."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    titulo = input("Digite o título da tarefa: ").strip()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
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
        print("-" * 40)
    print()


def main():
    tarefas = []

    while True:
        print("=== TASKTRACKER - MENU PRINCIPAL ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

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


if __name__ == "__main__":
    main()