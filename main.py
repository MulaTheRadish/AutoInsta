#Import configuration file.
import config
#importing necessary functions.
import os
import glob
#importing necessary libraries.
import praw
import urllib.request
from PIL import Image
from instabot import Bot

#Consistant cookie file created upon startup; must be deleted everytime the program is run again. 
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

#Signing into instagram using credentials from config.
bot = Bot()
bot.login(
    username = config.username,
    password = config.password
)

#Signing into reddit using credentials from config.
reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    user_agent = config.user_agent
)

#Declaring subreddit. 
subreddit = reddit.subreddit("animemes")

#Taking the top submission of the day from the subreddit declared. 
for submission in subreddit.top(limit = 1):
    #Turning the URL of the image in the reddit post into a PIL image for editing. 
    urllib.request.urlretrieve(submission.url, 'meme.png')
    meme = Image.open('meme.png')
    
    #Finding offset to format reddit meme onto instagram post format. 
    if meme.width > meme.height:
        dimensions = meme.width, meme.width
    else:
        dimensions = meme.height, meme.height

    #Creating and formatting instagram post. 
    bg = Image.new(mode = "RGB", size = dimensions, color = 'black')
    offset = (bg.width - meme.width) // 2, (bg.height - meme.height) // 2
    bg.paste(meme, offset)
    bg.save('post.png')

    #Uploading photo to instagram account using the reddit title as a caption. 
    bot.upload_photo('post.png', caption = submission.title)
   
#PIL image is occasionally saved in directory; is deleted after the program is run. 
if os.path.exists('meme.png'):
    os.remove('meme.png')
