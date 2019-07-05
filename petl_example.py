"""Test python etl library https://petl.readthedocs.io/en/stable/io.html"""

import psycopg2
from petl import todb, look

create_table_script = """
CREATE TABLE public.petl_test (
	petl_id serial NOT NULL,
	description varchar NULL,
	external_id int4 NULL
); """

# source list of data including headers
source = [['description', 'external_id'], ['teach', 2], ['learn', 3]]
look(source)  # debugging
dest_db_table = 'petl_test'  # this db table must already exist

with psycopg2.connect("host=localhost dbname=mydb user=guest password=12345") as connection:
	with connection.cursor() as db_cur:
		# truncate the table and insert the data
		todb(table=source, dbo=db_cur, tablename=dest_db_table, schema='public')
