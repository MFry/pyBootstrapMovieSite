#!/usr/bin/env python

import webbrowser
import os
import re

__author__ = 'Michal Frystacky'

"""
This is a modified version of Movie Trailer Website codebase.
 Found at:  https://docs.google.com/a/knowlabs.com/document/d/1joDQNQl_4icYYm6tM_F9ch5hZEH_f157hlljSUGOLWs/pub?embedded=true

 The program takes a
"""

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            padding-bottom: 60px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .summary {
            height:264px;
            overflow: hidden;
            -ms-text-overflow: ellipsis;
            -o-text-overflow: ellipsis;
            text-overflow: ellipsis;
            padding: 0;
        }

        .title {
            position: absolute;
            top: 400px;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">

            <div class=".container">
                <img class="col-md-7" src="{poster_image_url}" width="220" height="339">
                 <h5><b>Summary: </b></h5>
                <div class="col-md-5 summary">
                <p>
                    {summary}
                </p>
                </div>
            </div>
            <div class=".container-fluid">
                <strong>Director:</strong> {director}<br>
                <strong>Stars:</strong> {stars}
            </div>

            <div class=".container title">
                <h2 class="text-center">{movie_title}</h2>
            </div>
</div>
'''
# template to create google linked names
movie_talent_content = '<a href="http://www.google.com/search?q={query}">{name}</a>'


def create_movie_tiles_content(movies):
    """
        Generates movie tiles HTML code and inserts it into main page head
    :param movies:
     :type movies: list[Movie]
    :return: a generated HTML page with movie tiles inserted
    :rtype: str
    """
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                summary=movie.summary_text,
                director=construct_google_link(movie.director),
                stars=construct_google_link(*movie.stars)
        )
    return content


def construct_google_link(*names):
    """
        A program that takes strings of names and creates google links with html code out of them
    :param names: arbitrary many string containing names split by space. (e.x. arnold schwarzenegger)
     :type names: list[str]
    :return: A string containing a google link linking the names to google results.
                (e.x. <a href="http://www.google.com/search?q=Colin+Farrell">Colin Farrell</a>)
     :rtype: str
    """
    return_link = ''
    for name in names:
        if return_link != '':
            return_link += ', '
        name_parts = name.split(' ')
        # for people with multiple names
        query = ''
        for part in name_parts:
            if query != '':
                query += '+'
            query += part
        return_link += movie_talent_content.format(query=query,
                                                   name=name)

    return return_link


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
            movie_tiles=create_movie_tiles_content(movies),
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
