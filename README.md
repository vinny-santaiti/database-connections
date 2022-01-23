# database-connections

## Docker Microsoft SQL Server

```
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Passw0rd>" \
   -p 1433:1433 --name ms-sqlserver-linux \
   -v ~/docker/mssql:/VAR/OPT/MSSQLHOST
   -d mcr.microsoft.com/mssql/server:2017-latest
```

Connect using: 
```
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong!Passw0rd>" \
   -b -e -i script.sql
```

## Docker PostgreSQL Server

```
docker run --name my_postgres \
-e POSTGRES_PASSWORD=mysecretpassword \
-p 5432:5432 \
-e PGDATA=/var/lib/postgresql/data/pgdata \
-v ~/docker/postgresql/data:/var/lib/postgresql/data \
-d postgres:9.6
```
  
Connect using:
```
psql -h localhost -U postgres -p 5432 database_name
CREATE ROLE myuser WITH LOGIN PASSWORD '123456' SUPERUSER;
\du    --> show users
\l     --> list db
\q
```
Mac os install PostgreSQL database adapter for Python, try one of 2 options:
```
pip install psycopg2-binary

export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
pip install psycopg2
```
