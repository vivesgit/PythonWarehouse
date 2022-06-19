# Carles Vives Cano
# Advanced Programing in Python Warehouse programme


import os
import fileinput


def menuDisplay():
    '''
    This will be the initial menu that will serve as UI for the user.
    '''
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print('(1) Add New Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(6) Move stock from one to another warehouse')
    print('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    '''
    In the Menu Selection, users can select which operation they want to perform.
    '''
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 6:
        move_from_to()
    elif CHOICE == 99:
        exit()

def addInventory():
    '''
    This function adds new items to the selected warehouse.
    '''
    CHOICE = int(input('Enter warehouse 1 or 2: '))

    # Using if conditionals to asess the right warehouse.
    if CHOICE == 1:
        WarehouseFile = open('Warehouse1.txt', 'a')
    elif CHOICE == 2:
        WarehouseFile = open('Warehouse2.txt', 'a')
    else:
        print('That option is not available')
        addInventory()

    print("Adding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ")
    item_quantity = input("Enter the quantity of the item: ")
    WarehouseFile.write(item_description + '\n') # Here write to the warehouse DB the name of the item
    WarehouseFile.write(item_quantity + '\n') # Here write to the warehouse DB the quantity of the item
    WarehouseFile.close()
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def removeInventory():
    '''
    This function removes items from the selected warehouse.
    '''
    CHOICE = int(input('Enter warehouse 1 or 2: '))

    # Using if conditionals to asess the right warehouse.
    if CHOICE == 1:
        WarehouseFile = fileinput.input('Warehouse1.txt', inplace=True)
    elif CHOICE == 2:
        WarehouseFile = fileinput.input('Warehouse2.txt', inplace=True)
    else:
        print('That option is not available')
        removeInventory()

    print("Removing Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ")

    # The following for loop finds the item from the preselected warehouse and removes it.
    for line in WarehouseFile:
        if item_description in line:
            for i in range(1):
                next(WarehouseFile, None)
        else:
            print(line.strip('\n'), end='\n')
    item_description

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    '''
    This function updates existing items from the selected warehouse.
    '''
    CHOICE = int(input('Enter warehouse 1 or 2: '))

    # Using if conditionals to asess the right warehouse.
    if CHOICE == 1:
        WarehouseSelec = 'Warehouse1.txt'
    elif CHOICE == 2:
        WarehouseSelec = 'Warehouse2.txt'
    else:
        print('That option is not available')
        updateInventory()
    
    print("Updating Inventory")
    print("==================")
    item_description = input('Enter the item to update: ')
    item_quantity = int(input("Enter the updated quantity. Enter - for less: "))

    # Using fileinput module to read the DB.
    with open(WarehouseSelec, 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open(WarehouseSelec, 'r')
    file = f.read().split('\n')
    # The following for loop will find the item and change the quantity.
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                if change<0: # If the remaining stock is less than 0 warn the user and cancel the operation.
                    print('You cannot have less than 0 items!')
                    updateInventory()
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open(WarehouseSelec, 'w') as f: # Write and modify the DB.
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def move_from_to():
    '''
    This function moves stock from one warehouse to the other.
    '''
    print('Moving Stock')
    print('===================')
    CHOICE = int(input('Select warehouse of origin (1 or 2): '))

    # Using if conditionals to asess the right warehouse.
    if CHOICE == 1:
        origin = 'Warehouse1.txt'
        destination = 'Warehouse2.txt'
    elif CHOICE == 2:
        origin = 'Warehouse2.txt'
        destination = 'Warehouse1.txt'
    else:
        print('That option is not available')
        move_from_to()

    item_description = input('Enter the item to move: ')
    item_quantity = int(input("Enter the quantity to move. Enter - for less: "))

    # Reading the origin DB.
    with open(origin, 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open(origin, 'r')
    file = f.read().split('\n')
    # Here we substract the defined quantity from the original warehouse.
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value - (item_quantity)
                if change<0: # If the warehouse of origin is left with less than 0 in stock, abort.
                    print('Not enough stock to move!')
                    move_from_to()
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    # Updating the warehouse of origin.
    with open(origin, 'w') as f:
        for line in filedata:
            f.write(line)
    
    # Reading the warehouse of destination.
    with open(destination, 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open(destination, 'r')
    file = f.read().split('\n')
    # In the following for loop we add the defined quantity to the warehouse of destination.
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    # Modifying the warehouse of destination.
    with open(destination, 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()



def searchInventory():
    '''
    This function searches for the specified stock from both warehouses.
    '''
    print('Searching Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ')
    
    # Opening and reading warehouse 1.
    f = open('Warehouse1.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Warehouse 1: ')
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
    
    # Opening and reading warehouse 2.
    f = open('Warehouse2.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Warehouse 2: ')
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
        
        
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def printInventory():
    '''
    This function prints the entire inventory from the selected warehouse.
    '''
    CHOICE = int(input('Enter warehouse 1 or 2: '))

    # Using if conditionals to asess the right warehouse.
    if CHOICE == 1:
        WarehouseFile = open('Warehouse1.txt', 'r')
    elif CHOICE == 2:
        WarehouseFile = open('Warehouse2.txt', 'r')
    else:
        print('That option is not available')
        printInventory()

    # Adjusting visually the results.
    item_description = WarehouseFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = WarehouseFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = WarehouseFile.readline()
    WarehouseFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()


menuDisplay()