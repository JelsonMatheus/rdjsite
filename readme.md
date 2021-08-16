# Fórum RespondeJunto

Fórum de perguntas e resposta, voltado para as disciplinas ministradas no curso de computação.

## :clipboard: Descrição

O RespondeJunto é um projeto criado com o intuito de colocar em praticar algumas habilidades de desenvolvimento web com o framework Django, além de criar um espaço para discussões e compartilhamento de informações através de perguntas e resposta, focado nas disciplinas do curso de computação.

## :hammer: Tecnologias utilizadas

* Python;
* Django;
* HTML, CSS e Bootstrap 5;

## :arrow_forward: Começando

### Pré-requisitos

* Python3
* PIP3
* Virtualenv

### Instalando

1. Clonando o projeto para a sua máquina:

    ```bash
    git clone https://github.com/JelsonMatheus/rdjsite.git
    ```

2. Renomear o arquivo que contem as variáveis de ambiente `.env.example` para `.env`.

### Executando o projeto

1. Criar uma **virtualenv** na raiz do projeto:

    ```bash
    python3 -m venv venv
    ```

2. Ativar o ambiente virtual:\
   **Linux**: `source venv/bin/active`.\
   **Windows**: `venv\scripts\activate`.

3. Intalar dependências:

    ```bash
    pip3 install -r .requirements.txt
    ```

4. Realizar o migrate:

    ```bash
    python3 manage.py migrate
    ```

5. Criar um superuser com nome admin:

    ```bash
    python manage.py createsuperuser --username admin
    Email address: example@mail.com
    Password: ******
    Password(again): ******
    ```

6. Iniciar servidor Django:

    ```bash
    python3 manage.py runserver
    ```

7. O servidor será iniciado em localhost:8000:

    ```bash
    System check identified no issues (0 silenced).
    August 15, 2021 - 23:08:58
    Django version 3.2.5, using settings 'rdjsite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

8. Uma mensagem de erro deve aparecer. O proximo passo é acessar a pagina localhost:8000/admin/ e cadastrar um novo fórum.

## :pushpin: Licença

Este projeto está licenciado sob a licença *MIT License* - consulte o arquivo LICENSE.md para obter detalhes.
