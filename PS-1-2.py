##Write a program that prints the number of times the string 'bob' occurs in s.
##For example, if s = 'azcbobobegghakl', then your program should print

##Number of times bob occurs is: 2

##For problems such as these, do not include raw_input statements or define
##the variable s in any way. Our automated testing will provide a value of s
##for you - so the code you submit in the following box should assume s is already
##defined. If you are confused by this instruction, please review L4 Problems 10
##and 11 before you begin this problem set.

s='azcbobobegghaklbob'
count=0
strlen=len(s)
for i in range(0,strlen-2):
    finder=s[i:i+3]
    booltest=(finder[0]=='b' and finder[1]=='o' and finder[2]=='b')
    if booltest:
        count+=1

print("Number of times bob occurs is: " + str(count))
