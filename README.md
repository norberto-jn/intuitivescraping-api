# Descrição do Projeto

Neste projeto, foram realizadas as atividades 1 e 2. Na atividade 1, o objetivo era fazer o download dos Anexos I e II e, em seguida, compactá-los no formato zip. Já na atividade 2, o objetivo era pegar o Anexo I da primeira atividade, em formato PDF, e transformar as tabelas desse anexo para o formato CSV. Para realizar essas duas atividades, foi utilizado o Docker para rodar os containers no backend e no frontend, sendo que no backend foi utilizado o Flask e no frontend, o Vue.

## Visão Geral

Ao executar o comando docker compose up -d, são iniciados dois containers: um para o backend e outro para o frontend. No backend, são executados três comandos principais. O primeiro comando serve para baixar os anexos do site. Após isso, é executado o segundo comando para zipar os anexos. Por fim, o último comando é executado para extrair as tabelas do anexo I e transformá-las em CSV.

   ```bash
    command: > 
      sh -c "
      python /usr/src/workspace/intuitivescraping-api/download_attachments.py && 
      python /usr/src/workspace/intuitivescraping-api/create_zip_from_attachments.py && 
      python /usr/src/workspace/intuitivescraping-api/extract_and_save_tables_from_pdf.py && 
      python ./src/main.py
      "
   ```

Obs: Para rodar o projeto, será necessário ter o Docker e o Docker Compose instalados.


## Passo a Passo para Rodar o Projeto em Sua Máquina

1. **Criação do diretório para o projeto:**
   Crie uma pasta onde o back-end e o front-end serão colocados:
   ```bash
   mkdir project
   ```

2. **Acessar o diretório criado:**
   Entre na pasta `project`:
   ```bash
   cd project
   ```

3. **Clonar os repositórios do projeto:**
   Agora, clone os dois repositórios (back-end e front-end):
   ```bash
   git clone https://github.com/norberto-jn/intuitivescraping-api
   git clone https://github.com/norberto-jn/intuitivescraping-ui
   ```

4. **Copiar o arquivo `docker-compose.yaml`:**
   Copie o arquivo `docker-compose.yaml` de um dos repositórios (`intuitivescraping-api` e `intuitivescraping-ui`) e cole-os na raiz do diretório `project`.


5. **Instalar Docker Compose (caso necessário):**
   Se você não tem o Docker Compose instalado em sua máquina, siga o tutorial de instalação oficial [aqui](https://docs.docker.com/compose/install/).


6. **Rodar o Docker Compose:**
   Agora, dentro da pasta `project`, execute o comando:
   ```bash
   docker compose up -d
   ```

7. **Verificar se o projeto está rodando:**
   Após o Docker Compose subir os containers, você pode verificar o status do projeto com:
   ```bash
   docker compose ps
   ```

8. **Acessar a aplicação no navegador:**
   Abra um navegador de sua preferência e acesse a URL:
   ```
   http://localhost:5173
   ```