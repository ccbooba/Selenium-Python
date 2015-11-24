# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#from selenium_fixture import driver

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_remove_mov(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        """ Counting number of movies, taking into account that the movies
             in the last (4th) column have class name "movie_box last", and the rest
             have class name "movie_box" """
        number_of_movies_before = len(driver.find_elements_by_xpath("//div[@class='movie_box']")) +\
                                  len(driver.find_elements_by_xpath("//div[@class='movie_box last']"))

        movie_name = 'Movie #1'

        """ Find movies with specified name.
            If found, then delete the first one"""
        if len(driver.find_elements_by_xpath("//div[@title='" + movie_name + "']")) > 0:
            driver.find_element_by_xpath("//div[@title='" + movie_name + "']").click()
            driver.find_element_by_xpath("//img[@alt='Remove']").click()
            driver.switch_to_alert().accept()
        else:
            print "There is no movie with specified title: ", movie_name

        number_of_movies_after = len(driver.find_elements_by_xpath("//div[@class='movie_box']")) +\
                                 len(driver.find_elements_by_xpath("//div[@class='movie_box last']"))
        if number_of_movies_after - number_of_movies_before == -1:
            print "The movie '" + movie_name + "' was successfully removed." \
                                               " Current number of movies: ", number_of_movies_after
        elif number_of_movies_after - number_of_movies_before == 0:
            print "The movie was not removed. Current number of movies: ", number_of_movies_after
        else:
            print "Something strange happened"
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

if __name__ == "__main__":
    unittest.main()
