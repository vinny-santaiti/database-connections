# database-connections

## Docker MS SQL Server

docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Passw0rd>" \
   -p 1433:1433 --name sqlserver \
   -d mcr.microsoft.com/mssql/server:2017-latest

Connect using: 
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong!Passw0rd>"

## Docker Postgres SQL Server

docker run --name my_postgres \
-e POSTGRES_PASSWORD=mysecretpassword \
-p 5432:5432 \
-e PGDATA=/var/lib/postgresql/data/pgdata \
-v ~/docker/postgresql/data:/var/lib/postgresql/data \
-d postgres:9.6
  
Connect using:
psql -h localhost -U postgres -p 5432
CREATE ROLE myuser WITH LOGIN PASSWORD '123456' SUPERUSER;
\du    --> show users
\l     --> list db
\q
