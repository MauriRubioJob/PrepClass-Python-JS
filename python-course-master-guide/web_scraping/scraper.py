import requests
from bs4 import BeautifulSoup

def naive_search(html_code):
    profile_name_index = html_code.index("profile-name")
    print(f"{profile_name_index = }")
    closing_tag_index = html_code.index(">", profile_name_index)
    print(f"{closing_tag_index = }")
    opening_tag_index = html_code.index("<", profile_name_index)
    print(f"{opening_tag_index = }")
    name = html_code[closing_tag_index + 1 : opening_tag_index]
    print(f"{name = }")


def bs_search(html_code):
    soup = BeautifulSoup(html_code, features="html.parser")
    attributes = { "class": "profile-name" }
    name_tag = soup.find(attrs=attributes)
    print(name_tag.text)

    print(soup.img["src"])

    print(soup.find_all(attrs={"class":"menu-option"}))


with open("page2.html", "r") as html:
    html_code = html.read()

    # naive_search(html_code)
    bs_search(html_code)

    