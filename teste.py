"""
I am creating 2 instances, we going to be use 2 services to try bypass the possible paywall the first one is the outline
the second one is archive.is.

 attrs={'class' : 'content-text__container'}

"""

import requests, bs4 , time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#'https://g1.globo.com/politica/noticia/2020/03/25/em-reuniao-sobre-coronavirus-bolsonaro-e-doria-trocam-acusacoes.ghtml'

site = 'https://g1.globo.com/bemestar/coronavirus/noticia/2020/04/04/ministerio-da-saude-diz-que-4-estados-e-df-podem-estar-em-fase-de-transicao-para-aceleracao-descontrolada-de-coronavirus.ghtml'

def extraction(site):
    """
    extraction - parameters - the site url

    works in 3 parts:

    1.usage of selenium to navigate trough Chrome and send the link of the site to outline.
    2. using requests to extract the final result.
    3. using beatiful soup to parse the html to collect the text to be summarized.
    """


   # url = 'https://www.outline.com'
    #objeto = Options()
    #objeto.headless = True

    objeto = Options()
    #options= webdriver.ChromeOptions()
    #objeto.headless = True
    #options.add_argument("--incognito")
    browser = webdriver.Chrome()
    browser.get(f'https://www.outline.com/')
    time.sleep(5)
    siteinput = browser.find_element_by_id('source')
    siteinput.send_keys('https://www.wired.com/2014/07/history-of-autocorrect/')
    time.sleep(5)
    submitbutton = browser.find_element_by_css_selector('.main-button')
    submitbutton.click()
    print('clicked')
    time.sleep(30)




    res = requests.get(f'{browser.current_url}')

    print(res)
    print(browser.current_url)

    #browser.quit()



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