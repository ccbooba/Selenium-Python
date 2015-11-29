# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from user import User
from movie import Movie

def test_search_mov(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.clear_search()
    text_to_search = 'mov'
    app.enter_text_to_search(text_to_search)
    number_of_movies_found = app.number_of_movies()
    print "Number of movies found: ", number_of_movies_found
    app.logout()

