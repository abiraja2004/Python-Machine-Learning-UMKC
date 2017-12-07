fileName = "file1.txt"
infile = open(fileName, 'r')

print(sum(len(line.split()) for line in open(fileName)))