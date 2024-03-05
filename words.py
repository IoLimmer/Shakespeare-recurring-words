import english_words as engwords


words = list(engwords.get_english_words_set(['web2'], lower=True))

words.sort()
for x in range(10):
    print(words[x])


