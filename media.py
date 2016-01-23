__author__ = 'Michal Frystacky'


class Movie:
    def __init__(self, title, poster_image_url, youtube_url, summary, director, *stars):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url
        self.summary_text = summary
        self.director = director
        self.stars = []
        for star in stars:
            self.stars.append(star)
