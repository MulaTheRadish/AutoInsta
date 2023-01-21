# AutoInsta

Take the image of the most upvoted post from subreddit and upload it to instagram. 

## Problems:
Because of Meta's strict API on automated posting, commenting and liking, current libraries and APIs are not able to 'bypass' the Instagram API. Hence why there are two files in this repository. [Instabot.py](https://github.com/MulaTheRadish/AutoInsta/blob/main/instabot.py) uses the [instabot](https://instagrambot.github.io/docs/en/) library whilst [instapy_cli.py](https://github.com/MulaTheRadish/AutoInsta/blob/main/instapy_cli.py) uses the [instapy-cli](https://pypi.org/project/instapy-cli/) library. 

However, both work in a similar fashion using [PRAW](https://www.google.com/search?q=PRAW+python&oq=PRAW+python&aqs=chrome..69i57l2j69i59j69i60l3.1031j0j7&sourceid=chrome&ie=UTF-8). 
1. Get the link of the image. 
2. Use PIL to format the image into a 1:1 JPG/ JPEG/ PNG. 
3. Upload the image onto instagram. 

Unfortuantely, neither `instabot` nor `instapy-cli` currently bypass Meta's API. 

### Instabot error code:
```
2023-01-21 20:12:29,874 - ERROR - Error unknown send request
FOUND: w:850 h:850 r:1.0
2023-01-21 20:12:38,504 - ERROR - Photo Upload failed with the following response: <Response [400]>
2023-01-21 20:12:38,505 - INFO - Photo 'post.png' is not uploaded.
2023-01-21 20:12:38,507 - INFO - Total requests: 31
```

### Instapy-cli error code:
```
[IG] not found cookie/cookie_file >> login as default
Error parsing error response: Expecting value: line 1 column 1 (char 0)
Error is >>
    Not Found

Something went bad.
Please retry or send an issue on https://github.com/b3nab/instapy-cli

Traceback (most recent call last):
  File "/Users/mula/Documents/Projects/Python Projects/Autoinstagram/main.py", line 37, in <module>
    cli.upload('post.jpeg', caption)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/instapy_cli/cli.py", line 153, in upload
    raise IOError("Unable to upload.")
OSError: Unable to upload.
```

I favor `instapy-cli` because of its simplicity, but neither function...
