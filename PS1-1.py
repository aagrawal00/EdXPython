s='azcbobbobegghakl'
vowelcount=0
vowels = ["a","e","i","o","u"]
i=0
for i in range(0, len(s)-1):
        if s[i] == vowels[i]:
            vowelcount = vowelcount+1
print ('Number of vowels:' + str(vowelcount))
    
#while i<strlength:
#    compare=s[i]
#    if compare == 'a':
#        vowelcount=vowelcount+1
#        i=+1
#    elif compare == 'e':
#        vowelcount=vowelcount+1
#        i=i+1
#    elif compare == 'i':
#        vowelcount=vowelcount+1
#        i=i+1   
#    elif compare == 'o':
#        vowelcount=vowelcount+1
#        i=i+1
#    elif compare == 'u':
#        vowelcount=vowelcount+1
#        i=i+1
#    else:
#        i=i+1
#        
#print ('Number of vowels:' + str(vowelcount))