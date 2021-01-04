FROM python:3.8.2-alpine

WORKDIR /usr/src

ADD requirements.txt ./

RUN apk add --update npm make
RUN npm install -g serverless@1.83.2
RUN npm install serverless-offline --save-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /root/.aws
ADD credentials /root/.aws/

WORKDIR /usr/src/todo-list-serverless


CMD [ "python", "./start-app.py" ]