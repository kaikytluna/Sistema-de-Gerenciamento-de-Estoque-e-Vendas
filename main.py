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

products = {
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

tamanho_lista_products=len(products)
product_key=products.values()

# for id, dic in enumerate(products.values()):
#     print(id, dic)
#     input("Esperando...")


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
    print(f"\033[35m{"q"}\033[0m", "- Sair")
    print()
    cursor=input("Escolha uma opção: ")
    return cursor

def no_items():
    if len(products)==0:
        os.system("cls")
        input("A lista de produtos esta vazia...")
        return True


def list_products():

    if no_items():
        return
    
    os.system("cls")
    for product in products:
        # print(products.keys())
        print("ID:", product)
        print("Nome:", products[product]['nome'])
        print("Preço:", products[product]['preco'])
        print("Estoque:", products[product]['estoque'])
        print("------------------------")

def new_product(item):
    
    if item.values()['nome'] in product_key['nome']:
        sum(product_key['estoque'], item.values()['estoque'])

    products.update(item)

def register_product():

    if no_items():
        return
    
    os.system("cls")

    id=len(products)+1

    # products.update(
    products.update(item={id:{
        'nome': input("Insira o mome do item: ").capitalize(),
        'preco': float(input("Insira o preço do item: ")),
        'estoque': int(input("Insira a quantidade do item em estoque: "))
    }})


def change_product():
    ...
def remove_product():

    if no_items():
        return
    
    list_products()
    print()
    remove_id=(input("Insira o ID do item que deseja remover: "))

    if remove_id!='':
        int(remove_id)
        return
    
    if remove_id is int:
        products.pop(remove_id)

def make_a_sale():
    ...
def restock_product():
    ...
def report():
    ...


while True:
    cursor=show_main_menu()

    if cursor=="q":
        print()
        print("Fechando programa...")
        print()
        break

    if cursor == "1":
        list_products()   
        print()
        if len(products)!=0:
            input("Deseja retornar? ")     

    if cursor == "2":
        register_product()    

    if cursor == "3":
        change_product()  

    if cursor == "4":
        remove_product()        

# print()

# while True:
#     remove_product()
#     break












