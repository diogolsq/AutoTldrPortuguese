"""
    extraction - parameters - the site url

    works in 3 parts:

    1.usage of selenium to navigate trough Chrome and send the link of the site to outline. - This script -
    2. using requests to extract the final result.(X) Use selenium instead to get the page_source, that way will
     get the part of the source that is putted dinamically through Java Script- this script.
    3. using beatiful soup to parse the html to collect the text to be summarized. - this script.

"""


import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import time

#site = 'https://g1.globo.com/bemestar/coronavirus/noticia/2020/04/04/ministerio-da-saude-diz-que-4-estados-e-df-podem-estar-em-fase-de-transicao-para-aceleracao-descontrolada-de-coronavirus.ghtml'
def extraction(site):
    try:
        donotopenbrowser = Options()
        donotopenbrowser.headless = True
        browser = webdriver.Chrome(options = donotopenbrowser) # if you wanna see tha magic going on, erase the parameter given)
        browser.get('https://outline.com')
        time.sleep(5)
        siteinput = browser.find_element_by_css_selector('.source-input')
        siteinput.click()
        siteinput.send_keys(site)
        time.sleep(5)
        submitbutton = browser.find_element_by_css_selector('.main-button')
        submitbutton.click()
        time.sleep(10)
    finally:
        linktoread = browser.current_url
        print(f'leia a reportagem integral sem eventual paywall em :  {linktoread}')
        htmlcontent = bs4.BeautifulSoup(browser.page_source, features= 'html.parser')
        time.sleep(2)
        textcontent = htmlcontent.find_all('p')


        browser.quit()
        return textcontent

if __name__ == '__main__':
    print(outlining("https://g1.globo.com/bemestar/coronavirus/noticia/2020/04/04/ministerio-da-saude-diz-que-4-estados-e-df-podem-estar-em-fase-de-transicao-para-aceleracao-descontrolada-de-coronavirus.ghtml"))