FROM python:3.8.2-alpine

WORKDIR /usr/src

ADD requirements.txt ./

RUN apk add --update gcc npm make python3-dev musl-dev libffi-dev openssl-dev
RUN npm install -g serverless@1.83.2
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN apk add --update 

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /root/.aws

WORKDIR /usr/src/todo-list-serverless


CMD [ "python", "./start-app.py" ]