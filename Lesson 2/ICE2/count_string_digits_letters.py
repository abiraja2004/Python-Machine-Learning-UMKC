str1_list = ['j','d','j','o','d','o','k','p','w','s','u','v','h','u','b','x']
str1 = 'jdj12okpws1235'
let = 0
dig = 0
for char in str1:
     if char.isalpha():
         let =let+1
     if char.isdigit():
         dig=dig+1
print("The string is ",str1)
print('the total letters are',let)
print('the total digit are',dig)
