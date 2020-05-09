'''import re, string, sys

stops = set(open("../stop_words.txt").read().split(",") + list(string.ascii_lowercase))
words = [x.lower() for x in re.split("[^a-zA-Z]+", open(sys.argv[1]).read()) if len(x) > 0 and x.lower() not in stops]
unique_words = list(set(words))
unique_words.sort(key=lambda x: words.count(x), reverse=True)
print("\n".join(["%s - %s" % (x, words.count(x)) for x in unique_words[:25]]))'''


'''This method aims at using as less lines of code as possible. Hence it does
no include any comments. but I have included cmments in my code for the
sake of understanding and marks. This code is consice and uses as many
libraries as possible to lower the number of lines. My code is similar
to this code and it ensure the minimal steps requirement. This method is
called the code golf style. it is called so because in golf the ball is
supposed to be hiit in the hole in less number of shots.'''

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
