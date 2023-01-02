#this tokenizes the dataset into words.
import nltk
from nltk import ngrams
import io

#Downloads the punk if not already downloaded.

#Step 1: Get data.
from ngram.bigram import bigram_runner, get_best_bigram
from ngram.unigram import unigram_runner, get_best
from otherFunctions.helperFunctions import smaller

#Texts to test!
tests = ["cin seddi sinirina yaklastilar",
         "baskentinin istedigi buydu",
         "guneye dogru ilerlediler",
         "uc tane asker cin'in hakimiydi",
         "suslu manciniklari ogretti",
         "yapabilecek durumda degildi",
         "muhafiz kitasi oldu",
         "surlara dogru surdu",
         "oldugu tartisma konusudur",
         "celaleddin'in pesine dustu",
         "ayrildigi haberini aldi",
         "hanedaninin tavrini unutmamisti",
         "ele gecirmek konu oldu",
         "oncu birlik dayanmisti",
         "ilk kez gerceklesmisti",
         "cengiz han da ona katildi",
         "sehri ele gecirdi",
         "yapabilecek durumda degildi",
         "saldiri tuzagı kurmustu",
         "duvarlari onune yıgdı",
         ]

unigram_enabled = 1
bigram_enabled = 1

if unigram_enabled:
    file_5 = io.open("5.txt", encoding="utf8")
    text_5 = file_5.read()

    token_5 = nltk.word_tokenize(text_5)

    lower_text_5 = "" #This is converted to smaller caps version
    for token in token_5:
        lower_text_5 += smaller(token) + " "

    lower_token_5 = nltk.word_tokenize(lower_text_5)

    un = unigram_runner(lower_token_5)

    for test in tests:
        get_best(test, un)

#######################################################################################

if bigram_enabled:
    file_2 = io.open("02.txt", encoding="utf8")
    text_2 = file_2.read()

    token_2 = nltk.word_tokenize(text_2)

    lower_text_2 = "" #This is converted to smaller caps version
    for token in token_2:
        lower_text_2 += smaller(token) + " "

    lower_token_2 = nltk.word_tokenize(lower_text_2)

    bi = bigram_runner(lower_token_2)

    for test in tests:
        get_best_bigram(test, bi)