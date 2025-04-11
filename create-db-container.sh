docker stop test_pg
docker rm test_pg
docker create --name test_pg -p5432:5432 -e POSTGRES_DB=cec_test -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=02357110 -t postgres:latest