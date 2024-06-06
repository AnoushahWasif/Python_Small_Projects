from credentials import mobile_number
import requests
import schedule
import time

def send_message(message):
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': message,
        'key': 'textbelt',
    })
    print(resp.json())

def send_scheduled_message():
    message = "Hello, this is a test message"
    send_message(message)
    print("Message sent successfully")

# Schedule the task to be executed every day at 2:47:00
# schedule.every().day.at("02:47").do(send_scheduled_message)
schedule.every(200).seconds.do(send_scheduled_message)

while True:
    schedule.run_pending()
    time.sleep(1)