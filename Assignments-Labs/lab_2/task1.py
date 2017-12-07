#Write a program that accepts a sentence as input and remove duplicate words .
#Sort them alphanumerically and print it.
#Sample Input:
#hello world and practice makes perfect and hello world again
#Sample Output:
#again and hello makes perfect practice world

words = input("Enter sequence of words separated by whitespace: ").split(' ')
words_set = set(words)
print(' '.join(sorted(words_set)))
print(words_set)