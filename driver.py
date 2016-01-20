__author__ = 'michalfrystacky'

import fresh_tomatoes
from media import Movie

def main():
    movies = []
    # total recall
    t = Movie('Total Recall',
              'http://www.impawards.com/2012/posters/total_recall_ver12_xlg.jpg',
              'https://www.youtube.com/watch?v=_pV2zz3z0oM')
    movies.append(t)
    # Age of Adaline
    t = Movie('Age of Adaline',
              'http://www.impawards.com/2015/posters/age_of_adaline_ver13_xlg.jpg',
              'https://www.youtube.com/watch?v=7UzSekc0LoQ')
    movies.append(t)
    # Red
    t = Movie('Red',
              'http://www.impawards.com/2010/posters/red_xlg.jpg',
              'https://www.youtube.com/watch?v=SHPti5AVZXU')
    movies.append(t)
    # Star Trek
    t = Movie('Star Trek',
              'http://www.impawards.com/2009/posters/star_trek_xi_ver16_xlg.jpg',
              'https://www.youtube.com/watch?v=iGAHnZ555nI')
    movies.append(t)
    # John Carter
    t = Movie('John Carter',
              'http://www.impawards.com/2012/posters/john_carter_xlg.jpg',
              'https://www.youtube.com/watch?v=nlvYKl1fjBI')
    movies.append(t)
    # Django Unchained
    t = Movie('Django Unchained',
              'http://www.impawards.com/2012/posters/django_unchained_xlg.jpg',
              'https://www.youtube.com/watch?v=eUdM9vrCbow')
    movies.append(t)

    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__": main()