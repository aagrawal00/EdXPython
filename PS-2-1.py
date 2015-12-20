# -*- coding: utf-8 -*-
##Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
##
##The following variables contain values as described below:
##
##    balance - the outstanding balance on the credit card
##
##    annualInterestRate - annual interest rate as a decimal
##
##    monthlyPaymentRate - minimum monthly payment rate as a decimal
##
##For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:
##
##Month: 1
##Minimum monthly payment: 96.0
##Remaining balance: 4784.0
##
##Be sure to print out no more than two decimal digits of accuracy - so print
##
##Remaining balance: 813.41
##
##instead of
##
##Remaining balance: 813.4141998135 
##
##Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:
##
##Total paid: 96.0
##Remaining balance: 4784.0
##
##A summary of the required math is found below:
##
##    Monthly interest rate= (Annual interest rate) / 12.0
##    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
##    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
##    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
##
##Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below;
##we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
##New things learnt - 1.Declaring an empty list in python 2.Rounding to n digits
balance=4213.0
annualInterestRate=0.2
monthlyPaymentRate=0.04
b=[0]*15
monthlyinterestrate=(annualInterestRate)/12.0
totalpaid=0
for i in range(1,13):
     print('Month: ' + str(i))
     print("Minimum monthly payment: " + str(round(balance*monthlyPaymentRate,2)))
     totalpaid+=balance*monthlyPaymentRate
     b[i]=balance-(balance*monthlyPaymentRate)
     balance=(b[i]+(monthlyinterestrate*b[i]))
     print("Remaining Balance: " + str(round(balance,2)))
print("Total Paid: " + str(round(totalpaid,2)))
print("Remaining Balance: " + str(round(balance,2)))
##	      Test Case 1:
##	      balance = 4213
##	      annualInterestRate = 0.2
##	      monthlyPaymentRate = 0.04
##	      
##	      Result Your Code Should Generate:
##	      -------------------
##	      Month: 1
##	      Minimum monthly payment: 168.52
##	      Remaining balance: 4111.89
##	      Month: 2
##	      Minimum monthly payment: 164.48
##	      Remaining balance: 4013.2
##	      Month: 3
##	      Minimum monthly payment: 160.53
##	      Remaining balance: 3916.89
##	      Month: 4
##	      Minimum monthly payment: 156.68
##	      Remaining balance: 3822.88
##	      Month: 5
##	      Minimum monthly payment: 152.92
##	      Remaining balance: 3731.13
##	      Month: 6
##	      Minimum monthly payment: 149.25
##	      Remaining balance: 3641.58
##	      Month: 7
##	      Minimum monthly payment: 145.66
##	      Remaining balance: 3554.19
##	      Month: 8
##	      Minimum monthly payment: 142.17
##	      Remaining balance: 3468.89
##	      Month: 9
##	      Minimum monthly payment: 138.76
##	      Remaining balance: 3385.63
##	      Month: 10
##	      Minimum monthly payment: 135.43
##	      Remaining balance: 3304.38
##	      Month: 11
##	      Minimum monthly payment: 132.18
##	      Remaining balance: 3225.07
##	      Month: 12
##	      Minimum monthly payment: 129.0
##	      Remaining balance: 3147.67
##	      Total paid: 1775.55
##	      Remaining balance: 3147.67
##	
##                
##
##                  
##	      Test Case 2:
##	      balance = 4842
##	      annualInterestRate = 0.2
##	      monthlyPaymentRate = 0.04
##	      
##	      Result Your Code Should Generate:
##	      -------------------
##	      Month: 1
##	      Minimum monthly payment: 193.68
##	      Remaining balance: 4725.79
##	      Month: 2
##	      Minimum monthly payment: 189.03
##	      Remaining balance: 4612.37
##	      Month: 3
##	      Minimum monthly payment: 184.49
##	      Remaining balance: 4501.68
##	      Month: 4
##	      Minimum monthly payment: 180.07
##	      Remaining balance: 4393.64
##	      Month: 5
##	      Minimum monthly payment: 175.75
##	      Remaining balance: 4288.19
##	      Month: 6
##	      Minimum monthly payment: 171.53
##	      Remaining balance: 4185.27
##	      Month: 7
##	      Minimum monthly payment: 167.41
##	      Remaining balance: 4084.83
##	      Month: 8
##	      Minimum monthly payment: 163.39
##	      Remaining balance: 3986.79
##	      Month: 9
##	      Minimum monthly payment: 159.47
##	      Remaining balance: 3891.11
##	      Month: 10
##	      Minimum monthly payment: 155.64
##	      Remaining balance: 3797.72
##	      Month: 11
##	      Minimum monthly payment: 151.91
##	      Remaining balance: 3706.57
##	      Month: 12
##	      Minimum monthly payment: 148.26
##	      Remaining balance: 3617.62
##	      Total paid: 2040.64
##	      Remaining balance: 3617.62
