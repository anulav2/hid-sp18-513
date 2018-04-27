#!/usr/bin/env python
import os
import sys
import subprocess

SSH_DIR = "/home/%s/.ssh" % (USER)

def check_key():
    """Check if RSA is present already"""


    if "id_rsa" in os.listdir(SSH_DIR):
       return True
    else:
       return False


def generate_key():

    os.chdir(SSH_DIR)
    if check_key():
       Print ("SSH Key is already Present")
    else:
       subprocess.call('ssh-keygen', shell=True)
'''
def copy_key_asroot(host,key):
    copycmd = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                        -n root@%s 'echo %s >> ~/.ssh/authorized_keys'" % (host,key)
    os.system(copycmd)

def copy_key(host,user,port):
    os.chdir(SSH_DIR)
    if check_key():
       if ssh-copy-id" in os.listdir("/usr/local/bin")
          command = "ssh-copy-id -p %s %s@%s" % (port, user, host)
          subprocess.call(command, shell=True)
'''

def main():
    generate_key()

if __name__ == "__main__":
   main()
