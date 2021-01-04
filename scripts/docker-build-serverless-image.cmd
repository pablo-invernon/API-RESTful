@echo "CONSTRUYENDO IMAGEN"

@call scripts\docker-scripts-common.cmd
@echo on
docker build -t %IMAGE% .\docker