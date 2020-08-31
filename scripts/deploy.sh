export APP_VERSION=1.0.0
export DATABASE_URI=${DATABASE_URI}
export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
export TEST_DB_URI=${TEST_DB_URI}

docker service create --name registry --publish 4999:5000 registry
docker-compose up -d --build && docker-compose down
docker-compose push 
docker stack deploy --compose-file docker-compose.yml HTTPrequest