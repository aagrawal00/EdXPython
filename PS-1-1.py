##Write a program that counts up the number of vowels contained in the string s.
##Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
##For example, if s = 'azcbobobegghakl', your program should print:

##Number of vowels: 5

##For problems such as these, do not include raw_input statements or define
##the variable s in any way. Our automated testing will provide a value of s
##for you - so the code you submit in the following box should assume s is already
##defined. If you are confused by this instruction, please review L4 Problems 10
##and 11 before you begin this problem set.

s = 'azcbobobegghakl'
booltest=False
lengthofstring=len(s)
count=0
for i in range(0,lengthofstring):
    booltest=(s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U')
    if  booltest:
        count+=1
        
print("Number of vowels: " + str(count))
