# database-connections

## Docker MS SQL Server

docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Passw0rd>" \
   -p 1433:1433 --name sql1 \
   -d mcr.microsoft.com/mssql/server:2017-latest

Connect using: 
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong!Passw0rd>"

## Docker Postgres SQL Server

docker run --name psql -e POSTGRES_PASSWORD=docker \
  -d -p 5432:5432 \
  -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
  
Connect using:
psql -h localhost -U postgres -d postgres
