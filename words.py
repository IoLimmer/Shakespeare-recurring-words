import english_words as engwords
import wordfreq as wf
from random import randint
import re
import os

import utils



# print(utils.DIRECTORY)


words = list(engwords.get_english_words_set(['web2'], lower=True))
words.sort()


with open(os.path.join(utils.DIRECTORY, "macbeth2.txt"), "r") as file:
    macbeth = file.read()
    # macbeth = re.sub("\n+", "\n", macbeth)

# print(macbeth)
maclist = macbeth.split(" ")

for i in range(100):
    print(maclist[i], end=", ")
    print(wf.zipf_frequency(maclist[i], 'en'))


    
# print("God says")
# for x in range(10):
#     word = words[randint(0, len(words))]
#     print(word, end=", ")
#     print(wf.zipf_frequency(word, 'en'))