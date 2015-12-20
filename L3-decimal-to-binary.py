number=int(raw_input())
userinput=number
if userinput<0:
        userinput=abs(userinput)
        isNEG=True
        result=''
else:
        isNEG=False
        result=''
if userinput==0:
        result='0'
elif userinput>=1:
        while userinput>=1:
            binarybit=userinput%2
            result=str(binarybit)+result
            userinput=userinput/2
if isNEG==True:
    result='-'+result
print('binary of input number {0} is {1}', number, result)
        
        
