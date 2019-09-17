#Edward J Moon
#IT-140 Intro to Scripting
#Instructor: Zoe Likoudis
import sys
#get user input for the rentalCode and rentalPeriod
rentalCode=input("(B)udget, (D)aily, or (W)eekly rental?\n")
#Instead of having additional 'if' statements, 
#check two conditions at the same time by using an 'or'
#condition.
if(rentalCode.upper() == "B" or rentalCode.upper() == "D"):
  #Using variables in our programs gives us the opportunity to have 
  #the same segements of code that can have different results. First
  #we need to get input from our user to see how long a car has been
  #rented.
  rentalPeriod = int(input("Number of Days Rented:\n"))
elif(rentalCode.upper() == "W"):#Don't assume weekly if improper input.
#Else statements are good if there are no other options
#that the program will accept. This script does not loop 
#to confirm the input, so use elif to make sure that the input
#is right.
  rentalPeriod = int(input("Number of Weeks Rented:\n"))
#determine the priceplan for the type of rental
if(rentalCode.upper() == "B"):
  budget_charge = 40.00
elif(rentalCode.upper() == "D"):
  #we have more than two options that we can take with our rentalCode
  #We'll have to have a different branch of our condition for each option.
  daily_charge  = 60.00
elif(rentalCode.upper() == "W"): 
  weekly_charge = 190.00
#baseCharge is determined by rentalCode
#baseCharge is a float and rentalPeriod is an interger
#multiplying these together results in a float, which is
#what our final price will be displayed as.
if(rentalCode.upper() == "B"):
  baseCharge = budget_charge * rentalPeriod
elif(rentalCode.upper() == "D"):
  baseCharge = daily_charge * rentalPeriod
elif(rentalCode.upper() == "W"): 
  baseCharge = weekly_charge * rentalPeriod
#get user input for starting and ending odometer values

#Strings are a good data type to use here because they can be converted
#into other types when they are needed later. Strings are also the
#default input type for Python. Type conversions will be shown in the
#totalMiles computation.
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart)
#calculate the charge for milage
if(rentalCode.upper() == "B"): #budget gets charged for every mile driven
  mileCharge = 0.25 * totalMiles
elif(rentalCode.upper() == "D"): #daily gets a 100 mile allowance on the average for days rented
  averageDayMiles = totalMiles/rentalPeriod
  if(averageDayMiles > 100):
    extraMiles = averageDayMiles - 100
    mileCharge = 0.25 * extraMiles
elif(rentalCode.upper() == "W"): #weekly gets a 900 mile allowance on the average for each week rented
  averageWeekMiles = totalMiles/rentalPeriod
  if(averageWeekMiles > 900):
    extraMiles = averageWeekMiles - 900
    mileCharge = 100.00 * rentalPeriod
#our charges are already floats, so there's no need to convert. Just add them up
amountDue = baseCharge + mileCharge
#Print the summary
print("Rental Summary")
print("Rental Code: ", rentalCode)
print("Rental Period: ", rentalPeriod)
print("Starting Odometer: ", odoStart)
print("Ending Odometer: ", odoEnd)
print("Miles Driven: ", totalMiles)
#amountDue is a float. We need the float to be in normal pricing (rounded to hundredths) format.
#We will use %.2f to determine the number format here. %.2f is good for when you have a single variable.
#If we had more than one variable to outout, we would use the more modern print("{:.2f}".format(var))
#method of formating.
print("Amount Due: $%.2f" %amountDue)