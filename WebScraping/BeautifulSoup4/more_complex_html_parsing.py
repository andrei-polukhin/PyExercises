import re

from bs4 import BeautifulSoup

with open("middle.html", "r") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")


def find_header():
    selector = "div.header h1 a"  # class -> element
    item_link = soup.select_one(selector).attrs["href"]
    print(
        f"The header link is <{item_link}>."
    )


def find_price():
    """
    Specifying [id=...] is redundant in this case (only one image)
    but if there are several, <id> is unique -> easy-to-find.
    """

    selector = "div.contents img[id=unlocking_android]"
    item_price = soup.select_one(selector).attrs["alt"]
    print(item_price)  # Unlocking Android: $12.99
    pattern = "\$([0-9]+\.[0-9]{,2})"
    matcher = re.search(pattern, item_price)
    print(matcher.group(0))  # $12.99
    print(matcher.group(1))  # 12.99


def find_rating():
    selector = "div.ratings ul li"
    item_ratings = soup.select(selector)
    for n, rating in enumerate(item_ratings):
        item_ratings[n] = float(rating.string)
    average = sum(item_ratings)/len(item_ratings)

    attr_selector = "div.ratings ul"
    name_of_selector = soup.select_one(attr_selector).attrs["id"]

    print(
        f"From {name_of_selector} the average rating is "
        f"{average}/10."
    )
