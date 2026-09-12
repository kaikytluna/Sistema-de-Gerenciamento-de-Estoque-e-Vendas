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
        'estoque': 0
    }
}

# region VARIÁVEIS BASE

tamanho_lista_products=len(products)
lista_produtos=[]

# endregion

def gerar_lista_produtos():
    lista_produtos=[]
    for produtos in products.values():
        for i, dic in enumerate(produtos.items()):
            if i==0:
                lista_produtos.append(dic[1])
    return lista_produtos

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
    if tamanho_lista_products==0:
        os.system("cls")
        input("A lista de produtos esta vazia...")
        return True

def verificar_existencia_item():
    ...



def register_new_product(item):
    ...

def list_products():

    if no_items():
        return
    
    os.system("cls")

    for product in products:

        #NÃO MOSTRAR ITEMS SEM ESTOQUE:

        # key_item=products[product]

        # if key_item['estoque']==0:
        #     continue

        #-------------------------------

        # print(products.keys())
        print("ID:", product)
        print("Nome:", products[product]['nome'])
        print("Preço:", products[product]['preco'])
        print("Estoque:", products[product]['estoque'])
        print("------------------------")

def register_product():

    os.system("cls")

    id=tamanho_lista_products+1

    # products.update(
    item={id:{
        'nome': input("Insira o mome do item: ").capitalize(),
        'preco': float(input("Insira o preço do item: ")),
        'estoque': int(input("Insira a quantidade do item em estoque: "))
        }}

    if not verificar_existencia_item():
        products.update(item)
    else:
        print("")

def change_product():
    ...
def remove_product():

    if no_items():
        return
    
    list_products()
    print()
    remove_id=(input("Insira o ID do item que deseja remover: "))

    if remove_id!='':
        remove_id_int=int(remove_id)
        products.pop(remove_id_int)


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












