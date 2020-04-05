# AutoTldrPortuguese

This is the core script to be implemented in a Reddit Bot, to do a TLDR for post in the portuguese language.

**What is a TLDR?** 
TLDR is an acronym for Too Long, Didn't Read. Basically the bot will summarize a news, bypassing a eventual paywall.

## How does it work?
The script can be devided in 3 parts : 
* Extraction:
    * bypassing the paywall via outline.com
    * extracting the Html aknowlodging that some sections of it was putted dinamically through JavaScript.
* Treatment;
 
* Summarizing;
    
## Stepping Stones
This is for the coders and curious people, i am going to create a explanation for each stage of the devolopment and i will comment for the 
problems that i've encountered, so this could be a light for anyone trying to implement something alike.

### Extraction
A good way to bypass the now common paywall of any big news site is to use the site outline.com, outline will create a page with the final
news structured easilly.
So a few things that we will have to deal with, outline takes some time to actually give you the final result, and the final result is made 
throught javascripts pulls, so packages like Request,Urllib, etc won't work, since the object that they pull are not completed with all the site information.

the script for extraction was made using Selenium, which basically opens a browser himself, goes to the site, do the request, using Time make it to wait a little bit
and them pull the final result, this is mandatory, let selenium itself to pull the html **does not use others packages**, selenium will adress the javascript generated chunks of html,
to use him properly use the method ".page_source", this all happens hidden, you can make it visible with a few change in the code.

### Treatment

Easy interation to get the request, treat a little bit to pass to be summarize, will make that html snippets only in a text that can be summerized,
doesn't need a further explanation.

### Sumarizing
**Shout out for Vinícius R. Lima**

We currently have some packages in python that does it for you, but instead i picked some code that already existed and made some tweaks, for those
who knows portuguese i'let that author himself make his explanation, you can visit at:

https://medium.com/@viniljf/utilizando-processamento-de-linguagem-natural-para-criar-um-sumariza%C3%A7%C3%A3o-autom%C3%A1tica-de-textos-775cb428c84e

for those who doesn't know portuguese i'll make a easy explanation of every section of the script.

First we going to use NTLK ( Natural Language Toolkit) and some of their packages.

We start by breaking the raw text in sentences and words using the tokenize functions.
Second step is to take all the stopwords, which is words that doesn't bring any meaning and is only serves to creat sintax conection, we should take all 
the punctations as well.
Third step is to get all the words that are still in there and make some frequency destribution analysis to see which of them are the most
important.
we will create a defaultdict to put the 'score'of the most important words.
we will iterate over all the sentences, if the word is in the frequency variable, we going to add in the default dictionary the key is the index of the world and the value is
 the frequency of the world, then we can know wich sentences are the most important and how many them we will want to be the summarized version.
 
 
 
 









