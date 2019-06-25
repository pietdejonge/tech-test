from flask import Flask
import time
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    with open("/mnt/hello-world.txt","ab") as myfile:
        myfile.write(str(datetime.datetime.now()) + " -- hello world! \n")
        myfile.close()
        time.sleep(10)
