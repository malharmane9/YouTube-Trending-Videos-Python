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
                     ('maxResults', '10'), ('chart', 'mostPopular'),
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
