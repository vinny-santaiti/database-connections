"""Connect to postgres database"""
import psycopg2
import psycopg2.extras

dsn = """host='server' dbname='database' user='admin' password='1234' application_name='dbconnect'"""

db_conn = psycopg2.connect(dsn)
db_cur = db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql = """select column from table where column = %s"""
id = 4
db_cur.execute(sql, (id,))
result = db_cur.fetchall()
for res in result:
	print(res)
db_conn.close()

def test_mogrify():
	db_conn = psycopg2.connect(dsn)
	db_cur = db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
	ids = [1, 2, 3, 4]
	id_str = ','.join(str(i) for i in ids)
	sql = """select column from table where column in (%(id_str)s);"""
	data = {'id_str': id_str}
	query = dm_cur.mogrify(sql, data).decode("utf-8")
	db_cur.execute(query)
	result = db_cur.fetchall()
	for res in result:
		print(res)
	db_conn.close()
