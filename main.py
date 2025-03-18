import json
# -*- coding: utf-8 -*-
ARQUIVO = "cadastro.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("E-mail: ")

    pessoas = carregar_dados()
    pessoas.append({"nome": nome, "idade": idade, "email": email})
    salvar_dados(pessoas)
    print("Cadastro realizado com sucesso!\n")


def listar_pessoas():
    pessoas = carregar_dados()
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
    else:
        for i, pessoa in enumerate(pessoas, 1):
            print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, E-mail: {pessoa['email']}")
        print()


def buscar_pessoa():
    nome_busca = input("Digite o nome para buscar: ")
    pessoas = carregar_dados()
    encontrados = [p for p in pessoas if nome_busca.lower() in p['nome'].lower()]

    if encontrados:
        for pessoa in encontrados:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, E-mail: {pessoa['email']}")
    else:
        print("Nenhuma pessoa encontrada.")
    print()


def excluir_pessoa():
    nome_excluir = input("Digite o nome para excluir: ")
    pessoas = carregar_dados()
    pessoas_filtradas = [p for p in pessoas if p['nome'].lower() != nome_excluir.lower()]

    if len(pessoas) == len(pessoas_filtradas):
        print("Nenhuma pessoa encontrada com esse nome.")
    else:
        salvar_dados(pessoas_filtradas)
        print("Cadastro excluído com sucesso!")
    print()


def menu():
    while True:
        print("--- MENU ---")
        print(f'1. Cadastrar pessoa \n2. Listar pessoas \n3. Buscar pessoa \n4. Excluir pessoa \n5. Sair')

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            buscar_pessoa()
        elif opcao == "4":
            excluir_pessoa()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    menu()
