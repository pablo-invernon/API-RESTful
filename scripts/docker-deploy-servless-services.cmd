
call docker-scripts-common.cmd

docker container run  -v %cd%:/usr/src/todo-list-serverles %IMAGE% serverless deploy

