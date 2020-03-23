"""
Move postgesql database from one host to another host.
This assumes db user and pw is stored in .pgpass
"""
import subprocess
import calendar
from datetime import datetime
import time

def run_command(bashCommand):
    print(bashCommand)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)

if __name__ == '__main__':
    ts = calendar.timegm(time.gmtime())

    dt()
    user = 'pgadmin'
    source_host = 'host1'
    dest_host = 'host2'
    database = 'db'
    print('{}.{} will be replaced'.format(host=dest_host, database=database)
    dump_file = "/backup/{database}_{ts}.dump".format(database=database, ts=ts)
    bashCommand = "sudo pg_dump -h {host} -U {user} -d {database} -Fc -f {dump_file}".format(host=source_host, user=user, database=database, dump_file=dump_file)
    run_command(bashCommand)

    bashCommand = "dropdb -h {host} -U {user} {database}".format(host=dest_host, user=user, database=database)
    run_command(bashCommand)

    bashCommand = "createdb -h {host} -U {user} {database}".format(host=dest_host, user=user, database=database)
    run_command(bashCommand)

    bashCommand = "pg_restore -h {host} -U {user} -d {database} -j 10 {dump_file}".format(host=dest_host, user=user, database=database, dump_file=dump_file)
    run_command(bashCommand)
    dt()
