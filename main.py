"""
MENU PRINCIPAL:

===== LOJA =====

1 - Listar produtos
2 - Cadastrar produto
3 - Alterar produto
4 - Remover produto
5 - Realizar venda
6 - Repor estoque
7 - Relatório
8 - Sair

Escolha uma opção:

"""

import os

produtos = {
    1: {
        'nome': 'Teclado',
        'preco': 120.00,
        'estoque': 10
    },
    2: {
        'nome': 'Mouse',
        'preco': 80.00,
        'estoque': 15
    },
    3: {
        'nome': 'Headset',
        'preco': 200.00,
        'estoque': 5
    }
}

def show_main_menu():
    os.system("cls")
    print("===== LOJA =====")
    print()
    print(f"\033[35m{1}\033[0m", "- Listar produtos")
    print(f"\033[35m{2}\033[0m", "- Cadastrar produto")
    print(f"\033[35m{3}\033[0m", "- Alterar produto")
    print(f"\033[35m{4}\033[0m", "- Remover produto")
    print(f"\033[35m{5}\033[0m", "- Realizar venda")
    print(f"\033[35m{6}\033[0m", "- Repor estoque")
    print(f"\033[35m{7}\033[0m", "- Relatório")
    print(f"\033[35m{8}\033[0m", "- Sair")
    print()
    input("Escolha uma opção:")

while True:
    show_main_menu()











