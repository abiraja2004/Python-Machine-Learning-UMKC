
from nltk.corpus import wordnet as wn
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
import re, collections
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
from nltk import FreqDist
import nltk

#-	Read the file
file = open('input.txt', 'r')
fr = file.readline()

#tokenize word
fr_word = word_tokenize(fr)
fr_sent = sent_tokenize(fr)

#-	Using Lemmatization, apply lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
fr_lemma = []
for word in fr_word:
    fr_lema = lemmatizer.lemmatize(word.lower())
    fr_lemma.append(fr_lema)

print("\n after lemmetaizion  ")
print(fr_lemma)


fr_pos = pos_tag(fr_lemma)
print("\n before removing verbs:")
print(fr_pos)

fr_pos_verbs= [s for s in fr_pos if s[1]!= 'VB'and'VBD'and'VBG'and'VBN'and'VBP'and'VBZ'and'.'and','and'?'and'!']
print("\n after removing verbs:")
print(fr_pos_verbs)



str1 = " ".join(str(x) for x,y in fr_pos)
str1_word = word_tokenize(str1)
fdist1 = nltk.FreqDist(fr_lemma)
top_five = fdist1.most_common(5)
print("\n Top five words")
print(top_five)

sent1 = sent_tokenize(fr)
rep_sent1 = []

for sent in sent1:
  for word in word_tokenize(sent):
    for (k, l) in top_five:
       if word == k:
         rep_sent1.append(sent)  # Creating sentences containing the most common words
print ("\n Sentences with top five words")
print(rep_sent1)

