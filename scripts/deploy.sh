export APP_VERSION=1.0.0
export DATABASE_URI=${DATABASE_URI}
export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}


docker stack rm HTTPrequest
docker-compose down

docker service create --name registry --publish 4999:5000 registry
docker-compose build
#docker-compose push 
#docker stack deploy --compose-file docker-compose.yml HTTPrequest
#docker service ls
