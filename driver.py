import os
import fresh_tomatoes
from media import Movie

__author__ = 'michalfrystacky'

# expected order of data in text files for generating a Movie object
NAME = 0
IMG_URL = 1
YOUTUBE_TRAILER = 2
SUMMARY = 3
DIRECTOR = 4
# index 5+ is assumed to be stars


def main():
    # path containing movies data
    path = 'movies/'
    # container for movie objects
    movies = []
    # find all the files (we assume that the folder contains nothing but readable text files containing movie data)
    for _, _, files in os.walk(path):
        for file in files:
            with open(path + file) as f:
                lines = f.read().split('\n')
                movies.append(Movie(lines[NAME],
                                    lines[IMG_URL],
                                    lines[YOUTUBE_TRAILER],
                                    lines[SUMMARY],
                                    lines[DIRECTOR],
                                    *lines[DIRECTOR + 1:]))

    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__": main()
