# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium_fixture import app
from user import User
from movie import Movie

def test_remove_mov(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.clear_search()
    number_of_movies_before = app.number_of_movies()
    movie_name = 'Movie #5'
    movie_name = app.get_movie_name(Movie.Movie_first())
    """ If found, then delete the first one """
    if app.number_of_movies_found(Movie.Movie_first()) > 0:
        app.remove_first_by_name(Movie.Movie_first())
    else:
        print "\nThere is no movie with specified title: ", movie_name

    number_of_movies_after = app.number_of_movies()

    """ Checking if number of movies was decreased by 1 """
    if number_of_movies_after - number_of_movies_before == -1:
        print "\nThe movie '" + movie_name + "' was successfully removed." \
                                           "\nCurrent number of movies: ", number_of_movies_after
    elif number_of_movies_after - number_of_movies_before == 0:
        print "\nThe movie was not removed. \nCurrent number of movies: ", number_of_movies_after
    else:
        print "\nSomething strange happened"

    app.logout()

