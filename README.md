# Resumo
O escopo do projeto abrange as operações básicas (CRUD) sobre o banco de dados sobre armas e munições. A interface web é desevolvida em Python Django e o banco de dados é gerenciado por PostgreSQL.

# Executando o projeto
## Preparando o ambiente
A única instalação necessária a nível de Sistema Operacional é a linguagem **Python**. É, também, recomendado que o pacote **virtualenv** seja também instalado pelo terminal do Python:

    pip install virtualenv
    cd test-deticpc
    virtualenv ./pyvenv/

Com o ambiente virtual ativado, as dependências podem ser instaladas:

    source pyvenv/bin/activate
    pip install -r requirements.txt
    deactivate

Por fim, o arquivo **.env** contendo os dados privados de autenticação deve ser colocado na pasta **test-deticpc/src**.

## Ativando os componentes
O banco de dados, o ambiente virtual e o site vão ao ar com os seguintes comandos (na pasta **test-deticpc**):

    sudo systemctl start postgresql
    source pyvenv/bin/activate
    python manage.py runserver localhost:5000

# Explicando dependências relevantes
Requisitos básicos instalados com Django:

    asgiref==3.5.1
    Django==4.0.4
    sqlparse==0.4.2

Conectando Python ao PostgreSQL:

    psycopg2==2.9.3

Desacoplando informações de acesso ao banco de dados de **/src/settings.py** para ao arquivo **/.env** equivalente:

    python-decouple==3.6