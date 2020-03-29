"""
I am creating 2 instances, we going to be use 2 services to try bypass the possible paywall the first one is the outline
the second one is archive.is.

 attrs={'class' : 'content-text__container'}

"""

"""
I am creating 2 instances, we going to be use 2 services to try bypass the possible paywall the first one is the outline
the second one is archive.is.

 attrs={'class' : 'content-text__container'}

"""

import requests, bs4 , time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#'https://g1.globo.com/politica/noticia/2020/03/25/em-reuniao-sobre-coronavirus-bolsonaro-e-doria-trocam-acusacoes.ghtml'

site = 'https://g1.globo.com/politica/noticia/2020/03/25/em-reuniao-sobre-coronavirus-bolsonaro-e-doria-trocam-acusacoes.ghtml'

def extraction(site):
    """
    extraction - parameters - the site url

    works in 3 parts:

    1.usage of selenium to navigate trough Chrome and send the link of the site to outline.
    2. using requests to extract the final result.
    3. using beatiful soup to parse the html to collect the text to be summarized.
    """
    browser = webdriver.Chrome('/Users/user/Downloads/chromedriver')
    browser.get('https://www.outline.com')
    time.sleep(5)
    searchBar = browser.find_element_by_id('source')
    searchBar.send_keys(site)
    searchBar.send_keys(Keys.ENTER)

    time.sleep(10)
    res = requests.get(f'{browser.current_url}', allow_redirects = True)


    try:# checklist para ver se foi tudo baixada nos conforme
        res.raise_for_status()
    except Exception as exc:
        print(f'Houve um problema : {exc}')

    htmlcontent = bs4.BeautifulSoup(res.text, features= 'html.parser')


    #article = htmlcontent.select('p .content-text__container')

    textcontent = htmlcontent.find_all('p') # Find_all creates a set

    article = ''
    global numberparagraphs
    numberparagraphs = 0
    for paragraph in textcontent:
        article +=  paragraph.text.strip() +'\n'
        numberparagraphs += 1

    return article



extraction(site)