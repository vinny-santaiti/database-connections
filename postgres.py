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
	"""table has 3 columns: serial pkey, col_1, col_2"""
	conn = psycopg2.connect(dsn)
	cur = conn.cursor()
	data = [(1,2), (3,4), (5,6)]
	values = ','.join(cur.mogrify("(DEFAULT,%s,%s)", x).decode("utf-8") for x in tuple(data))
	cur.execute("INSERT INTO table VALUES " + values) 
	conn.commit()
	conn.close()
