# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium_fixture import driver

def login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def number_of_movies(driver):
    """ Counting number of movies, taking into account that the movies
        in the last (4th) column have class name "movie_box last", and the rest
        have class name "movie_box" """
    return len(driver.find_elements_by_xpath("//div[@class='movie_box']")) +\
           len(driver.find_elements_by_xpath("//div[@class='movie_box last']"))

def number_of_movies_found(driver, movie_name):
    """ Find movies with specified name. """
    return len(driver.find_elements_by_xpath("//div[@title='" + movie_name + "']"))

def remove_first_by_name(driver, movie_name):
    driver.find_element_by_xpath("//div[@title='" + movie_name + "']").click()
    driver.find_element_by_xpath("//img[@alt='Remove']").click()
    driver.switch_to_alert().accept()

def clear_search(driver):
    """ Making sure that search edit box is clear """
    driver.find_element_by_id("q").clear()
    driver.find_element_by_id("q").send_keys(Keys.RETURN)

def test_remove_mov(driver):
    base_url = "http://localhost"
    driver.get(base_url + "/php4dvd/")
    login(driver)
    clear_search(driver)
    number_of_movies_before = number_of_movies(driver)
    movie_name = 'Movie #1'
    """ If found, then delete the first one """
    if number_of_movies_found(driver, movie_name) > 0:
        remove_first_by_name(driver, movie_name)
    else:
        print "There is no movie with specified title: ", movie_name

    number_of_movies_after = number_of_movies(driver)

    """ Checking if number of movies was decreased by 1 """
    if number_of_movies_after - number_of_movies_before == -1:
        print "The movie '" + movie_name + "' was successfully removed." \
                                           " Current number of movies: ", number_of_movies_after
    elif number_of_movies_after - number_of_movies_before == 0:
        print "The movie was not removed. Current number of movies: ", number_of_movies_after
    else:
        print "Something strange happened"

    logout(driver)

