'''I am writing a code for getting the most viewed youtube videos.'''
import urllib.request
import urllib.parse
import json

# I assign my Api key to a variable for reccuring use in different functions
myAPIkey = 'AIzaSyBiWL8nWR0wx5F7P_KDvgp3MoDjLZMUrfk'


def make_url():
    '''This function just makes the url.'''
    # We write the url and assing it to a variable
    url = 'https://www.googleapis.com/youtube/v3/videos?'
    # We set the parameters we want to search
    parameter = [('key', myAPIkey), ('part', 'snippet, statistics'),
                 ('maxResults', '10'), ('chart', 'mostPopular'),
                 ('regionCode', 'us')]
    url += urllib.parse.urlencode(parameter)
    # we call the open_url function to open the url
    data = open_url(url)
    # The we call the print_data function to print the data
    print_data(data)


def open_url(url):
    '''This function opens the url and reads the information.'''
    response = urllib.request.urlopen(url)
    inf = response.read()
    response.close()
    # Data needs to be decoded hence the function is called.
    inf = decode_data(inf)
    # Decoded data is returned.
    return inf


def decode_data(data):
    '''This function decdes the data from a bytes string to python readable
    data.'''
    data = data.decode(encoding='utf-8')
    data = json.loads(data)
    # Data is decoded and returned
    return data


def print_data(data):
    '''This function deals only with the printing of the desired
    information.'''
    print('These are the 5 most watched videos in the past 24 hours.\n')
    for i in data['items']:
        print('Title:', i['snippet']['title'])
        print('Views', i['statistics']['viewCount'], end=' ')
        print('Likes', i['statistics']['likeCount'], '\n')


if __name__ == '__main__':
    # We call the function from here
    make_url()
