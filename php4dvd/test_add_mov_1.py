# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from user import User
from movie import Movie

def test_add_mov_1(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.clear_search()
    number_of_movies_before = app.number_of_movies()
    """ This movie will be added with success """
    app.add_movie(Movie.Movie_first())
    app.go_to_home_page()
    number_of_movies_after = app.number_of_movies()
    app.print_result_of_adding(number_of_movies_before, number_of_movies_after)
    app.logout()





