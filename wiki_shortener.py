# -*-coding:utf-8 -*
import re
import urllib.request
from bs4 import BeautifulSoup

def first_par():
    """Print the first paragraph of the researched wikipedia article.
    
    Research is currently limited to one word, one language,
    and must have one occurence on Wikipedia. Improvement must be made
    with the search word(s) (capitalize or not, more than one word,
    multiple occurences...).
    """
    
    language = 'en'
    print('The current language is {}'.format(language))
    
    search = ''
    while search == '':
        search = input('Enter a search to get a short summary: ').capitalize()
    
    link = 'https://' + language + '.m.wikipedia.org/wiki/' + search
    
    with urllib.request.urlopen(link) as url:
        # 'Soup' of the html page extracted from the link
        soup = BeautifulSoup(url.read(), 'html.parser')
        # Finding the first bold occurrence of the search
        # and retrieving the parent's text
        parent_text = soup.find('b', text=search).parent.get_text()
        
        # Text cleanup: removing citations marks
        clean = re.sub('[\[][0-9]*?[\]]', '', parent_text)
        
        print(clean)


if __name__ == "__main__":
    import os
    first_par()
    os.system('pause')