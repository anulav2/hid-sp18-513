from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error
from datetime import datetime
import json
import logging

app = Flask(__name__)
api = Api(app)

def validate_action():
    """ Update Status """
    APPROVED_QUERY = '''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'APPROVED'
                        WHERE EXISTS (SELECT 1 FROM Usergrp WHERE user_req_access.tgt_user_id = usergrp.user_id
                        AND user_req_access.tgt_host_name = usergrp.server)
                        AND req_status = 'INITIAL_REQUEST';'''
    DECLINED_QUERY = '''UPDATE user_req_access set last_update_dt=current_timestamp, req_status = 'DECLINED',
                        req_reject_reason = 'User doesnot have access to Targer Server'
                        WHERE NOT EXISTS (SELECT 1 FROM Usergrp WHERE user_req_access.tgt_user_id = usergrp.user_id
                        AND user_req_access.tgt_host_name = usergrp.server)
                        AND req_status = 'INITIAL_REQUEST';'''
    REQUEST_COUNT_QUERY = '''SELECT COUNT(1) FROM user_req_access WHERE req_status = 'INITIAL_REQUEST';'''

    with sqlite3.connect('sshkeymgmt.db') as conn:
        c = conn.cursor()
        c.execute(REQUEST_COUNT_QUERY)
        results = c.fetchall()
        print('Number of requests to be processed: {0}', results)
        c.execute(APPROVED_QUERY)
        c.execute(DECLINED_QUERY)
        c.execute('''SELECT * FROM user_req_access;''')
        results = c.fetchall()
        print(results)
        
class validate_and_action(Resource):
    """
    """
    def post(self):
       logging.info('Validating Request')
       validate_action()

api.add_resource(validate_and_action,'/validate_and_action',methods=['POST'])

if __name__ == '__main__':
   logging.getLogger().setLevel(logging.DEBUG)
   logging.info('Validating Access Request')
   app.run(host='0.0.0.0', port=5004, debug=True)

        
