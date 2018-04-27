from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error
from datetime import datetime
import json
import logging


app = Flask(__name__)
api = Api(app)

def insert_request(values):
    """ Inserting Record """
    try:
        logging.info('recieved valuels to insert')
        logging.debug(values)
        insert_sql = """INSERT INTO user_req_access(src_host_name, src_user_id, src_pub_key, 
        tgt_host_name, tgt_user_id, req_created_by, req_status, req_reject_reason, last_update_by) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        with sqlite3.connect('sshkeymgmt.db') as c:
            c.execute(insert_sql,values)
        logging.info('completed insert into db')
    except Error as e:
        print(e)

class request_access(Resource):
    """
    """
    def post(self):
        logging.info('recieved request')
        post = request.get_json()
        logging.debug(post)
        #dt = datetime.now()
        #json_input = '{"src_host":"Silver", "src_user":"Uma", "src_key":"/home/gani/", "tgt_host":"Plat", "tgt_user":"Uma"}'
        values = (post.get('src_host'), post.get('src_user'), post.get('src_key'), 
        post.get('tgt_host'), post.get('tgt_user'), 'Uma', 'INITIAL_REQUEST', 'NULL', 'Test')
        insert_request(values)

api.add_resource(request_access, '/request_access', methods=['POST'])

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('calling create tables...')
    logging.info('completed db setup...')
    logging.info('deploying API...')
    app.run(host='0.0.0.0', debug=True)
