##Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order.
##A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    count=1
    listofnum=[2]
    if N<0:
        for j in (2,abs(N)):
            if abs(N)%j==0:
                break
            else:
                    count+=1
                    listofnum+=[N]
    elif N>0:
        for j in (2,N):
            if N%j==0:
                break
            elif j==(N-1):
                count+=1
                listofnum+=[N]
    print listofnum
#    listofnum=sort(listofnum)
#    
#def sort(listofnum):
#    
        
                
                 
            
            

    