#Edward J Moon
#IT-140 Intro to Scripting
#Instructor: Zoe Likoudis
import sys 
#starting balance 
account_balance = float(500.25)
#define functions
#functions start with a capital letter to distinguish them from vars

#Functions can be prewritten in the language, such as the print() function, or
#they can be custom, like the four functions I've written below. Custom functions
#are useful for a variety of of different reasons. They make it so that your code
#is able to updated and maintained by other programmers, they keep the code readable
#by breaking code into smaller chunks and they increase security by hiding the data that
#is being worked with from the main function that is running. Many programs will use a 
#separate file for each function. This makes it so that code segments are included only 
#when they're needed. In Python, we would include a function from another file with the 
#import keyword.
def Printbalance(): 
  #format all variables to $0.00 format and output in a one-line string
  #use modern (current Python suggested) method of formating: 
  #print("{:.2f}".format(var))
  #can also use print("{0:.2f}".format(var)) but this method works better with
  #multiple variables
  print("{:.2f}".format(account_balance))
  #end printbalance()

#The Deposit() function calls for two parameters. A parameter is a piece of information
#that is passed into the function so that the function is able to use it without having 
#to create the variable from scratch. This makes it so that the same piece of information
#can be used through many different functions. This capability makes it so that you can 
#optimize your memory usage by manipulating the same segment of data. 
def Deposit(deposit_amount, account_balance):
  #add the deposited amount to the account balance and show the output
  account_balance += float(deposit_amount)
  print("Deposit was $",end="")
  print("{:.2f}".format(deposit_amount), end="")
  print(", current balance is $",end="")
  print("{:.2f}".format(account_balance))
  #end deposit()

#These functions don't have return statements. This is because they do their user output
#locally within the function. If we were using the information for other logical or 
#mathematical computations, we would send the results of our function back to the main
#function, or whatever custom function called it so that the result could be used in
#another calculation. We send information back to the calling function with the return
#keyword.
def Withdrawl(withdrawl_amount, account_balance):
  if withdrawl_amount > account_balance: #not enough money in the bank
    #show overdraw output
    print("${:.2f}".format(withdrawl_amount), end="")
    print(" is greater than your account balance of $", end="")
    print("{:.2f}".format(account_balance))
  elif withdrawl_amount <= account_balance:
    #adjust the balance and show the output
    account_balance -= float(withdrawl_amount)
    print("Withdrawal amount was $", end="")
    print("{:.2f}".format(withdrawl_amount), end="")
    print(", current balance is $", end="")
    print("{:.2f}".format(account_balance))
  #end withdrawl()
def Quit():
  print("Thank you for banking with us.")
  #end quit()
#start main script
#add a welcome message that displays the input options
#the welcome message would have caused Codio to fail 

#print() is a built-in function of Python. It's an essential part of the language
#and because it's a part of the language, we don't need to make a custom function 
#to be able to use it.
print("Welcome to SNHU-Bank.\nYour banking options are (B)alance Inquiry, (D)eposit, (W)ithdrawl and (Q)uit\n")
#get user input and do the associated function
userchoice = input("What would you like to do?\n")
if (userchoice.upper() == 'D'):
  amtDeposit = float(input("How much would you like to deposit today?\n"))
  Deposit(amtDeposit,account_balance)
elif (userchoice.upper() == 'W'):
  amtWithdrawl = float(input("How much would you like to withdraw today?\n"))
  Withdrawl(amtWithdrawl, account_balance)
elif (userchoice.upper() == 'B'):
  Printbalance()
elif (userchoice.upper() == 'Q'):
  Quit()

#Reflections:
#I didn't have any issues with this assignment. I did use the parameters of print()
#differently to make sure that there was no possibility for the Python interpreter 
#to print formatted variables incorrectly. I've worked with functions in the past
#with other languages and they're essentially the same regardless of language.
#There are only a few minor differences between them with different languages in 
#their declaration. The following is an example of the differences in function
#declaration in three languages: (Note that comments will be shown within the examples
#and they will be marked approprietly for the language that the example is in.)
#
#Python:
#def FunctionName(parameter1,parameter2):
#    bodyCode
#    #return statement is optional
#
#PHP:
#function FunctionName($parameter1,$parameter2)
#{
#    bodyCode;
#    // return statement is optional
#}
#
#C++:
#void FunctionName(int parameter1, int parameter2) //Parameters must have a data type assigned to them, just like normal variables
#{
#    bodyCode;
#    /* return data must match the data type that is declared before the 
#    function's name. If there is no return data, use return type void as 
#    shown in this example */
#}