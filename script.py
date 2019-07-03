#setup
from yandex.Translater import Translater
import sys,os
from keys import API_KEY
clear = lambda: os.system('cls')
filePath = sys.argv[1]

#opening files
wordSet = open(filePath,'r').read().split('\n')
wordSet_trd = open('translation.txt', 'w')

#setting up the API key
tr=Translater()
tr.set_key(API_KEY)

All_num = len(wordSet)
Done_num = 0

def translation(word):
    tr.set_from_lang('pl')
    tr.set_to_lang('en')
    tr.set_text(word)
    trd = tr.translate()
    return trd

#main
for word in wordSet:
    clear()
    print(str(Done_num) + "/" + str(All_num) + " done.")
    word_trd = translation(word)
    Done_num += 1
    wordSet_trd.write(word + " - " + word_trd + "\n")
    

#closing the files
wordSet_trd.close()