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


@app.schedule('cron(30 1 ? * MON *)')
def notify_dishdash(event):
    message = "Hi Guys! Don't forget to order next week's DishDash! https://www.dishdash.co/ "
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}
