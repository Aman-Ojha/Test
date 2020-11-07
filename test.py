import time
from flask import Flask, request

app = Flask(__name__)

# We create global variables to keep track of the counter
speed = thetime = cents = 0


@app.route('/', methods=["GET"])
def post():
    global speed, thetime, cents

    # Check if previous counter is running
    counter_running = True if thetime else False

    thetime = int(request.args["time"])
    speed = float(request.args["speed"])
    cents = request.args["cents"]

    print('\n')
    print('AccuView Digital:')
    print('Speed:', speed, ' Time:', thetime, ' Cents:', cents)
    print('-------------------------------')

    def countdown():
        global thetime, speed
        while thetime:
            mins, secs = divmod(thetime, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print('Tijd:', timer, end="\r")
            time.sleep((speed + 1) / 1000)
            thetime -= 1
            if thetime == 0:
                print('Werp geld in\n')

    # If existing counter is running, then we don't start another counter
    if not counter_running:
        countdown()
    return '1'


app.run(host='192.168.1.107', port= 8099)