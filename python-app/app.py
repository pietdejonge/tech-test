from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime
import schedule
import sys

app = Flask(__name__)

@app.route('/')
def display_hello_world():
    return 'Hello World!'

def job(path='/tmp'):
    with open(str(path)+"/hello-world.txt", "ab") as myfile:
        myfile.write(str(datetime.datetime.now()) + " -- hello world! \n")
        myfile.close()

if (len(sys.argv)) > 1:
    path = sys.argv[1]
else:
    path = '/tmp'

schedule.every(10).seconds.do(job, path)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
# schedule.run_continuously()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')