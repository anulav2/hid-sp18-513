from __future__ import print_function
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

def check_key(SSH_DIR):
    """Check if RSA is present already"""
    if "id_rsa" in os.listdir(SSH_DIR):
       return True
    else:
       return False

def generate_key(src_host, src_user):

    hostname = socket.gethostname()
    currentuser = getpass.getuser()
    if hostname != src_host:
       print "You Need to Login to Correct Host: ", src_host
    else:
        if (currentuser != src_user and 'SUDO_USER' not in os.environ and os.geteuid() != 0):
           print "You Need to Login as root or as user: ", src_user
        else:
             SSH_DIR = "/home/{user}/.ssh".format(user=src_user)
             if not os.path.exists(SSH_DIR):
                os.mkdir(SSH_DIR)
                os.chdir(SSH_DIR)
             if check_key(SSH_DIR):
                print ("SSH Key is already Present")
             else:
                subprocess.call('ssh-keygen -f id_rsa -t rsa -N ""', shell=True)
                print ("SSH Key Created")
                
class create_ssh_key(Resource):
    """
    """
    def post(self):
        logging.info('Creating SSH Key')
        post = request.get_json()
        logging.debug(post)
        generate_key(post.get('src_host'), post.get('src_user'))

api.add_resource(create_ssh_key,'/create_ssh_key',methods=['POST'])

if __name__ == "__main__":
   logging.getLogger().setLevel(logging.DEBUG)
   logging.info('Create SSH Key')
   app.run(host='0.0.0.0', port=5001, debug=True)

