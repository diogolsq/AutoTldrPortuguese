"""
Hello, world!

This is a program to be used on reddit, with intention to create summarys of news, in portuguese, when possible
bypassing some paywalls. The bot will create a post in the same thread that someone post a news, will be similar
to the already known bot called AutoTldr.

Salve, esse será um programa a ser utilizado no reddit ,com intuito de realizar
resumos de reportagens em português e colocar na mesma thread em que alguém postou
a reportagem, será similar com o bot já existente AutoTldr.

obs: TLDR é uma sigla para Time is limited didn't read.


Instruções para os Devs:
O programa será feito então em 3 etapas:

a) puxar um request do site da notícia - check
b) burlar o paywall da notícia, mexendo direto no código de JavaScript da página
c) criar um resumo da notícia e se o texto for reduzido em ao menos 50% do tamanho original, realizar um post
na thread.

"""

import requests,bs4
from extraction import extraction
from resumomanual import resumo

#'https://g1.globo.com/politica/noticia/2020/03/25/em-reuniao-sobre-coronavirus-bolsonaro-e-doria-trocam-acusacoes.ghtml'
#https://oglobo.globo.com/brasil/na-contramao-de-bolsonaro-mourao-diz-que-posicao-do-governo-pelo-isolamento-social-24328130

texttosummarize = extraction('https://g1.globo.com/politica/noticia/2020/03/25/em-reuniao-sobre-coronavirus-bolsonaro-e-doria-trocam-acusacoes.ghtml')
summarized = str(resumo(texttosummarize))


reductionsize = 1 - (len(summarized)/len(texttosummarize))

if reductionsize >= 0.5:
    print(f'a reportagem original foi reduzida em em {(1 - (len(summarized)/len(texttosummarize))) * 100} % ' + '\n')
    print(summarized)
