from selenium.webdriver.common.keys import Keys
import time

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go_to_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

    def number_of_movies(self):
        """ Counting number of movies, taking into account that the movies
            in the last (4th) column have class name "movie_box last", and the rest
            have class name "movie_box" """
        driver = self.driver
        return len(driver.find_elements_by_xpath("//div[@class='movie_box']")) +\
               len(driver.find_elements_by_xpath("//div[@class='movie_box last']"))

    def number_of_movies_found(self, movie):
        """ Find movies with specified name. """
        driver = self.driver
        return len(driver.find_elements_by_xpath("//div[@title='" + movie.movie_name + "']"))

    def remove_first_by_name(self, movie):
        driver = self.driver
        driver.find_element_by_xpath("//div[@title='" + movie.movie_name + "']").click()
        driver.find_element_by_xpath("//img[@alt='Remove']").click()
        driver.switch_to_alert().accept()

    def get_movie_name(self, movie):
        return movie.movie_name

    def clear_search(self):
        """ Making sure that search edit box is clear """
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(Keys.RETURN)

    def add_movie(self, movie):
        driver = self.driver
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie.movie_name)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys(movie.year)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(movie.notes)
        driver.find_element_by_id("submit").click()

    def print_result_of_adding(self, number_of_movies_before, number_of_movies_after):
        if number_of_movies_after - number_of_movies_before == 1:
            print "The movie was successfully added. Current umber of movies: ", number_of_movies_after
        elif number_of_movies_after - number_of_movies_before == 0:
            print "The movie was not added. Current umber of movies: ", number_of_movies_after
        else:
            print "Something strange happened"

    def print_result_of_removing(self, number_of_movies_before, number_of_movies_after, movie_name=""):
        """ Checking if number of movies was decreased by 1 """
        if number_of_movies_after - number_of_movies_before == -1:
            print "\nThe movie '" + movie_name + "' was successfully removed." \
                                               "\nCurrent number of movies: ", number_of_movies_after
        elif number_of_movies_after - number_of_movies_before == 0:
            print "\nThe movie was not removed. \nCurrent number of movies: ", number_of_movies_after
        else:
            print "\nSomething strange happened"

    def enter_text_to_search(self, text_to_search):
        driver = self.driver
        driver.find_element_by_id("q").send_keys(text_to_search)
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        time.sleep(2)