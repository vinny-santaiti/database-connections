"""Connect to postgres database"""
import pymssql
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
params = {'username': 'admin', 'password': '1234', 'host': 'server', 'port': '1433', 'database': 'dbname'}
sql_server_uri = 'mssql+pymssql://{username}:{password}@{host}:{port}/{database}'
dsn = sql_server_uri.format(**params)
# sqlalchemy engine should only be created once per app, not for each sql
engine = db.create_engine(dsn, convert_unicode=True)  
sql = """select column from table where column = %s"""
params = [4]
result = engine.execute(sql, params)
for res in result:
	print(res)
