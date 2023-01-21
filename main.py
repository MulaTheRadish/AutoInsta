import config
import os
import glob
import praw
import urllib.request
from PIL import Image
from instabot import Bot

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

bot = Bot()
bot.login(
    username = config.username,
    password = config.password
)

reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    user_agent = config.user_agent
)

subreddit = reddit.subreddit("animemes")

for submission in subreddit.top(limit = 1):
    urllib.request.urlretrieve(submission.url, 'meme.png')
    meme = Image.open('meme.png')
    
    if meme.width > meme.height:
        dimensions = meme.width, meme.width
    else:
        dimensions = meme.height, meme.height

    bg = Image.new(mode = "RGB", size = dimensions, color = 'black')
    offset = (bg.width - meme.width) // 2, (bg.height - meme.height) // 2
    bg.paste(meme, offset)
    bg.save('post.png')

    bot.upload_photo('post.png', caption = submission.title)
    
if os.path.exists('meme.png'):
    os.remove('meme.png')
