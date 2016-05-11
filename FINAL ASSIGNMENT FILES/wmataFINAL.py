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

CONSUMER_KEY = 'fpnmBC0PYg0XqjolpAXbi2H0b'
CONSUMER_SECRET = 'rYrzqOr0x4i3LtM34B9cpxdkn0xgPHsvMDpwpapfySW4QCJuXR'
ACCESS_TOKEN = '730402984971141120-7H4H3DcZahPOEbPNDdS1zmHKKDb3awk'
ACCESS_TOKEN_SECRET = 'mXFRZAwGJE5Sj4iEd2WrXffKj4KzYvGdDmi4Cykd2KsOL'
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


#Function magic. This grabs the relevant json data, turns it into tweets and posts it
tweet_text_rail = "No incident on the Metro"
#tweet_text_bus = "No bus incident"

for incident in json_rail['Incidents']:
	if incident['Description'] not in tweeted_rail_incidents:
		tweeted_rail_incidents.append(incident)

		try:
		#Building the tweet by cleaning up the data and and trimming it to fit a tweet.
			line_affected = incident['LinesAffected'][:2]
			incident_description = incident['Description']
			
			tweet_text_rail = incident['IncidentType'] + ' at #DCMetro ' + incident_description
			
			tweet_text_rail = tweet_text_rail[:140]

		#Actually tweeting it
			twitter.update_status(status=tweet_text_rail)

		except TwythonError as e:
			print "Listening; nothing new to tweet"

	
#for incident in json_bus['BusIncidents']:
#	if incident['Description'] not in tweeted_bus_incidents:
#		tweeted_bus_incidents.append(incident)
#
#
#		try:
#
#		#Building the tweet and trimming it to fit a tweet.
#			#tweet_text_bus = 'New incident in the DC bus system: ' + incident['Description']
#			tweet_text_bus = incident['IncidentType'] + ' at DC bus route #' + incident['Description']
#			tweet_text_bus = tweet_text_bus[:140]	
#
#		#Actually tweeting it
#			twitter.update_status(status=tweet_text_bus)
#
#		except TwythonError as e:
#			print "Listening; nothing new to tweet"

#And just to check 
print('NEW TWEET: '+ tweet_text_rail)
#print('NEW TWEET: '+ tweet_text_bus)









#Reseting the list to test it again.
tweeted_rail_incidents = []
tweeted_bus_incidents = []





