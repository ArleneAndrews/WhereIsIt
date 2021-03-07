import pyinputplus as pyip

itemFind = {}

def yesNo():
  answer = input('Any more to list? Yes or No.  ').upper()
  if answer == 'NO' or answer =='N':
    findStuff()
  else:
    addStuff()

def addStuff():
  item = input("Enter the item's name. ")
  if len(item) < 1 or len(item) > 50:
    print('This item must have a length between 1 and 50 characters.')
  else:
    #Get input of where the item is found
    find = input('Please list where the item can be found. ')
  
  if len(find) < 1 or len(find) > 50:
    print('The location must have a length between 1 and 50 characters.')
  else:
    itemFind.update({item:find})
    yesNo()
    

def itemList():
  print("Items already listed:")
  for x in itemFind.keys():
    print(x)

def itemLost(lostItem):
  for key, value in itemFind.keys():
    if lostItem == key:
        return value
    return "This item hasn't been entered."

def findStuff():
  lostItem = ('What are you looking for?  ')
  itemLost(lostItem)
  yesNo()

if len(itemFind)>= 1:
  itemList()
else:
# List item -input
  print("You have no items listed! Ready to add them.")
  addStuff()
  yesNo()
# Get item to find
# Return location of item
# Another item?
# Update item location?
# Quit
