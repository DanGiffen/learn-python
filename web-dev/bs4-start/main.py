from bs4 import BeautifulSoup
# import lmxl // if parsing error
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)