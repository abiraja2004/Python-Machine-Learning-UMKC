str = "Hello this Is an Example With cased letters"
#str = input('Enter the string with comma')
#words = str.split()
#print(sorted(str))
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(sorted(words))

