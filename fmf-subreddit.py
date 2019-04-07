import praw
import os
import time
from time import sleep
import requests
from time import sleep, strftime, gmtime
from random import randint

post_params = { 'bot_id' : 'your_bot_id', 'text': "starting bot reddit frugal bot" }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
 
reddit = praw.Reddit(user_agent='your agent name',
                     client_id='your client id', client_secret="your client secret")
# initilizes the time the bot starts running
start_time = time.time()
client_error = False
while True:
    try:
        for post in reddit.subreddit('frugalmalefashion').new():
            # Sends message if reddit was down and has come back up
            if client_error == True:
                post_params = { 'bot_id' : 'your_bot_id', 'text': "Reddit is back online" }
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                client_error = False
            # prints only the new posts 
            if post.created_utc > start_time:
                post_params = { 'bot_id' : 'your_bot_id', 'text': post.title +": https://www.reddit.com" + post.permalink }
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
    # sends an error message when reddit is down
    except praw.exceptions.ClientException as e:
        if client_error == False:
            post_params = { 'bot_id' : 'your_bot_id', 'text': "client error" }
            requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            client_error = True
        sleep(150)

    sleep(randint(60, 140))
