from bs4 import BeautifulSoup
import requests
import lxml


def words():

    site = requests.get('https://www.ef.com/wwen/english-resources/english-vocabulary/top-1000-words/').text

    # print(site)

    soup = BeautifulSoup(site, 'lxml')

    # print(soup)

    word = soup.find('div', class_='content').text

    para = word.split()

    return para



