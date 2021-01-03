FROM python:3.8.2-alpine

WORKDIR /usr/src

ADD requirements.txt ./

RUN apk add --update npm
RUN npm install -g serverless@1.83.2
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /root/.aws
ADD credentials /root/.aws/

RUN serverless init sf_7lWWMPlt

WORKDIR /usr/src/todo-list-serverless


CMD [ "python", "./start-app.py" ]