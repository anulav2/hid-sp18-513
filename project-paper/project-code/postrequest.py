import sqlite3
from sqlite3 import Error
from datetime import datetime
import json

def exec_insert(conn, insert_sql,task_1):
    """ Inserting Record """
    try:
        c = conn.cursor()
        c.execute(insert_sql,task_1)
    except Error as e:
        print(e)



def main():
   conn = sqlite3.connect('sshkeymgmt.db')
   dt = datetime.now()
   json_input = '{"src_host":"Silver", "src_user":"Uma", "src_key":"/home/gani/", "tgt_host":"Plat", "tgt_user":"Uma"}'
   my_dict = json.loads(json_input)

   insert_sql = """INSERT INTO user_req_access(src_host_name, src_user_id, src_pub_key, tgt_host_name, tgt_user_id, req_created_by, req_status, req_reject_reason, last_update_by) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"""

   task_1 = (my_dict["src_host"], my_dict["src_user"], my_dict["src_key"], my_dict["tgt_host"], my_dict["tgt_user"], 'Uma', 'Initial Request', 'Null', 'Test')

   exec_insert(conn,insert_sql,task_1)
   conn.commit()
   conn.close()

if __name__ == '__main__':
   main()
