
@call scripts\docker-scripts-common.cmd

@echo on
docker container run -ti --rm --env-file scripts\py.env ^
    -v %CD%\docker\credentials:/root/.aws/credentials ^
    -v %CD%:/usr/src/todo-list-serverless %IMAGE% serverless deploy -s Develop


