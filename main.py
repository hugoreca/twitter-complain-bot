from speedtest_bot import SpeedTest
from twitter_bot import TweetBot
import os

PROMISED = 20

# Get the Download speed from Speedtest
speed_bot = SpeedTest()
real_down = speed_bot.get_internet_speed()

# Complain or congrats accordingly
tweet_bot = TweetBot()
tweet_bot.tweet_at_provider(real_down, os.getenv('USER'), os.getenv('PWD'))
