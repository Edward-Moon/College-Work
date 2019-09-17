#IT-140: Introduction to Scripting
#Assignment: Project 2 Final
#Instructor: Zoe Likoudis

#Make the dictionary and the list, but don't put anything in them yet
grocery_item = {} #this could be a dictionary or a set. It'll be a dictionary for this script
grocery_history = [] #Using a list makes it so that we can add or remove elements. A tuple would be used if it was static.
#tempitem = {} commented declaration for later use in showing update()

stop = 'go'
while stop == 'go': #use a while loop here because we don't know how many items are needed to be added to our list
    #get user input
    item_name = input("Item name:\n")
    quantity = int(input("Quantity purchased:\n"))
    cost = float(input("Price per item:\n"))
    #The update method is useful for combining dictionaries. The process for doing this is shown below.
    #This method isn't necessary for this program, so it's been commented
    #tempitem = {'name':item_name, 'number':quantity, 'price':cost}
    #grocery_item.update(tempitem)
    #Make the dictionary an item in the list
    #The list has items, but the items have names, quantities and prices
    #This could be done with just a list, but having a list of dictionary items makes it a lot easier
    grocery_history.append({'name':item_name,'number':int(quantity),'price':float(cost)})
    #Is the user done adding items?
    keepGoing = input("Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n")
    if keepGoing.upper() == 'Q':
        stop = 'stop' #loop control
grand_total = 0.00
#Now determine how much each item in a list is along with the combined cost for everything
for i in range(0,len(grocery_history),1): #We only need to iterate as many times as there are items in our list
  #get the total cost for the individual item, then add it to grand total
  item_total = grocery_history[i]['price']*grocery_history[i]['number']
  grand_total += item_total
  #create the output to be shown to the user for the individual item
  outputString = str(grocery_history[i]['number']) + " " + grocery_history[i]['name'] + " @ " + str(grocery_history[i]['price']) + " ea $" + str(item_total)
  print(outputString)
  #reset the total for individual items
  item_total = 0
#show the cost for everything in the grocery list
print("Grand total: $%.2f" % grand_total)

#REFLECTIONS:
# I really didn't have any problems with getting this program to work. I had some small 
# syntax errors, like a missing ) or :, but I didn't have any logical problems with
# writing this script. The problem was straight-forward:
#   1: Make an empty list
#   2: Make an empty dictionary
#   3: Get user input for each element in the dictionary
#   4: Add a new element to the list that is the dictionary
#   5: Multiply the price and the quantity to get the total for the list's element
#   6: Add the total cost for each element in the list to get the cost for everything
#   7: Show the output
#
# If anything gave me trouble, it was inserting the dictionary into the list. Python
# doesn't allow you to insert assign a list element to a dictionary directly, as in
# theList[i]=theDict, so I ended up appending the dictionary elements into the list. 
# It was a little bit of a work-around, but in the end it worked.