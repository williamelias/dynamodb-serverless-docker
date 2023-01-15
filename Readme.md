# dynamodb-serverless

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

### info
    sls info

### To create a serveless environment with Python and aws
    serverless --template aws-python

### To run function local
    - sls invoke :
        > local -f function_name
        > -f function_name
    with params:
        -d "{'param':a}"

    run all local:
        sls offline
    run with local dynamodb:
        sls offline start
### To deploy 
    - sls deploy 
        or
    - sls deploy -f function_name
        or 
    - sls deploy --stage qa
    example: serverless deploy --stage prod --region us-east-1
### local logs
    sls logs -f function --tail

### Local test with vscode

Need replace class SqsMessage to:

    class SqsMessage:
        def __init__(
            self,
            messageId: str,
            body: str,
            messageAttributes: dict=None,
            *args,
            **kwargs
        ) -> None:

            self.id: str = messageId
            self.public_prices: typing.Iterable[dict] = body
            self.attr: dict = messageAttributes

## setup to run with docker

    docker-compose build
    sudo chmod 777 ./docker/dynamodb

    docker-compose up