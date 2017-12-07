#str1_list = ['j','d','j','o','d','o','k','p','w','s','u','v','h','u','b','x']
#alpha1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','z']
#str1 = ('abcdefghijklmnopqrstuvwxyz')

while True:
    str1= input("Enter the string: type Q or q to quit the program : ")
    if str1 == "q" or str1 == "Q":
        quit()
    else:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        al = 0
        for i in range(len(alpha)):
            s1 = alpha[i]
            if str1.count(s1) > 0:
                al = al+1
        if al == 26:
            print("The String contain all the letters")
        else:
            print("String does not have all the letters")
