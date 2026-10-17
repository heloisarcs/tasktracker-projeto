from datetime import datetime


def pedir_titulo():
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("O título não pode ficar vazio. Tente de novo.")


def pedir_prioridade():
    opcoes = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}
    while True:
        p = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if p in opcoes:
            return opcoes[p]
        print("Prioridade inválida. Use Alta, Média ou Baixa.")


def pedir_data():
    while True:
        data = input("Data limite (DD/MM/AAAA, Enter para pular): ").strip()
        if data == "":
            return ""
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Exemplo: 25/12/2026")


def cadastrar(tarefas):
    print("\n--- Nova tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data = pedir_data()

    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!\n")


def listar(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if len(tarefas) == 0:
        print("Não há tarefas cadastradas no momento.\n")
        return

    for i, t in enumerate(tarefas, 1):
        print(f"Tarefa {i}")
        print("Título:", t["titulo"])
        print("Descrição:", t["descricao"] or "Sem descrição")
        print("Prioridade:", t["prioridade"])
        print("Data limite:", t["data_limite"] or "Não informada")
        print("Status:", t["status"])
        print("-" * 30)
    print()


def main():
    tarefas = []

    while True:
        print("=== TaskTracker ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(tarefas)
        elif opcao == "2":
            listar(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    main()
