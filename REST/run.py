from eve import Eve
import platform

app = Eve()


@app.route('/ubuntu/processor',methods=['GET'])

def processor():
    ProcessorName = platform.processor()
    return "Processor name: " + ProcessorName + "\n"


if __name__ == '__main__':
    app.run()
