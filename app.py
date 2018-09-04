from chalice import Chalice
from datetime import datetime

import os
import requests

import json

app = Chalice(app_name='slackBotWines')
app.debug = True

slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']


@app.schedule('cron(0 9 ? * FRI *)')
def notify_wines_friday(event):
    currentDate = datetime.now().strftime("%Y-%m-%d")
    message = "Today is Friday[%s]; Please remember to input your WINES for this week" % currentDate
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}

@app.schedule('cron(0 9 L * ? *)')
def notify_wines_last_day_of_month(event):
    currentMonth = datetime.now().strftime('%B')
    message = "Today is the last day of the month of %s; Please remember to input your WINES" % currentMonth
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}

@app.schedule('cron(30 1 ? * MON,WED *)')
def notify_dishdash(event):

    # Send first reminder message on Monday
    if datetime.today().weekday() == 0:
        message = "Hi Guys! Don't forget to order next week's DishDash! https://www.dishdash.co/ "
    else:
        message = "Guys... If you don't order now, you won't have food on your table next week.. Order Here! " \
                  "https://www.dishdash.co/ "
    response = requests.post(slack_webhook_url, data=json.dumps({'text': message}))
    return {'message': json.dumps(message)}

@app.route('/lunch', methods=['POST'], content_types=['application/json',
                          'application/x-www-form-urlencoded'])
def notify_lunch_time():
    message = "It's Bento time! " \
              "Enjoy your Lunch! \n " \
              "You've been served by RMinder "
    return {
        "response_type": "in_channel",
        'text': message
    }
