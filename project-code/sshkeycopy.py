import os
import sys
import subprocess
import socket
import getpass
from  flask import Flask, request
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error
from datetime import datetime
import json
import logging


app = Flask(__name__)
api = Api(app)


def copy_key(src_host, src_user, src_pub_key, tgt_host, tgt_user, procesed_by):

     with sqlite3.connect('sshkeymgmt.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT count(*) FROM user_req_access WHERE req_status = 'APPROVED' AND src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id = ?;''',(src_host, src_user, tgt_host, tgt_user))
        results = c.fetchall()
        if results != 1:
           print("Approved Record Found in Table user_req_access")
           sshcopykey(src_host, src_user, tgt_host, tgt_user, procesed_by, src_pub_key)
        else:
           print("Approved Record Not Found in Table user_req_access")

def sshcopykey(src_host, src_user, tgt_host, tgt_user, procesed_by, src_pub_key):
    hostname = socket.gethostname()
    currentuser = getpass.getuser()
    if hostname != src_host:
       print "You Need to Login to Correct Host: ", src_host
    else:
        if (currentuser != src_user and 'SUDO_USER' not in os.environ and os.geteuid() != 0):
           print "You Need to Login as root or as user: ", src_user
        else:
             if (os.path.isfile(src_pub_key)):
                   command = "ssh-copy-id -i %s %s@%s" % (src_pub_key, tgt_user, tgt_host)
                   print "command :",command
                   try:
                       subprocess.call(command, shell=True)
                   except subprocess.CalledProcessError as errData:
                       errMsg = errData.output
                       print(errMsg)
                       print ("SSH Key Copied")
                       req_status = "COMPLETED"
                       upd_db(src_host, src_user, tgt_host, tgt_user, procesed_by, req_status)
             else:
                   req_status = "FAILED"
                   logging.info('Source Public Key Not Found')
                   upd_db(src_host, src_user, tgt_host, tgt_user, procesed_by, req_status)
               
def upd_db(src_host, src_user, tgt_host, tgt_user, procesed_by, req_status):

        """Update Final Status """

        approved_query = '''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'COMPLETED', last_update_by = ? WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id = ?;'''

        failed_query = '''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'FAILED',req_reject_reason = 'Public Key Not Found in Source Server', last_update_by = ? WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id = ?;'''

        with sqlite3.connect('sshkeymgmt.db') as conn:
             c = conn.cursor()
             if req_status == 'FAILED':
                c.execute('''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'FAILED',req_reject_reason = 'Public Key Not Found in Source Server', last_update_by = ? WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id = ?;''',(procesed_by,src_host, src_user, tgt_host, tgt_user))
                results = c.fetchall()
             else:
                c.execute('''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'COMPLETED',req_reject_reason = ' ', last_update_by = ? WHERE src_host_name = ? AND src_user_id = ? AND tgt_host_name = ? AND tgt_user_id = ?;''',(procesed_by,src_host, src_user, tgt_host, tgt_user))

             c.execute('''SELECT * FROM user_req_access;''')
             results = c.fetchall()
             print(results)


class copy_ssh_key(Resource):
    """
    """
    def post(self):
        logging.info('Creating SSH Key')
        post = request.get_json()
        logging.debug(post)
        copy_key(post.get('src_host'), post.get('src_user'), post.get('src_pub_key'), post.get('tgt_host'), post.get('tgt_user'), post.get('req_processed_by'))

api.add_resource(copy_ssh_key,'/copy_ssh_key',methods=['POST'])

if __name__ == "__main__":
   logging.getLogger().setLevel(logging.DEBUG)
   logging.info('Copy SSH Key')
   app.run(host='0.0.0.0',port=5005,debug=True)


