# Resumo
O escopo do projeto abrange as operações básicas (CRUD) sobre o banco de dados sobre armas e munições. A interface web é desevolvida em Python Django e o banco de dados é gerenciado por PostgreSQL.

# Executando o projeto
## Preparando o ambiente
A única instalação necessária a nível de Sistema Operacional é a linguagem **Python**. É, também, recomendado que o pacote **virtualenv** seja também instalado pelo terminal do Python:

    pip install virtualenv
    cd test-deticpc
    virtualenv ./pyenv/

Com o ambiente virtual ativado, as dependências podem ser instaladas:

    source pyenv/bin/activate
    pip install -r requirements.txt
    deactivate

Por fim, o arquivo **.env** contendo os dados privados de autenticação deve ser colocado na pasta **test-deticpc/src**.

## Ativando os componentes
O banco de dados, o ambiente virtual e o site são colocados no ar com os seguintes comandos:

    sudo systemctl start postgresql
    source pyenv/bin/activate
    python src/manage.py runserver