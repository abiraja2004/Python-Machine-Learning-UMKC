word_list = ["PHP","Exercises","Backend"]

x=[]



for i in range(len(word_list)):
    let = 0
    s1 = word_list[i]
    for char in s1:
        if char.isalpha():
            let = let+1
    s2 = (let,s1)
    x.append(s2)

print(x)



