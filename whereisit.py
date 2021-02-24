import pyinputplus as pyip

itemFind = {}
if len(itemFind)>= 1:
  print("Items already listed:")
  for x in itemFind.keys():
    print(x)
else:
  print("You have no items listed! Ready to add them.")
  while True:
    print("Enter the item's name - it must be unique")
    item = input()
    try
      if len(item) < 1 or len(item) > 50:
        print('This item must have a length between 1 and 50 characters.')
      else
      print('Please list where the item can be found. This alos must be unique.')
      find = input()
      try
      if len(find) < 1 or len(find) > 50:
        print('The location must have a length between 1 and 50 characters.')
# List item -input new ones?
# test - list the items in the dictionary
# Get item to find
# Return location of item
# Another item?
# Update item location?
# Quit