from selenium.webdriver.common.keys import Keys

class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        driver = self.driver
        base_url = "http://localhost"
        driver.get(base_url + "/php4dvd/")

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
        driver = self.driver
        return movie.movie_name

    def clear_search(self):
        """ Making sure that search edit box is clear """
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(Keys.RETURN)