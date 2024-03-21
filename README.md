# Gerenciador Financeiro Pessoal

Este é um projeto de um gerenciador financeiro pessoal desenvolvido utilizando Flask (Python) para o backend, SQLite para o banco de dados, e JavaScript para interatividade na interface do usuário.

## Descrição do Projeto

Este projeto visa oferecer uma solução simples e eficaz para o controle das suas finanças pessoais. Com ele, você pode adicionar, editar, pagar e excluir contas a pagar e a receber, além de visualizar gráficos que apresentam uma visão geral das suas finanças.

## Funcionalidades Principais

- **Adicionar Nova Conta**: Permite adicionar novas contas especificando o tipo (a pagar ou a receber), o valor, a data de vencimento e uma descrição.
- **Editar Conta**: Permite editar os detalhes de uma conta existente, como valor, data de vencimento e descrição.
- **Pagar Conta**: Marca uma conta como paga.
- **Excluir Conta**: Remove uma conta do sistema.
- **Visualização de Gráficos**: Apresenta gráficos que mostram o total de contas a pagar e a receber.

## Como Executar o Projeto

1. Certifique-se de ter Python instalado em seu sistema. Você pode fazer o download e instalar a versão mais recente do Python em [python.org](https://www.python.org/).
2. Clone ou faça o download deste repositório para o seu ambiente local.
3. Instale as dependências necessárias utilizando o gerenciador de pacotes `pip`:

    ```
    pip install -r requirements.txt
    ```

4. Execute o aplicativo Flask:

    ```
    python app.py
    ```

5. Acesse o aplicativo em seu navegador web através do endereço [http://localhost:5000](http://localhost:5000).

## Estrutura do Projeto

- **`app.py`**: Arquivo principal que contém a lógica do servidor Flask.
- **`models.py`**: Arquivo que define a estrutura do banco de dados e as classes de modelo usando SQLAlchemy.
- **`database.py`**: Arquivo que configura a conexão com o banco de dados SQLite.
- **`templates/`**: Pasta que contém os arquivos HTML para a interface do usuário.
- **`static/`**: Pasta que contém arquivos estáticos como CSS e JavaScript.

## Tecnologias Utilizadas

- **Flask**: Um microframework web escrito em Python.
- **SQLite**: Um sistema de gerenciamento de banco de dados SQL embutido.
- **SQLAlchemy**: Uma biblioteca SQL para Python que facilita a interação com o banco de dados.
- **JavaScript**: Utilizado para criar interatividade na interface do usuário.
- **Chart.js**: Uma biblioteca JavaScript para criar gráficos e visualizações de dados.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).