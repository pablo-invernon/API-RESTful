@echo "CONSTRUYENDO IMAGEN"

set IMAGE=api-restful:serverless-latest

docker container run  -v %cd%:/usr/src/todo-list-serverles %IMAGE% serverless deploy

