import connexion
import six

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server.models.disk import DISK  # noqa: E501
from swagger_server.models.ram import RAM  # noqa: E501
from swagger_server import util
import os, platform, subprocess, re, psutil

def get_cpu_info():
    print "Hello"
    processordata = {
       "ProcessorName": platform.processor(),
       "System Name": platform.system(),
       "Version": platform.version(),
       "Node": platform.node(),
       "Release": platform.release()
    }
    return (processordata)

def get_disk_info():
    diskdata = {
       "Disk Size": psutil.disk_usage('/').total,
       "Disk Free": psutil.disk_usage('/').available,
       "Disk Used": psutil.disk_usage('/').used
    }
    return (diskdata)

def get_ram_info():
    ramdata = {
       "Total Ram": psutil.virtual_memory().total,
       "Ram Free": psutil.virtual_memory().available,
       "Ram Used": psutil.virtual_memory().used
    }
    return (ramdata)

def cpu_get():  # noqa: E501
    return get_cpu_info()


def disk_get():  # noqa: E501
    return get_disk_info()


def ram_get():  # noqa: E501
    return get_ram_info()

