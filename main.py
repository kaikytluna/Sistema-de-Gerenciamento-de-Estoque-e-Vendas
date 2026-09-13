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

# region BASES

senha_gerente='1234'
tamanho_lista_produtos=len(products)

# endregion

def senha_gerencia():
    limpar_terminal()
    senha_inserida=input("Insira a Senha de gerente: ")

    if senha_inserida==senha_gerente:
        return True

    else:
        return False

def limpar_terminal():
    os.system("cls")

def show_main_menu():
    limpar_terminal()
    print("===== LOJA =====")
    print()
    print(f"\033[35m{1}\033[0m", "- Listar produtos")
    print(f"\033[35m{2}\033[0m", "- Realizar venda")
    print(f"\033[35m{3}\033[0m", "- Repor estoque")
    print(f"\033[35m{4}\033[0m", "- Relatório")
    print(f"\033[35m{"q"}\033[0m", "- Sair")
    print(f"\033[35m{"g"}\033[0m", "- Modo Gerência")
    print()
    cursor=input("Escolha uma opção: ")
    return cursor

def dev_main_menu():
    limpar_terminal()
    print("===== LOJA - ", f"\033[1;96m{"MODO GERÊNCIA"}\033[0m", "=====")
    print()
    print(f"\033[35m{1}\033[0m", "- Listar produtos")
    print(f"\033[35m{2}\033[0m", "- Cadastrar produto")
    print(f"\033[35m{3}\033[0m", "- Alterar produto")
    print(f"\033[35m{4}\033[0m", "- Remover produto")
    print(f"\033[35m{5}\033[0m", "- Realizar venda")
    print(f"\033[35m{6}\033[0m", "- Repor estoque")
    print(f"\033[35m{7}\033[0m", "- Relatório")
    print(f"\033[35m{"q"}\033[0m", "- Sair")
    print(f"\033[35m{"g"}\033[0m", "- Modo Estoque")
    print()
    cursor=input("Escolha uma opção: ")

    if cursor=="g":
        return show_main_menu

    return cursor
    # return cursor

def gerar_lista_produtos():
    lista_produtos=[]
    for produtos in products.values():
        for i, dic in enumerate(produtos.items()):
            if i==0:
                lista_produtos.append(dic[1])
    return lista_produtos

def no_items():
    if tamanho_lista_produtos==0:
        limpar_terminal()
        input("A lista de produtos esta vazia...")
        return True

def verificar_existencia_item(item):
    if item  in lista_produtos:
        return True
    else:
        return False

def list_products():

    if no_items():
        return
    
    limpar_terminal()

    for product in products:

        #NÃO MOSTRAR ITEMS SEM ESTOQUE:

        # key_item=products[product]

        # if key_item['estoque']==0:
        #     continue

        #-------------------------------

        print("ID:", product)
        print("Nome:", products[product]['nome'])
        print("Preço:", products[product]['preco'])
        print("Estoque:", products[product]['estoque'])
        print("------------------------")




def alterar_produto():
    limpar_terminal()

    item=input("Insira o nome do item: ").capitalize()

    if item=="Q":
        return

    exist=verificar_existencia_item(item)
    limpar_terminal()
    
    # item="Teclado"     #...
    # exist=True         #...

    if exist==True:
        for produto in products.values():
            if list(produto.values())[0]==item:
                id_item=0
                for id in products.items():
                    if id[1]==produto:
                        print("Id:", id[0])
                        id_item=id[0]
                        break
                    

                # preco=
                # estoque=

                
                print("Nome:", produto['nome'])
                print("Preço:" , produto['preco'])
                print("Estoque:" , produto['estoque'])
                print("------------------------")
                print()
                print(f"\033[35m{1}\033[0m", "- Renomear")
                print(f"\033[35m{2}\033[0m", "- Alterar Preço")
                print(f"\033[35m{3}\033[0m", "- Alterar Estoque")
                print(f"\033[35m{4}\033[0m", "- Alterar Tudo")
                print(f"\033[35m{5}\033[0m", "- Deletar")
                print()
                cursor=input("O que deseja fazer com o item? ")


                try:

                    if cursor=="1":
                        products.update({id_item:{'nome':input("Insira o novo nome do item: ").capitalize(), 
                                                'preco' : produto['preco'],
                                                'estoque' : produto['estoque']}})
                        print("")
                        input("Item renomeado com sucesso. ")
                        input(products)
                        return

                    if cursor=="2":
                        products.update({id_item:{'nome': produto['nome'], 
                                                'preco' : float(input("Insira o novo preço do item: ")),
                                                'estoque' : produto['estoque']}})
                        print("")
                        input("Preço alterado com sucesso. ")
                        return
                    
                    if cursor=="3":
                        products.update({id_item:{'nome': produto['nome'], 
                                                'preco' : produto['preco'],
                                                'estoque' : int(input("Insira a nova quantidade em estoque do item: "))}})
                        print("")
                        input("Quantidade alterada com sucesso. ")
                        return
                    
                    if cursor=="4":
                        products.update({id_item:{'nome':input("Insira o novo nome do item: ").capitalize(), 
                                                'preco' : float(input("Insira o novo preço do item: ")),
                                                'estoque' : int(input("Insira a nova quantidade em estoque do item: "))}})
                        print("")
                        input("Quantidade alterada com sucesso. ")
                        return
                    
                except ValueError:
                    print()
                    input("Digite apenas numerais.")
                    alterar_produto()



    if exist==False:
        input("Produto não cadastrado.")
        alterar_produto()
        return

def register_product():

    limpar_terminal()

    id_novo_item=tamanho_lista_produtos+1

    item_novo={}

    item_novo.update({id_novo_item:{'nome': input("Insira o nome do item: ").capitalize(),}})
    
    for id, dic in item_novo.items():
        item=dic['nome']

        if item=='Q':
            return

        if len(item)==0:
            limpar_terminal()
            input("Campo de nome vazio.")
            register_product()


        if not item.replace(" ","").isalpha():
            limpar_terminal()
            print(item) 
            input("Digite apenas letras.")
            register_product()


        exist=verificar_existencia_item(item=item)

        if not exist:
            item_novo[id_novo_item].update({
                'preco': float(input("Insira o preço do item: ")),
                'estoque': int(input("Insira a quantidade do item em estoque: "))
                })
            limpar_terminal()
            input("Produto cadastrado com sucesso!")
            return products.update(item_novo)

        else:
            print("Esse produto já esta cadastrado.")
            exit=input("... ")
            if exit=="q":
                return
            register_product()

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


# EXECUCÃO DO CÓDIGO


while True:
    # cursor=show_main_menu()
    lista_produtos=gerar_lista_produtos()

    cursor=dev_main_menu() # placeholder pra executar em modo gerencia

    # if cursor == "g":

            # if senha_gerencia():
            #     cursor=dev_main_menu()

            # else:
            #     limpar_terminal()
            #     input("Senha incorreta.")
            #     continue

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
        gerar_lista_produtos()

    if cursor == "3":
        alterar_produto()  
        gerar_lista_produtos()

    if cursor == "4":
        remove_product()
        gerar_lista_produtos()

    if cursor == "k":
        input(lista_produtos)



# print()

# while True:
#     remove_product()
#     break












