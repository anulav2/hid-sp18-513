from flask import Flask, request, json, render_template
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error
from datetime import datetime
import json
import logging
import createtables

app = Flask(__name__)
api = Api(app)

def select_status(req_status):
        select_sql = """SELECT src_host_name, src_user_id, tgt_host_name, tgt_user_id, req_created_by, req_status, last_update_by FROM user_req_access WHERE req_status = ?;"""

        reject_sql = """SELECT src_host_name, src_user_id, tgt_host_name, tgt_user_id, req_created_by, req_status, req_reject_reason, last_update_by FROM user_req_access WHERE req_status = ?;"""
        print(req_status)
        with sqlite3.connect('sshkeymgmt.db') as conn:
             c = conn.cursor()
             c.execute(reject_sql,(req_status.strip().strip('\n'),))
             results = c.fetchall()
            # return render_template('show_results.html', results = results)
             print(results)

class request_access(Resource):
    """
    """
    def post(self, request_status):
        logging.info('recieved request')
        select_status(request_status)

api.add_resource(request_access, '/getstatus/<string:request_status>', methods=['POST'])
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('Deploying API to Get Status of the Request...')
    app.run(host='0.0.0.0', debug=True)
