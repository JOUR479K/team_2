##WMATA incidents bot

Elaine Hunt, Danielle Ling and Daniel Trielli


Inspired by the common occurrences of incidents and problems in the Washington DC Metro, our idea was to create a Twitter bot that alerts followers about metro incidents in real time. 

Luck would have it, the Washington Metropolitan Area Transit Authority (WMATA) has an API that provides real-time data on bus and rail incidents. The data is updated every 20 to 30 seconds.

The challenge then was to combine the WMATA API with the Twitter API and construct the tweets from the data provided.

In summary, the code is divided in these parts:
- Necessary imports: requests and twython
- Authenticating with WMATA API
- Pulling data from WMATA API
- Authenticating with Twitter
- Function that builds tweets and tweets them out

The data comes from WMATA as a JSON array called "Incidents". Within Incidents there are the useful elements such as "Description (a "Free-text description of the incident") IncidentType and LinesAffected. These were the elements we used to build the tweets.

One of the challenging aspects was understanding how to parse those elements, finding them within the JSON structure and turn them into strings. When we did that, it was easier to build the tweets.

The writing of the tweets combined the elements mentioned above with a hashtag. We experimented with a couple of variations until there was one that was both readable and with the information we needed.

If we had more time in this project, we would have added an interactive element to it, that would listen to specific tweets and responded to Twitter users.

The end result can be seen at twitter.com/WMATAAlertBot



