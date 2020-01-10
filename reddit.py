import json
import praw

with open('secrets.json', 'r') as f:
	secrets = json.load(f)

reddit = praw.Reddit(client_id=secrets['client_id'],
						client_secret=secrets['secret'],
						user_agent=secrets['user_agent'])

subreddit = reddit.subreddit('Nootropics')

top_subreddit = subreddit.top() # top 100 upvoted subbmissions to sub
top_subreddit = subreddit.top(limit=500) # top 500 upvoted submissions

for sub in top_subreddit:
	print(sub.title)

