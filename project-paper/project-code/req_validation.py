import sqlite3
from sqlite3 import Error
from datetime import datetime
import json

def exec_select(conn, select_sql):
    """ Selecting Record """
    c = conn.cursor()
    c.execute(select_sql)
    rows = c.fetchall()
    for row in rows:
        print(row)


def main():
   conn = sqlite3.connect('sshkeymgmt.db')

   select_sql = """SELECT src_host_name,src_user_id,tgt_host_name,tgt_user_id FROM user_req_access WHERE req_status = 'Initial Request';"""

   exec_select(conn,select_sql)
   conn.commit()
   conn.close()

if __name__ == '__main__':
   main()
