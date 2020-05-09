
'''We are writing a code for getting the 5 most viewed videos on youtube in
24 hours.'''
import urllib.request
import urllib.parse
import json
# I generate my API key
myAPIkey = 'AIzaSyBiWL8nWR0wx5F7P_KDvgp3MoDjLZMUrfk'
# I set the parameters I want
parameters = [('key', myAPIkey), ('part', 'snippet, statistics'),
              ('maxResults', '10'), ('chart', 'mostPopular'),
              ('regionCode', 'us')]
# I write doen the url and save it to a variable
url = 'https://www.googleapis.com/youtube/v3/videos?'
url += urllib.parse.urlencode(parameters)
# The url is opened
info = urllib.request.urlopen(url)
# The information on the Url is read
readinfo = info.read()
# We convert the bytes infomation and decode the information
readinfo = json.loads(readinfo.decode(encoding='utf-8'))
# Then we just print out the title of the most viewed videos
print('Most viewed videos in the past 24 hours are:\n')
for i in readinfo['items']:
    print('Title:', i['snippet']['title'])
    print('Views', i['statistics']['viewCount'], end=' ')
    print('Likes', i['statistics']['likeCount'], '\n')
