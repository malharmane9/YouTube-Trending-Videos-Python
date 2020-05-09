'''import sys, re, operator, collections

class WordFrequenciesModel:
    """ Models the data. In this case, we're only interested
    in words and their frequencies as an end result """
    freqs = {}
    stopwords = set(open('../stop_words.txt').read().split(','))
    def __init__(self, path_to_file):
        self.update(path_to_file)

    def update(self, path_to_file):
        try:
            words = re.findall('[a-z]{2,}', open(path_to_file).read().lower())
            self.freqs = collections.Counter(w for w in words if w not in self.stopwords)
        except IOError:
            print("File not found")
            self.freqs = {}

class WordFrequenciesView:
    def __init__(self, model):
        self._model = model

    def render(self):
        sorted_freqs = sorted(self._model.freqs.items(), key=operator.itemgetter(1), reverse=True)
        for (w, c) in sorted_freqs[0:25]:
            print(w, '-', c)

class WordFrequencyController:
    def __init__(self, model, view):
        self._model, self._view = model, view
        view.render()

    def run(self):
        while True:
            print("Next file: ") 
            sys.stdout.flush() 
            filename = sys.stdin.readline().strip()
            self._model.update(filename)
            self._view.render()


m = WordFrequenciesModel(sys.argv[1])
v = WordFrequenciesView(m)
c = WordFrequencyController(m, v)
c.run()'''


'''This syle of coding is also called MVC. In my code I have used three
classes of Model, controller and view. this resembles the idea of christa
lopes code. it has a structural organisation unlike any other. The advantage
of this type of coding is that more code can be added or existing code can
be altered without hindering any prevailing process. it is really useful in
software development. The view only present things to the user controller
conects the view and the model, the model is where the actual functioning
happens.'''


import urllib.request
import urllib.parse
import json


class Youtubemodel:
    '''We create the model class where all the functionality happens.'''
    def __init__(self):
        pass

    def url_make(self, key):
        '''We make our url here.'''
        url = 'https://www.googleapis.com/youtube/v3/videos?'
        # The parameters are used for getting the desired result
        parameter = [('key', key), ('part', 'snippet, statistics'),
                     ('maxResults', '5'), ('chart', 'mostPopular'),
                     ('regionCode', 'us')]
        url += urllib.parse.urlencode(parameter)
        # We return the complete url
        return url

    def url_open(self, url):
        '''This method opens the url and reads it.'''
        response = urllib.request.urlopen(url)
        # The url is read and the information is stored
        inf = response.read()
        response.close()
        # The stored information is returned
        return inf

    def data_decode(self, data):
        '''This method decodes the data we need.'''
        data = data.decode(encoding='utf-8')
        data = json.loads(data)
        # The decoded data is returned
        return data


class Youtubecontroller:
    '''We create the controller class as a connection between the
    model and the view.'''
    def __init__(self):
        self.x = Youtubemodel()

    def make_url(self, key):
        '''This calls the url_make method in model.'''
        return self.x.url_make(key)

    def open_url(self, url):
        '''This calls the url_open method in the model.'''
        return self.x.url_open(url)

    def decode_data(self, data):
        '''This calls the data_decode method in the model.'''
        return self.x.data_decode(data)


class YoutubeView:
    '''We create a view class that prints to the screen and maintains
    the running of the code.'''
    def __init__(self):
        # We create an API key
        self.myAPIkey = 'AIzaSyBiWL8nWR0wx5F7P_KDvgp3MoDjLZMUrfk'
        self.y = Youtubecontroller()

    def get_data(self):
        '''This is the main running method of the module.'''
        # We call to make url
        url = self.y.make_url(self.myAPIkey)
        # We call to open url
        data = self.y.open_url(url)
        # We call to decode and get data
        ddata = self.y.decode_data(data)
        # And then we print necessary data
        print('Most viewed videos in the past 24 hours are:\n')
        for i in ddata['items']:
            print('Title:', i['snippet']['title'])
            print('Views', i['statistics']['viewCount'], end=' ')
            print('Likes', i['statistics']['likeCount'], '\n')


if __name__ == '__main__':
    # We call classes and methods from here
    u = YoutubeView()
    u.get_data()
