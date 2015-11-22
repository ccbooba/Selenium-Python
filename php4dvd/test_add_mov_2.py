# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
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
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Movie #2")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Not worth seeing")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()
        number_of_movies_after = len(driver.find_elements_by_xpath("//div[@class='movie_box']")) +\
                                 len(driver.find_elements_by_xpath("//div[@class='movie_box last']"))
        if number_of_movies_after - number_of_movies_before == 1:
            print "The movie was successfully added. Current number of movies: ", number_of_movies_after
        elif number_of_movies_after - number_of_movies_before == 0:
            print "The movie was not added. Current number of movies: ", number_of_movies_after
        else:
            print "Something strange happened"
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(),
                                 r"^Are you sure you want to log out[\s\S]$")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
