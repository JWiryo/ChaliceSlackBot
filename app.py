from chalice import Chalice
from datetime import datetime

import json

app = Chalice(app_name='slackBotWines')
app.debug = True

@app.route('/wines')
def notify_wines():
    currentDate = datetime.now().strftime("%Y-%m-%d")
    message = "Today is %s; Please remember to input your WINES for this week" % currentDate
    return {'message' : json.dumps(message)}
