from bs4 import BeautifulSoup
import pdb
import lxml
import requests
import json


word_lists = {
    'types': [
        {
            'list_type' : 'animals',
            'url'       : 'https://enchantedlearning.com/wordlist/animal.shtml'
        },
        {
            'list_type' : 'adjectives',
            'url'       : 'https://enchantedlearning.com/wordlist/adjectives.shtml'
        }
    ]
}

def word_scraper(list_type, url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    list_ = []

    for item in soup.find_all('div', class_='wordlist-item'):
        try:
            if item.find('a').text:
                text = item.find('a').text
                if len(text) < 6:
                    if ' ' not in text:
                        list_.append(text)

        except AttributeError:
            text = item.text
            if len(text) < 6:
                if ' ' not in text:
                    list_.append(text)
            

    return list_

def generate_lists(l):
    
    for entry in l['types']:
        ltype = entry['list_type']
        url = entry['url']
        
        entry['list'] = word_scraper(list_type=ltype, url=url)

def main():
    generate_lists(word_lists)

if __name__ == '__main__':
    main()
