import random #random used to randomize names
#classList = ['Andrew', 'Chris', 'Aidan', 'Ben', 'Liam', 'Brandon', 'Jessie', 'Emma', 'Matt', 'Robert', 'Bobby', 'Brian', 'Alane', 'Anne', 'Evan', 'Eric', 'Jeanette', 'Lucas', 'Spencer', 'Graham']
classList = [] #insert class list here
group = int(input("Type 2 for groups of 2, 3 for groups of 3 and 4, and 4 for groups of 4: ")) #input for group numbers
# read exceptions and normalize casing so they match names in classList
while group not in (2, 3, 4): #if the input is invlaid
    print("Invalid input for group size. Please try again")
    group = int(input("Type 2 for groups of 2, 3 for groups of 3 and 4, and 4 for groups of 4: ")) #asks for input again
excep = int(input("Type 1 for no exceptions, 2 for an exception: ")) #input for exceptions
while excep not in (1, 2): # if the input is invalid
  print("Invalid input for exceptions. Try Again") #prints the input is invalid
  excep = int(input("Type 1 for no exceptions, 2 for an exception: ")) #asks for input again
if excep == 2:
  exception1 = input("Input first exception: ").strip().title() #input for exceptions
  exception2 = input("Input second exception: ").strip().title() #input for exceptions
  group1 = []#creating groups 1-10 with exceptions in the correct groups
  group2 = []
  group3 = []
  if group == 3: #if it is groups of 3 and 4 put the exceptions in group 5 and 6
    group4 = []
    group5 = [exception1]
    group6 = [exception2]
  if group == 4: #if it is groups of 4 put the exceptions in group 4 and 5
    group4 = [exception1]
    group5 = [exception2]
    group6 = []
  group7 = []
  group8 = []
  group9 = []
  group10 = []
  if group == 2: # if it is groups of 2 put the exceptions in group 9 and 10
    group4 = []
    group5 = []
    group6 = []
    group9 = [exception1]
    group10 = [exception2]
  #takes the exception input and checks if name is in list
  for exc in (exception1, exception2): 
    if exc in classList: #if name is in list remove it
        classList.remove(exc)
    else:
        # warn the user in case of a typo or unknown name
        print(f"Warning: '{exc}' not found in class list")
if excep == 1: #if there are no exceptions create groups 1-10 empty
  group1 = []
  group2 = []
  group3 = []
  group4 = []
  group5 = []
  group6 = []
  group7 = []
  group8 = []
  group9 = []
  group10 = []
groupNumber = 1 #starts group number at 1
randomPick = [] #creates the random pick variable
while len(classList) > 0 and group == 3: #if it is groups of 3 and 4 adds people to groups 1-6 until class list is empty
  randomPick = random.choice(classList)
  if groupNumber == 1:
    group1.append(randomPick)
  if groupNumber == 2:
    group2.append(randomPick)
  if groupNumber == 3:
    group3.append(randomPick)
  if groupNumber == 4:
    group4.append(randomPick)
  if groupNumber == 5:
    group5.append(randomPick)
  if groupNumber == 6:
    group6.append(randomPick)
  classList.remove(randomPick)
  groupNumber = groupNumber + 1
  if groupNumber == 7:
    groupNumber = 1
if group == 3: #prints the groups if it is groups of 3 and 4
  print("Group 1: ", group1)
  print("Group 2: ", group2)
  print("Group 3: ", group3)
  print("Group 4: ", group4)
  print("Group 5: ", group5)
  print("Group 6: ", group6)
while len(classList) > 0 and group == 2: #if it is groups of 2 adds people to groups 1-10 until class list is empty
  randomPick = random.choice(classList)
  if groupNumber == 1:
    group1.append(randomPick)
  if groupNumber == 2:
    group2.append(randomPick)
  if groupNumber == 3:
    group3.append(randomPick)
  if groupNumber == 4:
    group4.append(randomPick)
  if groupNumber == 5:
    group5.append(randomPick)
  if groupNumber == 6:
    group6.append(randomPick)
  if groupNumber == 7:
    group7.append(randomPick)
  if groupNumber == 8:
    group8.append(randomPick)
  if groupNumber == 9:
    group9.append(randomPick)
  if groupNumber == 10:
    group10.append(randomPick)
  classList.remove(randomPick)
  groupNumber = groupNumber + 1
  if groupNumber == 11:
    groupNumber = 1
if group == 2: #prints the groups if it is groups of 2
  print("Group 1: ", group1)
  print("Group 2: ", group2)
  print("Group 3: ", group3)
  print("Group 4: ", group4)
  print("Group 5: ", group5)
  print("Group 6: ", group6)
  print("Group 7: ", group7)
  print("Group 8: ", group8)
  print("Group 9: ", group9)
  print("Group 10: ", group10)
while len(classList) > 0 and group == 4: #if it is groups of 4 adds people to groups 1-5 until class list is empty
  randomPick = random.choice(classList)
  if groupNumber == 1:
    group1.append(randomPick)
  if groupNumber == 2:
    group2.append(randomPick)
  if groupNumber == 3:
    group3.append(randomPick)
  if groupNumber == 4:
    group4.append(randomPick)
  if groupNumber == 5:
    group5.append(randomPick)
  classList.remove(randomPick)
  groupNumber = groupNumber + 1
  if groupNumber == 6:
    groupNumber = 1
if group == 4: #prints the groups if it is groups of 4
  print("Group 1: ", group1)
  print("Group 2: ", group2)
  print("Group 3: ", group3)
  print("Group 4: ", group4)
  print("Group 5: ", group5)