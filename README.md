# Gerenciador de Tarefas (CLI)

Este projeto é uma aplicação de linha de comando desenvolvida em Python para gerenciar tarefas de forma simples e objetiva. Ele permite adicionar novas tarefas, visualizar a lista de tarefas cadastradas e remover tarefas existentes por meio de um menu interativo no terminal. O objetivo é praticar conceitos básicos da linguagem Python utilizando um projeto funcional e organizado.

---

## 🚀 Tecnologias utilizadas

- Python 3  
- Python Standard Library (`os`)  
- Manipulação de arquivos (`.txt`)  
- Console / CLI  
- Programação estruturada  

---

## 📦 Sobre o projeto

Este projeto consiste em um **gerenciador de tarefas em linha de comando (CLI)**, criado com foco em aprendizado e prática de lógica de programação em Python.

- **Persistência de dados em arquivo `.txt`**  
  As tarefas são armazenadas em um arquivo de texto, garantindo que os dados não sejam perdidos ao encerrar o programa.  
  - Caso o arquivo não exista, ele é criado automaticamente.
  - Caso exista, as tarefas são carregadas ao iniciar o programa.

- **Adicionar tarefas**  
  Permite ao usuário inserir novas tarefas, que são armazenadas em memória e salvas no arquivo `.txt`.

- **Visualizar tarefas cadastradas**  
  Exibe todas as tarefas existentes de forma numerada, facilitando a identificação e organização.

- **Remover tarefas**  
  Permite selecionar uma tarefa específica para remoção, com confirmação antes de excluir o item.  
  Após a remoção, o arquivo `.txt` é atualizado automaticamente.

- **Menu principal interativo**  
  Toda a navegação é feita via terminal, utilizando um menu numérico simples e retorno automático ao menu após cada ação.

- **Limpeza do terminal**  
  Utiliza o módulo `os` para limpar a tela e melhorar a organização visual da aplicação durante a execução.

---

## 📁 Funcionamento do sistema de arquivos

- As tarefas são salvas em um arquivo `tarefas.txt`
- Cada tarefa ocupa uma linha do arquivo
- O programa:
  1. Verifica se o arquivo existe
  2. Cria o arquivo caso não exista
  3. Carrega as tarefas do arquivo para uma lista em memória
  4. Atualiza o arquivo sempre que uma tarefa é adicionada ou removida

Esse modelo simula um sistema simples de persistência de dados, servindo como base para futuras evolões do projeto.

---

## 📌 Objetivo geral do projeto

O principal objetivo deste projeto é **consolidar fundamentos essenciais da linguagem Python**, incluindo:

- Estruturas condicionais  
- Funções  
- Manipulação de listas  
- Entrada e saída de dados no terminal  
- Leitura e escrita de arquivos (`.txt`)  
- Organização e reutilização de código  
