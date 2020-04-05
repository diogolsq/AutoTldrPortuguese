
import requests, bs4 , time

from extractionpart1 import extraction
from selenium import webdriver

def treating(site):
    """
    parameter = url

    Getting the outbput of the extraction, simple interate over.
    """
    textcontent = extraction(site)


    article = ""
    global numberparagraphs

    numberparagraphs = 0

    for paragraph in textcontent:
        article +=  paragraph.text.strip() +'\n'
        numberparagraphs += 1

    return article



if __name__ == '__main__':
   print(treating("https://g1.globo.com/bemestar/coronavirus/noticia/2020/04/04/ministerio-da-saude-diz-que-4-estados-e-df-podem-estar-em-fase-de-transicao-para-aceleracao-descontrolada-de-coronavirus.ghtml"))