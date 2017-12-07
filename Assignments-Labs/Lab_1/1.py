
infile = open("file1.txt",'r')

x=[]
count = 0
line = infile.readline()
while line != "":
    for xStr in line.split(" "):
        x.append(xStr)
        count = count + 1
    line = infile.readline()
x1 = str(x)
#print(x)

def word_count(str1):
    co = dict()
    wo = str1.split()

    for word in wo:
        if word in co:
            co[word] += 1
        else:
            co[word] = 1

    return co

print(word_count(x1))
