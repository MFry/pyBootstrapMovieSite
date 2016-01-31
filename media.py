#!/usr/bin/env python
"""
 Container class for parameters that are used to create a movie tile
"""
__author__ = 'Michal Frystacky'


class Movie:
    """
        Container for extracted movie information data
    """
    def __init__(self, title, poster_image_url, youtube_url, summary, director, *stars):
        """
            Constructor that requires all the arguments and an arbitrary many stars (1+) that will be passed to
            fresh_tomatoes.py to generate movie tiles
        :param title: The movie name (e.x. Terminator)
         :type title: str
        :param poster_image_url: A string to a location of an image of the movie poster (e.x. images/red_poster.img,
            http://www.impawards.com/2012/posters/django_unchained_xlg.jpg)
         :type poster_image_url: str
        :param youtube_url: A url to a trailer hosted on youtube (e.x. https://www.youtube.com/watch?v=nlvYKl1fjBI)
         :type youtube_url: str
        :param summary: A summary text of the movie (such as the ones found on imdb)
         :type summary: str
        :param director: The main director of the movie
         :type director: str
        :param stars: An unpacked list of stars (e.x. "Taylor Kitsch", "Lynn Collins", "Willem Dafoe"
         :type stars: str
        :return: Nothing
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url
        self.summary_text = summary
        self.director = director
        self.stars = []
        for star in stars:
            self.stars.append(star)
