import random
from instapy import InstaPy
from instapy import smart_run
from getpass import getpass
import time

# login credentials
print("Hi!\nThis script will automate commenting on black square posts on the #blacklivesmatter hashtag asking to please remove it, \nsuch that useful info for the movement is not hidden behind a wall of black squares. \nIt uses very rudimentary AI, and is by no means perfect. \nIt may comment on posts that are not just black squares. \nIf you want to stop the script from running at any point, press Ctrl+C in the command line. \nThanks!\n")

comments = []
with open('comments.txt', 'r') as fp:
	for line in fp:
		comment = line.replace("\n", "")
		if comment:
			comments.append(comment)

insta_username = input("what's your instagram username?\n> ")
insta_password = getpass("what's your instagram password?\n> ")

# get a session!
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

tags = ['blacklivesmatter']

session.set_comments(comments)
session.set_use_clarifai(enabled=True, api_key="15d4d2a1d8ec46e996f8bf95fbb6b6c2", probability = 0.99)

with smart_run(session):
	session.set_sleep_reduce(50)
	session.set_do_comment(enabled = True, percentage = 100)
	session.like_by_tags(tags, amount=100, skip_top_posts=True)
	session.clarifai_check_img_for(['not-blackout'], comment=True, comments = comments)


