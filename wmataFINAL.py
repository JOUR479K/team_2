import requests
from twython import Twython
from twython import TwythonError, TwythonRateLimitError, TwythonAuthError
twitter = Twython()

#Grabbing stuff from the WMATA API

url_param = {'api_key': '3c1275f8a9a44dba91b79c2acdac77d5'}
r_rail = requests.get('https://api.wmata.com/Incidents.svc/json/Incidents', params=url_param)
r_bus = requests.get('https://api.wmata.com/Incidents.svc/json/BusIncidents', params=url_param)

#Converting data into json and creating an empty tweet list so things don't get retweeted (I think Twitter doesn't allow repeat tweets anyway, but it's best to be safe)

json_rail = r_rail.json()
json_bus = r_bus.json()
tweeted_rail_incidents = []
tweeted_bus_incidents = []



#Authenticating our Twitter account. This data is for the test tweet. TO DO: Create our definitive Twitter account and change the keys

CONSUMER_KEY = 'yx3Jc3Uizy0Ma0dtFWbTGUBLJ'
CONSUMER_SECRET = '7bIIHXHGiOKcILa8tUInmKl5qbDaxFsay3zhXrIwiheYrtx98f'
ACCESS_TOKEN = '722873455578775553-qe4o1yIcaXai1lsFJZw4HDAVkwjiJnt'
ACCESS_TOKEN_SECRET = 'og61R7JIRGRfwLsTyBhk7pcm87KL2zfalQwsBf8oe8V1D'
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


#Function magic. This grabs the relevant json data, turns it into tweets and posts it

for incident in json_rail['Incidents']:
	if incident['Description'] not in tweeted_rail_incidents:
		tweeted_rail_incidents.append(incident)

		#Building the tweet and trimming it to fit a tweet.
		tweet_text_rail = 'New incident in the DC Metro: ' + incident['Description']
		tweet_text_rail = tweet_text_rail[:140]

		#Actually tweeting it
		try:
			twitter.update_status(status=tweet_text_rail)
		except TwythonError as e:
			print "Listening; nothing new to tweet"

for incident in json_bus['BusIncidents']:
	if incident['Description'] not in tweeted_bus_incidents:
		tweeted_bus_incidents.append(incident)

		#Building the tweet and trimming it to fit a tweet.
		tweet_text_bus = 'New incident in the DC bus system: ' + incident['Description']
		tweet_text_bus = tweet_text_bus[:140]	

		#Actually tweeting it
		try:
			twitter.update_status(status=tweet_text_bus)
		except TwythonError as e:
			print "Listening; nothing new to tweet"


#And just to check 
print('NEW TWEET: '+ tweet_text_rail)
print('NEW TWEET: '+ tweet_text_bus)

#Reseting the list to test it again.
tweeted_rail_incidents = []
tweeted_bus_incidents = []
