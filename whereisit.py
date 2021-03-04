import pyinputplus as pyip
quitStr = 'None'

itemFind = {}
def itemList():
  print("Items already listed:")
  for x in itemFind.keys():
    print(x)
# test - list the items in the dictionary
if len(itemFind)>= 1:
  itemList()
else:
# List item -input

  print("You have no items listed! Ready to add them.")
  while True:
    print("Enter the item's name - or type NONE to quit.")
    item = input()
    if len(item) < 1 or len(item) > 50:
      print('This item must have a length between 1 and 50 characters.')
    elif item.casefold() == quitStr.casefold():
      itemList()    
      break  
    else:
      print('Please list where the item can be found.')
    find = input()
    
    if len(find) < 1 or len(find) > 50:
      print('The location must have a length between 1 and 50 characters.')
    else:
      newItem = {item:find}
      print(newItem)
      itemFind.update({item:find})
      itemList()
      

# Get item to find
# Return location of item
# Another item?
# Update item location?
# Quit