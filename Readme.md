# Dynamodb-serverless

Repositório destinado ao estudo da ferramenta serverless , com o provedor aws e com lambda de interação com API Gateway.
Todos os objetos válidos , passados via POST são salvos em um banco Dynamodb rodando num docker.

# Requirements:
    - node
    - serverless: npm install -g serverless
    - to run serverless local: npm install serverless-offline
    - to use python requirements: npm install serverless-python-requirements
        - create env: virtualenv -p python3 .venv
        - access: source .venv/bin/activate
        - install requirements: pip3 install -r requirements.txt
    - to use .env : npm i -D serverless-dotenv-plugin

## Comandos do serverless

### Obter informações
    sls info

### Criar serverless com python e aws
    serverless --template aws-python

### Executar localmente
    sls offline

### Realizar Deploy:
    sls deploy --stage qa
    
### local logs
    sls logs -f function --tail

## Configurar docker
    sudo chmod 777 ./docker/dynamodb
    
   Demais comandos presentes no arquivo Makefile.
