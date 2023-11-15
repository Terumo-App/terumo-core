

1. Frontend - Terumo Web
    - Fazer clone do repositorio
    - Checkout para branch `terumo_main`
    - usar `npm install` para instalar as bibliotecas
    - usar `npm run start` para rodar a aplicação

2. Backend - Terumo Core
    - Fazer clone do repositorio
    - Checkout para branch `main`
    - Neste projeto está sendo usado versão do python `--python 3.10.4`
    - instalar pipenv `pip install pipenv` no seu python global
    - usar `pipenv sync` ou `pipenv install` para um virtual env instalando todas bibliotecas listadas nos arquivos `Pipfile` e `Pipfile.lock`
    - usar `pipenv shell` para iniciar o ambiente virtual

    - É necessário criar um usuário admin no cytomine e alterar no arquivo `./src/.env.test` os seguintes atributos
        ```cmd
        PUBLIC_KEY={{public_key_do_usuario_admin}}
        PRIVATE_KEY={{private_key_do_usuario_admin}}
        HOST={{ host_do_cytomine}}
        ```
    - usar o comando `python src/main.py` para rodar a aplicação ou os scripts `run`
    - Para ver a documentação do OpenAPI acesse:
        ```cmd
        http://localhost:8000/docs#/
        ```
    - Na pasta  `./requests ` existem exemplos dos endpoints que já foram criados.

3. O que ja foi implementado até o momento

- [x] Login (front only)
- [x] Logout (front only)
- [x] SignIn (front/back)
- [x] Create Collection (front/back)
- [x] Create Collection (front/back)
- [x] List Collection (front/back)
- [x] List Images (front/back)

4. Próximas atividades

- [ ] Upload image(s) To Collection (front/back)
- [ ] Trigger Indexing (front/back)

- [ ] Image query (front/back)
