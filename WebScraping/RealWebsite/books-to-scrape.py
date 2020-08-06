import re

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Selectors:
    titles = "div[class=\"container-fluid page\"] div.page_inner div.row " \
             "div[class=\"col-sm-8 col-md-9\"] section div " \
             "ol.row li article h3 a"
    warning = "div[class=\"container-fluid page\"] div.page_inner div.row " \
              "div[class=\"col-sm-8 col-md-9\"] " \
              "section div[class=\"alert alert-warning\"]"
    images = "div[class=\"container-fluid page\"] div.page_inner div.row " \
             "div[class=\"col-sm-8 col-md-9\"] section div " \
             "ol.row li article div[class=image_container] a img"
    categories = "div[class=\"container-fluid page\"] div.page_inner div.row " \
                 "aside div.side_categories ul li ul li a"


class BooksToScrape:
    def __init__(self, url):
        self.url = url
        html = urlopen(url).read()
        self.soup = BeautifulSoup(html, "html.parser")

    def get_titles(self):
        list_links = self.soup.select(Selectors.titles)
        print("\n--------Our list of books--------")

        for n, title in enumerate(list_links):
            list_links[n] = title.attrs["title"]
            print(list_links[n])
        print("\n")

    def get_warning(self):
        repr_warning = self.soup.select(Selectors.warning)
        pattern = "\<\/strong\> ([A-Za-z0-9 ,.]+)\<\/div\>"
        text_warning = str(repr_warning[0])
        matcher = re.search(pattern, text_warning)
        print("\n--------The website\'s warning--------")
        print(matcher.group(1), "\n")

    def get_images(self):
        img_list = self.soup.select(Selectors.images)
        print("\n--------Here are links to images--------")
        for n, img in enumerate(img_list):
            img_list[n] = {
                img.attrs["alt"]: "{}{}".format(self.url, img.attrs["src"])
            }
            for text, link in img_list[n].items():
                print(text, ": ", link)
        print("\n")

    def get_genres(self):
        genres_in_a = self.soup.select(Selectors.categories)
        print("\n--------Here are all the genres--------")
        for n, genre in enumerate(genres_in_a):
            genres_in_a[n] = genre.string.strip()
            print(genres_in_a[n])
        print("\n")
