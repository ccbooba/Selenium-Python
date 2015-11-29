# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from user import User
from movie import Movie

def test_remove_mov(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.clear_search()
    number_of_movies_before = app.number_of_movies()
    movie_to_remove = Movie.Movie_second()
    movie_name = app.get_movie_name(movie_to_remove)
    """ If found, then delete the first one """
    if app.number_of_movies_found(movie_to_remove) > 0:
        app.remove_first_by_name(movie_to_remove)
    else:
        print "\nThere is no movie with specified title: ", movie_name
    number_of_movies_after = app.number_of_movies()
    app.print_result_of_removing(number_of_movies_before, number_of_movies_after, movie_name)
    app.logout()

