#!/usr/bin/env python

"""
 Program that interfaces with the user and calls all other programs to generate the final page.
  Takes an optional single command line arguments and looks fora  folder defined in the argument.
"""

import os
import argparse
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
    # get help and setup to acceptcommand line arguments
    parser = argparse.ArgumentParser(description="Generate Bootstrap movie site.")
    parser.add_argument('PATH', metavar='PATH', type=str,
                        help='Location of the folder containing movie text files. \n  (default: movies/)',
                        default='movies/')
    # path containing movies data
    args = parser.parse_args()
    path = args.PATH
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
