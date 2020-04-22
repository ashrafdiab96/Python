# ATM project
import time                                                   # import time library
import sys
# Users data instead of database
users = [{"name": "Menna", "balance": 1500000, "pinCode": 2707},
         {"name": "Ashraf", "balance": 1000000, "pinCode": 1311},
         {"name": "Ahmed", "balance": 90000, "pinCode": 2806},
         {"name": "Mustafa", "balance": 80000, "pinCode": 1234},
         {"name": "Asmaa", "balance": 1290, "pinCode": 1234},
         {"name": "Ayman", "balance": 1200, "pinCode": 4321},
         {"name": "Adel", "balance": 19000, "pinCode": 3214},
         {"name": "Alaa", "balance": 129000, "pinCode": 2134},
         {"name": "Mahy", "balance": 25000, "pinCode": 2341},]
# charity data
charity = [{"name": "Resala", "balance": 5000000},
           {"name": "MisrElkhair", "balance": 1200000},
           {"name": "LifeMaker", "balance": 900000},
           {"name": "FoodBank", "balance": 800000},
           {"name": "ZakatHouse", "balance": 1800000}]
# user who use the ATM now
currentUser = {}                                              # var to carry the current user
currentPinCode = 0                                            # var to carry the pin code
# loading screen
def loadingScreen():
    for i in range(1, 3):                                     # printing loading
        print("\rloading", "."*i, end="")
        time.sleep(1)                                         # delay 1 second
# initial screen setting
def initialScreen():
    global currentUser                                        # make var global
    global currentPinCode                                     # make var global
    found = False                                             # variable set as true if there is a user
    loadingScreen()                                           # call loading screen on to show start
    print("\r#############################################")
    print("#          Welcome to O-Learning ATM        #")
    print("#          Please, Enter your PinCode:      #")
    currentPinCode = int(input("                     "))
    print("#                                           #")
    print("#                                           #")
    print("#############################################")
    for user in users:                                       # loop on users and get the user depending om pinCode
        if user["pinCode"] == currentPinCode:                # check if correct pinCode
            currentUser = user                               # get current user
            found = True                                     # set found as true
    if found:                                                # check if there is a user
        loadingScreen()                                      # call loading screen
        selectScreen()                                       # call select screen (next screen)
    else:                                                    # if there isn't user
        errorScreen()                                        # call error screen
# screen will show when user enter any correct data
def errorScreen():
    print("\r#############################################")
    print("#                                           #")
    print("#                                           #")
    print("#          pinCode not correct              #")
    print("#                                           #")
    print("#                                           #")
    print("#############################################")
    loadingScreen()
    initialScreen()
# screen will show when user enter his correct pinCode
def selectScreen():
    print("\r#############################################")
    print("#       Welcome to O-Learning ATM           #")
    print("#                 ", currentUser["name"], "                   #")
    print("#                                           #")
    print("# 1- cashWithdrawal      2- balance Inquiry #")
    print("# 3- transfer            4- setting         #")
    print("# 5- billPayment         6- donate          #")
    print("#                7- Exit                    #")
    print("#        Enter required operation           #")
    op = int(input("                    "))
    print("#############################################")
    # check for the operation that user wants to do
    if op == 1:
        loadingScreen()
        cashWithdrawal()
    elif op == 2:
        loadingScreen()
        balanceInquiry()
    elif op == 3:
        loadingScreen()
        transfer()
    elif op == 4:
        loadingScreen()
        setting()
    elif op == 5:
        loadingScreen()
        billPayment()
    elif op == 6:
        loadingScreen()
        donate()
    elif op == 7:
        exitScreen()
    else:
        print("Please enter a valid operation !")
        loadingScreen()
        initialScreen()
# function to allow user take a money
def cashWithdrawal():
    print("\r#############################################")
    print("#                                           #")
    print("#     Enter the amount you want withdraw    #")
    print("#                                           #")
    amount = float(input("                    "))
    # check if current balance allow to complete the operation or not
    if amount <= currentUser["balance"]:
        currentUser["balance"] = currentUser["balance"] - amount
        print("#  The requested amount has been withdrawn  #")
        print("#            our balance is now:            #")
        print("#               ", currentUser["balance"], "                 #")
    else:
        print("#   Your current balance isn't sufficient   #")
    print("#############################################")
    loadingScreen()
    anotherOperation()
