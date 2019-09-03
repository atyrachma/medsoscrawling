import pandas as pd

search_results = api.search(q="bigdata", count=100)
datatw = pd.DataFrame()
datatw["text"] = [tweet.text.lower() for tweet in search_results]
datatw["created_at"] = [tweet.created_at for tweet in search_results]
datatw["retweet_count"] = [tweet.retweet_count for tweet in search_results]
datatw["user_screen_name"] = [tweet.author.screen_name for tweet in search_results]
datatw["user_followers_count"] = [tweet.author.followers_count for tweet in search_results]
datatw["user_location"] = [tweet.author.location for tweet in search_results]

datatw.to_csv("bigdata.csv")
