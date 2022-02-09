import datetime
dateTime = datetime.datetime.now()
month = dateTime.month
day = dateTime.day
hour = dateTime.hour 
minute = dateTime.minute


#Welocme the user to the Grocery Shoppig APP and show time the shopping is happening. 
print("\n\tWelcome to The Grocery Shopping APP")
print(f"\nCurrent dat and Time: {month}/{day} {hour}:{minute}\n")

#initialise list 
myShoppingList = ["Meat","Cheese"]

#Accept users input into the list
product1 = input("\nEnter a food name to add to your grocery list: ")
product2 = input("Enter a food name to add to your grocery list: ")
product3 = input("Enter a food name to add to your grocery list: ")

#Add users new list to the myShopping List 
myShoppingList.append(product1.title())
myShoppingList.append(product2.title())
myShoppingList.append(product3.title())

#print the new list
print("Here is your Grocery List: ")
print(myShoppingList)

print()

print("sorting your List...")

#sort the list...
myShoppingList.sort()

#Display sorted list to users.
print(f"Your sorted Grocery: {myShoppingList}")

print()

print("Simulating Grocery List...")

#Display the number of Element in the List to the user.
print(f"You have : {len(myShoppingList)} in your Lsit")
print(f"They are {myShoppingList}")

#take what the user bought and remove from the list. 
item = str(input("\nWhat did you just buy? ")).title()
myShoppingList.remove(item)
#Display users item being removed from the lsit 
print(f"Removing {item} from the List... ")
#tell the quantity of current List remaining and show them, remove one item again
print("You have: " + str(len(myShoppingList)) + " items remaining.")
print(myShoppingList)

#take what the user bought and remove from the list again.
item = str(input("\nWhat did you just buy? ")).title()
myShoppingList.remove(item)
#Display users item being removed from the lsit 
print(f"Removing {item} from the List... ")
#tell the quantity of current List remaining and show them, remove one item again
print("You have: " + str(len(myShoppingList)) + " items remaining.")
print(myShoppingList)

#take what the user bought and remove from the list again.
item = str(input("\nWhat did you just buy? ")).title()
myShoppingList.remove(item)
#Display users item being removed from the lsit 
print(f"Removing {item} from the List... ")
#tell the quantity of current List remaining and show them, remove one item again
print("You have: " + str(len(myShoppingList)) + " items remaining.")
print(myShoppingList)

#Tell the user the store is out of an item and should be replaced
print("The store is out of " + str(myShoppingList[1]))
outOFstock = myShoppingList.pop(1)
print(f"The store is out of {outOFstock} replace the item")

print(myShoppingList)
#add a new item to the shopping list




