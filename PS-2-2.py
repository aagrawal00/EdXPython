##Problem 2: Paying Debt Off In A Year (1 point possible)
##
##Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
##By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
##
##In this problem, we will not be dealing with a minimum monthly payment rate.
##
##The following variables contain values as described below:
##
##    balance - the outstanding balance on the credit card
##
##    annualInterestRate - annual interest rate as a decimal
##
##The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
##
##Lowest Payment: 180 
##
##Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
##The monthly payment must be a multiple of $10 and is the same for all months.
##Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
##
##    Monthly interest rate = (Annual interest rate) / 12.0
##    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
##    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
balance=40773
originalbalance=balance
annualInterestRate=0.2
monthlyInterestRate=(annualInterestRate/12.0)
minmonthlypayment=0
while balance>0:
    balance=originalbalance
    minmonthlypayment+=.01
    for i in range(1,13):
            monthlyUnpaidBalance=(balance-minmonthlypayment)
            balance=(monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
print("Lowest Payment: " + str(minmonthlypayment))
##            print("monthlyUnpaidBalance for month " + str(i) + " is " + str(round(monthlyUnpaidBalance,2)))
##            print("balance at the end of " + str(i) + " months is " + str(round(balance,2)))
##Test Cases:                      
##Test Case 1:
##balance = 3329
##annualInterestRate = 0.2
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 310
##                      
##Test Case 2:
##balance = 4773
##annualInterestRate = 0.2
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 440
##                   
##Test Case 3:
##balance = 3926
##annualInterestRate = 0.2
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 360
