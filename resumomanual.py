"""
This script was made for Vínicius R. Lima with a few changes, you can see he explaining his code in :

https://medium.com/@viniljf/utilizando-processamento-de-linguagem-natural-para-criar-um-sumariza%C3%A7%C3%A3o-autom%C3%A1tica-de-textos-775cb428c84e


"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

def resumo(texto):
    sentencas  = sent_tokenize(texto,'portuguese')
    palavras = word_tokenize(texto.lower())

    stopword = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopword]
    frequencia = FreqDist(palavras_sem_stopwords)

    sentencas_importantes = defaultdict(int)

    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]

    idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

    artigoresumido = ""
    for i in sorted(idx_sentencas_importantes):
        artigoresumido += sentencas[i]

    return artigoresumido

