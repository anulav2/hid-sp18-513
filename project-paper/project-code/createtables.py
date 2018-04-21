import sqlite3
from sqlite3 import Error


def create_connection(database):
    """ Create a Database Connection to a SQLite Database """
    try:
       conn = sqlite3.connect(database)
       return conn
    except Error as e:
       print(e)
    return none

def create_table(conn, create_table_sql):
    """ Create a Table """
    try:
       c = conn.cursor()
       c.execute(create_table_sql)
    except Error as e:
       print(e)

def main():
   database = "sshkeymgmt.db"
   sql_create_usergrp = """ CREATE TABLE IF NOT EXISTS usergrp (
                            server    varchar(100),
                            groups    varchar(100),
                            user_id   varhar(100)
                         );"""

   sql_create_useraccess = """ CREATE TABLE IF NOT EXISTS user_access (
                            server    varchar(100),
                            groups    varchar(100),
                            accesslvl  varhar(100)
                         );"""
   sql_create_req_access = """ CREATE TABLE IF NOT EXISTS user_req_access (
                            src_host_name       varchar(100),
                            src_user_id         varchar(100),
                            src_pub_key         varchar(1000),
                            tgt_host_name       varchar(100),
                            tgt_user_id         varchar(100),
                            req_created_dt      datetime default current_timestamp ,
                            req_created_by      varchar(100),
                            req_status          varchar(100),
                            req_reject_reason   varchar(100),
                            last_update_dt      datetime default current_timestamp,
                            last_update_by      varchar(100),
                            primary key(src_host_name,src_user_id,tgt_host_name,tgt_user_id)
                         );"""

   conn = create_connection(database)
   if conn is not None:
      create_table(conn, sql_create_usergrp)
      create_table(conn, sql_create_useraccess)
      create_table(conn, sql_create_req_access)
   else:
      print("Error!! Cannot Create the Database Connection")
   conn.close()

if __name__ == '__main__':
   main()
