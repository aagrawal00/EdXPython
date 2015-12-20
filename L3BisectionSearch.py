#my own implementation of bisection search

from random import randint
x=randint(1,25)
epsilon=0.01
numGuesses=0
low=0.0
high=x
ans=(low+high)/2.0
while (abs(ans**2-x)>=epsilon):
       print("Low=" + str(low) + "High=" + str(high) + "Ans=" + str(ans))
       if (ans**2>x):  
           high=ans
           ans=ans/2.0
       elif (abs(ans**2-x)>epsilon):
           low=ans
           ans=(low+high)/2

print("Square root of {0} is {1}",x,ans)           
           
        
