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

## 📌 Observação

Este projeto faz parte dos estudos de **Python**, com foco na consolidação dos fundamentos antes da utilização de Programação Orientada a Objetos.

A implementação deve ser realizada de forma incremental, começando pelas funcionalidades básicas e aumentando a complexidade conforme o sistema evolui.
