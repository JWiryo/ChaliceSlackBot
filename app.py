from chalice import Chalice
from datetime import datetime

import os
import requests

import json

app = Chalice(app_name='slackBotWines')
app.debug = True

slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']


@app.route('/wines')
def notify_wines():
    currentDate = datetime.now().strftime("%Y-%m-%d")
    message = "Today is %s; Please remember to input your WINES for this week" % currentDate
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}


@app.schedule('cron(30 1 ? * MON,WED *)')
def notify_dishdash(event):
    if datetime.today().weekday() == 1:
        message = "Hi Guys! Don't forget to order next week's DishDash! https://www.dishdash.co/ "
    else:
        message = "Guys... If you don't order now, you won't have food on your table next week.. Order Here! " \
                  "https://www.dishdash.co/ "
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}
