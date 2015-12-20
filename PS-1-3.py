##Assume s is a string of lower case characters.
##
##Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
##For example, if s = 'azcbobobegghakl', then your program should print
##
##Longest substring in alphabetical order is: beggh
##In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
##
##Longest substring in alphabetical order is: abc

##For problems such as these, do not include raw_input statements or define
##the variable s in any way. Our automated testing will provide a value of s
##for you - so the code you submit in the following box should assume s is already
##defined. If you are confused by this instruction, please review L4 Problems 10
##and 11 before you begin this problem set.
s = 'azcbobobegghakl'
comparisonstring=''
booltest=True
strlen=len(s)
for i in range(strlen):
        longstring=''
        j=i
        while (booltest==(s[j]<s[j+1]):
              longstring+=s[j]
              j+=1
        if (longstring>comparisonstring):
            comparisonstring=longstring
print('Longest substring in alphabetical order is: ' + comparisonstring)
