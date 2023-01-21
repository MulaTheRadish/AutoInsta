#Import configuration file.
import config
#Import necessary functions/ libraries.
import os
import praw
import urllib.request
from PIL import Image

from instapy_cli import client

#logging into reddit using credentials from config file. 
reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    user_agent = config.user_agent
)

#Declaring subreddit
subreddit = reddit.subreddit("animemes")

#Taking the top submission of the day from the subreddit declared. 
for submission in subreddit.top(limit = 1):
    #Turning the URL of the image in the reddit post into a PIL image for editing. 
    urllib.request.urlretrieve(submission.url, 'meme.jpeg')
    meme = Image.open('meme.jpeg')
    
    #Finding offset to format reddit meme onto instagram post format. 
    if meme.width > meme.height:
        dimensions = meme.width, meme.width
    else:
        dimensions = meme.height, meme.height

    #Creating and formatting instagram post. 
    bg = Image.new(mode = "RGB", size = dimensions, color = 'black')
    offset = (bg.width - meme.width) // 2, (bg.height - meme.height) // 2
    bg.paste(meme, offset)
    bg.save('post.jpeg')
  
    #Unnecessray PIL image occasionally created, removed. 
    if os.path.exists('meme.jpeg'):
        os.remove('meme.jpeg')

    #Uploading photo to instagram with submission title as caption. 
    with client(config.username, config.password) as cli:
        cli.upload('post.jpeg', submission.title)
