import requests
import logging
import json

logger = logging.getLogger('movie-calendar')
HEADERS = {'User-Agent': 'api-client/0.1.3 com.douban.frodo/6.9.1'}
APIKEY = '0ab215a8b1977939201640fa14c66bab'

class Movie(object):
    def __init__(self,movie):
        self.movie = movie
    
    def get_rating(self):
        return self.movie['rating']
    
    def get_genres(self):
        return self.movie['genres']
    
    def get_putdate(self):
        return self.movie['pubdate']
    
    def has_linewatch(self): # 是否在线观看
        return self.movie['has_linewatch']

    def get_url(self):
        return self.movie['url']

    def get_title(self):
        return self.movie['title']

    def get_release_date(self):
        return self.movie['release_date']
    
    def get_pic(self,large=False):
        if large:
            return self.movie['pic']['large']
        else:
            return self.movie['pic']['normal']
    
    def get_subtype(self):
        return self.movie['subtype']
    
    def get_directors(self):
        return self.movie['directors']
    
    def is_show(self):
        return self.movie['is_show']

    def get_actors(self):
        return self.movie['actors']
    
    def is_release(self):
        return self.movie['is_release']
    
    def get_year(self):
        return self.movie['year']
    
    def get_card_subtitle(self):
        return self.movie['card_subtitle']
    
    def get_color_scheme(self):
        return self.movie['color_scheme']
    
    def get_type(self):
        return self.movie['type']

class MovieCalendar(object):
    def __init__(self,date):
        self.url = 'https://frodo.douban.com/api/v2/calendar/today'
        self.date = date
        self.json_result = self.request_url()

    def request_url(self):
        argv = {
            'apikey': APIKEY,
            'date': self.date
        }
        response = requests.get(self.url,params=argv,headers=HEADERS)
        # print(response.url)
        return response.json()

    def get_comment(self):
        return self.json_result['comment']
    
    def get_today(self):
        return self.json_result['today']
    
    def get_movie(self):
        return Movie(self.json_result['subject'])

if __name__ == "__main__":
    for i in range(1,30):
        date = '2019-01-' + '{:0>2d}'.format(i) 
        calendar = MovieCalendar(date)
        print(calendar.get_comment()['content'])
        movie = calendar.get_movie()
        print(movie.get_title())
        print(movie.get_directors()[0])
        
