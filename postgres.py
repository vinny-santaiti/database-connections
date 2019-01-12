"""Connect to postgres database"""
import psycopg2
import psycopg2.extras

dsn = """host='server' dbname='database' user='admin' password='1234' application_name='dbconnect'"""

db_conn = psycopg2.connect(dsn)
db_cur = db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql = """select column from table where column = %s"""
db_cur.execute(sql, (id,))
result = db_cur.fetchall()
for res in result:
	print(res)
db_conn.close()
