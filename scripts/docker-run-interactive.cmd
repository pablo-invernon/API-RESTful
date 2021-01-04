@echo "INVOCACION INTERACTIVA"

@call scripts\docker-scripts-common.cmd

@echo on
docker container run -p 3000:3000 -ti --rm --env-file scripts\py.env -v %CD%:/usr/src/todo-list-serverless %IMAGE% /bin/sh

