import requests
import time


request_params = { 'token': 'YOUR_TOKEN'}
num = -1

print('Gametime is in 1 minute')

warn = 'Gametime is in 1 minute'

post_params = { 'bot_id' : 'YOUR_BOT_ID', 'text': warn }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)

time.sleep(59)

t_end = time.time() + 60
while time.time() < t_end:

    response = requests.get('https://api.groupme.com/v3/groups/YOUR_GROUP_ID/messages', params = request_params)


    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']


        for message in response_messages:
            if (message['text'] == 'Woopig' or 'woopig'):

                print('Complete')
                print(str(num))
                num += 1

                to_send = ''

                post_params = { 'bot_id' : 'YOUR_BOT_ID', 'text': to_send }
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                request_params['since_id'] = message['id']
                break

print('The number of Woo Pigs was ' + str(num))

send = 'The number of Woo Pigs was ' + str(num)

post_params = { 'bot_id' : 'YOUR_BOT_ID', 'text': send }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
