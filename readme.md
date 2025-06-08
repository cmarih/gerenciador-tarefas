# Gerenciador de Tarefas 📝

![version](https://img.shields.io/badge/version-1.0-blue))

Uma aplicação em Python que permite adicionar, listar, atualizar, completar e remover tarefas, com interface de menu no console.

## 📋 Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#requisitos)
- [Instalação e execução](#instalação-e-execução)
- [Exemplos de Uso](#exemplos-de-uso)
- [Fluxo típico](#fluxo-típico)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Agradecimentos](#agradecimentos-)

---

## Descrição

Este projeto implementa um gerenciador de tarefas simples via console. O usuário interage através de um menu para:

- Adicionar novas tarefas;

- Visualizar tarefas com indicação de status (não completa/completa);

- Editar o nome de tarefas existentes;

- Marcar tarefas como concluídas;

- Remover todas as tarefas já completadas.

Ideal para estudar lógica de manipulação de listas, dicionários, e entrada/saída de dados em Python.

---

## Funcionalidades

1. **Adicionar tarefa:** registra um dicionário com os campos "tarefa" e "completada".

2. **Listar tarefas:** mostra um índice, ícone de status (✅ ou ❌) e nome da tarefa.

3. **Atualizar tarefa:** permite editar o nome de uma tarefa existente, identificada por índice.

4. **Completar tarefa:** altera o status da tarefa para True, marcando-a como concluída.

5. **Deletar concluídas:** remove todas as tarefas com completada == True.

6. **Sair:** encerra o programa com mensagem de finalização.

---

## Requisitos

- Python 3.6+

- Nenhuma biblioteca externa necessária — o projeto usa apenas biblioteca padrão.

---

## Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/cmarih/gerenciador-tarefas.git
   ```
2. Acesse a pasta:

   ```bash
   cd gerenciador-tarefas
   ```
2. Execute o script:
   ```bash
    python main.py
   ```

# Exemplos de Uso
```txt
    Menu do gerenciador de Lista de tarefas:
    1. Adicionar tarefa
    2. Ver tarefa
    3. Atualizar tarefa
    4. Completar tarefa
    5. Deletar tarefas completadas
    6. Sair
```

## Fluxo típico:

1. Adiciona “Comprar leite”
    ```bash
    Informe o nome da tarefa a ser adicionada: Comprar leite
    Tarefa 'Comprar leite' foi adicionada.
    ```
2. Adiciona “Estudar Python”
    ```bash
    Informe o nome da tarefa a ser adicionada: Estudar Python
    Tarefa 'Estudar Python' foi adicionada.
    ```
3. Lista tarefas e vê:
    ```css
    1. [❌] Comprar leite
    2. [❌] Estudar Python
    ```
4. Marca tarefa 1 como concluída:
    ```css
    Lista de tarefas:
    1. [✅] Comprar leite
    2. [❌] Estudar Python
    ```
5. Atualiza tarefa 2 para “Estudar APIs”
    ```css
        Qual tarefa deseja atualizar? 2
        Digite o novo nome da tarefa: Estudar APIs
        Tarefa 'Estudar Python' atualizada para 'Estudar APIs'
    ```
    5.1 Lista tarefas e vê:
        
    ```css
        Lista de tarefas:
        1. [✅] Comprar leite
        2. [❌] Estudar APIs
     ```

6. Remove tarefas concluídas → lista agora mostra apenas:
    ```css
    1. [❌] Estudar APIs
    ```

# Estrutura do Projeto
```bash
   gerenciador-tarefas/
├── main.py          # Código principal com funções + menu interativo
├── README.md        # Este arquivo de documentação
```
- `main.py`: contém todas as funções conforme declaradas *(adicionar, ver, atualizar, completar, deletar).*

# Contribuição
- Contribuições são bem-vindas 🙌:

- Dê um fork neste repositório.

- Crie uma feature branch *(git checkout -b minha-feature).*

- Commit suas alterações *(git commit -m 'Adiciona feature X').*

- Push para sua branch *(git push origin minha-feature).*

- Abra um Pull Request detalhando as mudanças.


# Agradecimentos 🙏

Este projeto foi desenvolvido como parte do meu aprendizado no curso de **Python** da [Rocketseat](https://www.rocketseat.com.br/).  
Agradeço pelo conteúdo claro e prático! 🚀
