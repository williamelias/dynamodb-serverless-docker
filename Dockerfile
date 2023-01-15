FROM python:3.9

WORKDIR /code

COPY dynamodb-serverless/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 


# Copy project
COPY dynamodb-serverless/ /code
COPY mock/ /code/mock

CMD ["python3", "handler.py"]
