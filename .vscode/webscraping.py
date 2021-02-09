import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Impossible_world')

soup = bs4.BeautifulSoup(res.text,"lxml")

