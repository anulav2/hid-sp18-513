from eve import Eve
import platform
import psutil
import json

app = Eve()


@app.route('/ubuntu/processor',methods=['GET'])

def processor():
    processordata = {
       "ProcessorName": platform.processor(),
       "System Name": platform.system(),
       "Version": platform.version(),
       "Node": platform.node(),
       "Release": platform.release()
    }
    return format(processordata)

def disk():
    diskdata = {
       "Disk Size": psutil.disk_usage('/').total,
       "Disk Free": psutil.disk_usage('/').available,
       "Disk Used": psutil.disk_usage('/').used
    }
    return format(diskdata)

def ram():
    ramdata = {
       "Total Ram": psutil.virtual_memory().total,
       "Ram Free": psutil.virtual_memory().available,
       "Ram Used": psutil.virtual_memory().used
    }
    return format(ramdata)

def format(data):
    output = json.dumps(data)+"\n"
    return output

if __name__ == '__main__':
    app.run()
