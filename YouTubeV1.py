# Cookbook type of code. By Crista lopes
'''import sys, string

# The shared mutable data
data = []
words = []
word_freqs = []

#
# The procedures
#
def read_file(path_to_file):
    """
    Takes a path to a file and assigns the entire
    contents of the file to the global variable data
    """
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())

def filter_chars_and_normalize():
    """
    Replaces all nonalphanumeric chars in data with white space
    """
    global data
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()

def scan():
    """
    Scans data for words, filling the global variable words
    """
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()

def remove_stop_words():
    global words
    with open('../stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)

def frequencies():
    """
    Creates a list of pairs associating
    words with frequencies
    """
    global words
    global word_freqs
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])

def sort():
    """
    Sorts word_freqs by frequency
    """
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)


#
# The main function
#
read_file(sys.argv[1])
filter_chars_and_normalize()
scan()
remove_stop_words()
frequencies()
sort()

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])'''


'''This code is similar to what I have coded. The cookbook method of
coding has a procedural processing of code. One function processes only
one activity. No single function processes two activities. In my example, I
have separated url making, url opening, data decoding and data printing.
This is method is given the name cookbook because this code goes in a
sequence flow just like the sequence flow of ingredients in a cookbook.'''


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
                 ('maxResults', '5'), ('chart', 'mostPopular'),
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
