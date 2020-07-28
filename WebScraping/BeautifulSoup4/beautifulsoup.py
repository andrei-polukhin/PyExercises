from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    contents = file.read()
simple_soup = BeautifulSoup(contents, 'html.parser')


def find_paragraph():
    paragraph = simple_soup.find('p')
    print(paragraph.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(", ".join(list_contents))


def find_important():
    para = simple_soup.find('p', {'class': 'important'})
    print(para.string)


def find_usual():
    # a beautiful workaround by me!
    usual_paragraph = simple_soup.find('p', {'class': None})
    print(usual_paragraph.string)


def find_other():
    all_paragraphs = simple_soup.find_all('p')
    other_paragraphs = [
        p.string for p in all_paragraphs
        if p.attrs.get('class') != 'subtitle'
    ]
    print(other_paragraphs[0])
