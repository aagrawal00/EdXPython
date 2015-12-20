##print("Please think of a number between 0 and 100!")
##low=0
##high=100
##guess=(high+low)/2
##while True:
##       print("Is your secret number " + str(guess) + "?")
##       print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
##       reply=str(raw_input())
##       replyrange = ['l','h','c']
##       if reply not in replyrange:
##               print("Sorry, I did not understand your input.")
##       elif reply == 'l':
##            low=guess
##            guess=(high+low)/2
##       elif reply == 'h':
##            high=guess
##            guess=(high+low)/2
##       elif reply =='c':
##            print("Game over. Your secret number was: " + str(guess))
##            break
##
##
print("Please think of a number between 0 and 100!")
low=0
high=100
guess=(high+low)/2
while True:
       print "Is your secret number %d?" %guess
       print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
       reply=str(raw_input())
       replyrange = ['l','h','c']
       if reply not in replyrange:
            print("Sorry, I did not understand your input.")
       elif reply == 'l':
            low=guess
            guess=(high+low)/2
       elif reply == 'h':
            high=guess
            guess=(high+low)/2
       elif reply =='c':
            print("Game over. Your secret number was: " + str(guess))
            break


