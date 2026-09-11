# 🛒 Sistema de Gerenciamento de Estoque e Vendas

Projeto desenvolvido em **Python** com o objetivo de praticar lógica de programação, estruturas de dados, funções, tratamento de exceções e organização de código.

O sistema simula o gerenciamento básico de uma pequena loja, permitindo cadastrar produtos, controlar o estoque, realizar vendas e consultar relatórios.

> **Status:** 🚧 Em desenvolvimento

---

## 📋 Sobre o projeto

O programa funciona através de um menu no terminal e permite ao usuário administrar os produtos e as vendas da loja.

O projeto foi desenvolvido sem o uso de **Programação Orientada a Objetos (POO)**, utilizando funções e estruturas de dados para organizar o sistema.

A proposta é transformar um problema relativamente grande em várias partes menores, trabalhando a capacidade de criar funções específicas e fazer essas funções trabalharem em conjunto.

---

## ⚙️ Funcionalidades

### 📦 Gerenciamento de produtos

* Listar produtos cadastrados
* Cadastrar novos produtos
* Alterar informações de produtos
* Remover produtos
* Pesquisar produtos
* Gerar IDs automaticamente

### 🏪 Controle de estoque

* Consultar quantidade disponível
* Repor estoque
* Verificar produtos com estoque baixo
* Calcular o valor total do estoque

### 🛒 Sistema de vendas

* Criar uma nova venda
* Adicionar múltiplos produtos à mesma venda
* Definir quantidade de cada produto
* Verificar disponibilidade em estoque
* Exibir resumo da venda
* Confirmar ou cancelar vendas
* Atualizar o estoque após uma venda
* Registrar o histórico de vendas

### 📊 Relatórios

* Valor total do estoque
* Produto com maior estoque
* Produto com menor estoque
* Produto mais caro
* Produto mais barato
* Produtos abaixo do estoque mínimo
* Histórico de vendas
* Faturamento total

### 🛡️ Tratamento de erros

O sistema deve impedir que entradas inválidas interrompam a execução do programa.

Exemplos:

* Valores que não são números
* IDs inexistentes
* Quantidades negativas
* Preços inválidos
* Produtos inexistentes
* Entradas vazias

Também deve existir um tratamento genérico para situações inesperadas utilizando `Exception`.

---

## 🧠 Conceitos praticados

Este projeto tem como objetivo praticar:

* Variáveis
* Tipos de dados
* `if / elif / else`
* `for`
* `while`
* Listas
* Dicionários
* Tuplas
* Sets
* Funções
* Parâmetros e argumentos
* `return`
* `*args`
* `**kwargs`
* F-strings
* `try / except`
* Tratamento específico de exceções
* Manipulação de estruturas de dados
* Validação de entrada
* Modularização
* Organização de código

---

## 🚫 Restrições

Para aumentar o nível de dificuldade e incentivar a implementação da lógica manualmente, algumas funções prontas não devem ser utilizadas.

### Não utilizar:

```python
max()
min()
sum()
sorted()
```

Também não deve ser utilizada **POO** nesta versão do projeto.

Por exemplo:

```python
class Produto:
    ...
```

não faz parte da proposta atual.

---

## 🖥️ Menu principal

O sistema deverá possuir uma estrutura semelhante a:

```text
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
```

---

## 📊 Estrutura dos dados

Os produtos podem ser armazenados utilizando um dicionário:

```python
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
    }
}
```

As vendas podem ser armazenadas em uma lista:

```python
vendas = []
```

Cada venda deverá possuir informações suficientes para reconstruir seu histórico e calcular o faturamento.

---

## 🔎 Pesquisa de produtos

O sistema também deverá permitir pesquisar produtos.

A pesquisa por nome deve ser **case-insensitive**, permitindo encontrar o mesmo produto independentemente de como o usuário digitar:

```text
mouse
Mouse
MOUSE
MoUsE
```

Também deverá ser possível pesquisar por:

* ID
* Nome
* Faixa de preço

---

## 🚨 Tratamento de exceções

O programa deve tratar erros previsíveis de maneira específica.

Exemplo:

```python
try:
    ...
except ValueError:
    ...
```

Além disso, deverá existir um tratamento genérico para erros inesperados:

```python
except Exception:
    ...
```

O objetivo não é utilizar `Exception` para esconder todos os erros, mas sim funcionar como uma última camada de proteção.

---

## 📁 Organização

A estrutura inicial pode ser simples:

```text
sistema-estoque-vendas/
│
├── main.py
└── README.md
```

Conforme o projeto evoluir, o código poderá ser dividido em diferentes módulos.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entre na pasta

```bash
cd sistema-estoque-vendas
```

### 3. Execute o programa

```bash
python main.py
```

---

## 🎯 Objetivos do projeto

Este projeto foi criado para desenvolver principalmente:

1. **Raciocínio lógico**
2. **Decomposição de problemas**
3. **Criação e reutilização de funções**
4. **Manipulação de estruturas de dados**
5. **Validação de dados**
6. **Tratamento de exceções**
7. **Organização de código**
8. **Construção de sistemas maiores em Python**

A principal dificuldade do projeto não está em uma funcionalidade isolada, mas em fazer todas as partes funcionarem corretamente em conjunto.

---

## 🚀 Possíveis melhorias futuras

Depois que a versão inicial estiver funcionando, o projeto poderá evoluir com:

* [ ] Persistência dos dados em arquivos JSON
* [ ] Sistema de login
* [ ] Diferentes tipos de usuários
* [ ] Carrinho de compras
* [ ] Sistema de descontos
* [ ] Cupons de desconto
* [ ] Data e hora das vendas
* [ ] Relatórios mais detalhados
* [ ] Exportação de relatórios
* [ ] Interface gráfica
* [ ] Banco de dados
* [ ] Migração para POO
* [ ] API para acesso aos produtos
* [ ] Testes automatizados

---

## 📌 Observação

Este projeto faz parte dos estudos de **Python**, com foco na consolidação dos fundamentos antes da utilização de Programação Orientada a Objetos.

A implementação deve ser realizada de forma incremental, começando pelas funcionalidades básicas e aumentando a complexidade conforme o sistema evolui.
