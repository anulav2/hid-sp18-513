import sqlite3
from sqlite3 import Error
from datetime import datetime
import json

def exec_select(conn, select_sql):
    """ Selecting Record """
    c = conn.cursor()
    c.execute(select_sql)
    results = c.fetchall()
    return results

def validate_user(conn, tgt_host,tgt_user_id):
    """ Validting User """
    c = conn.cursor()
    c.execute("""SELECT count(*) FROM Usergrp WHERE server = ? AND user_id = ?;""",(tgt_host, tgt_user_id))
    cnt = c.fetchall()
    return cnt

def upd_status(conn, cnt, src_host, src_user, tgt_host, tgt_user_id):
    """ Update Status """
    c = conn.cursor()
    if cnt == 0:
          c.execute("""UPDATE user_req_access set req_status = 'Declined', req_reject_reason = 'User doesnot have access to Targer Server' WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id =?;""",(src_host,src_user,tgt_host, tgt_user_id))
    else:
          c.execute("""UPDATE user_req_access set req_status = 'Request Approved' WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id =?;""",(src_host,src_user,tgt_host, tgt_user_id))

def main():
   conn = sqlite3.connect('sshkeymgmt.db')

   select_sql = """SELECT src_host_name,src_user_id,tgt_host_name,tgt_user_id FROM user_req_access WHERE req_status = 'Initial Request';"""

   sel_rec = exec_select(conn,select_sql)
   for i in sel_rec:
       src_host = i[0]
       src_user = i[1]
       tgt_host = i[2]
       tgt_user = i[3]
       cnt = validate_user(conn,tgt_host,tgt_user)
       upd_status(conn,cnt[0][0],src_host,src_user,tgt_host,tgt_user)
   conn.commit()
   conn.close()

if __name__ == '__main__':
   main()

