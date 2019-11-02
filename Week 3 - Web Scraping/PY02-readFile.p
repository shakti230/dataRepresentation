from bs4 import BeautifulSoup

with open("../week02/Lab 02 - carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())