# function to show  current balance
def balanceInquiry():
    print("\r#############################################")
    print("#                                           #")
    print("#          Your current balance is:         #")
    print("#                ", currentUser["balance"], "                  #")
    print("#                                           #")
    print("#############################################")
    loadingScreen()
    anotherOperation()
# transfer money to person (we using the name as a key for the second person)
def transfer():
    print("\r#############################################")
    print("#                                           #")
    print("#     Enter the amount you want transfer    #")
    print("#                                           #")
    amount = int(input("                    "))
    # check if current balance allow to complete the operation or not
    if amount <= currentUser["balance"]:
        print("#  Enter name of person you want transfer   #")
        personName = str(input("                    "))
        for user in users:
            if user["name"] == personName:
                user["balance"] = user["balance"] + amount
                currentUser["balance"] = currentUser["balance"] - amount
                print("#  The requested amount has been transfer   #")
                print("#            Your balance is now:           #")
                print("#               ", currentUser["balance"], "                   #")
            else:
                print("#  This customer isn't present in service   #")
                break
    else:
        print("#   Your current balance isn't sufficient   #")
    print("#############################################")
    loadingScreen()
    initialScreen()
# transfer money to pay bill company
def billPayment():
    print("\r#############################################")
    print("#                                           #")
    print("#     Enter the amount you want transfer    #")
    print("#                                           #")
    amount = int(input("                    "))
    # check if current balance allow to complete the operation or not
    if amount <= currentUser["balance"]:
            currentUser["balance"] = currentUser["balance"] - amount
            print("#  The requested amount has been transfer   #")
            print("#            Your balance is now:           #")
            print("#               ", currentUser["balance"], "                   #")
    else:
        print("#   Your current balance isn't sufficient   #")
    print("#############################################")
    loadingScreen()
    anotherOperation()
# set name and pinCode
def setting():
    print("\r#############################################")
    print("#                                           #")
    print("#  Your name:          ", currentUser["name"], "              #")
    print("#  Your pinCode:        ****                #")
    print("#  1- Edit name         2- Edit pinCode     #")
    editOp = int(input("                  "))
    if editOp == 1:
        print("#             Enter new name:               #")
        newName = str(input("                   "))
        currentUser["name"] = newName
    elif editOp == 2:
        print("#            Enter new pinCode:             #")
        newPin = int(input("                   "))
        currentUser["pinCode"] = newPin

    print("#                                           #")
    print("#############################################")
    loadingScreen()
    initialScreen()
# transfer money to charity
def donate():
    print("\r#############################################")
    print("#                                           #")
    print("#     Enter the amount you want transfer    #")
    print("#                                           #")
    amount = int(input("                    "))
    # check if current balance allow to complete the operation or not
    if amount <= currentUser["balance"]:
        print("#  Enter name of charity you want transfer  #")
        chName = str(input("                    "))
        for ch in charity:
            if ch["name"] == chName:
                ch["balance"] = ch["balance"] + amount
                currentUser["balance"] = currentUser["balance"] - amount
                print("#  The requested amount has been transfer   #")
                print("#            Your balance is now:           #")
                print("#               ", currentUser["balance"], "                   #")
    else:
        print("#   Your current balance isn't sufficient   #")
    print("#############################################")
    loadingScreen()
    initialScreen()
# ask user if wants to make another operation
def anotherOperation():
    print("\r#############################################")
    print("#   Do you want to make another operation?  #")
    print("#        1- Yes           2- No             #")
    res = int(input("                   "))
    print("#                                           #")
    print("#                                           #")
    print("#############################################")
    # check user answer
    if res == 1:
        loadingScreen()
        selectScreen()
    elif res == 2:
        loadingScreen()
        exitScreen()
# function show on final of operations
def exitScreen():
    print("\r#############################################")
    print("#                                           #")
    print("#                                           #")
    print("#                Thank you !                #")
    print("#                                           #")
    print("#                                           #")
    print("#############################################")

initialScreen()