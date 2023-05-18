# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KSavard, 5.15.23, added code to complete assignment 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
objFile = None

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(',')  # each position would be a single letter if not for split
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
    print(dicRow["Task"] + ', ' + dicRow["Priority"]) # not including this, but keeping code for reference
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        objFile = open(strFile, "r")
        for Row in lstTable:
            #strData = row.split(',')  # each position would be a single letter if not for split
            print(Row["Task"]+ ", " + Row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a To-Do Task: ")  # defined UserTask as variable for list items
        strPriority = input("Enter priority level: ")  #defined UserPriority as variable for priority
        dicRow ={"Task": strTask, "Priority": strPriority}
        lstTable += [dicRow]
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        DelItem = input("Enter the task you want to remove: ")
        for Row in lstTable:
            if Row["Task"].lower() == DelItem.lower():
                lstTable.remove(Row)
                print(DelItem + " removed")
            else:
                print("entry not found")  # how do i get this to not print after checking each row?
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("list saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("bye!")
        break  # and Exit the program
