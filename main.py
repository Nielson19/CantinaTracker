# this is the main structure of the app to keep track of the meals paid in the week
# keeping track of who ordered the food
import time


# MDatabase = {}
MDatabase = {'Member#1': {'first_Name': 'Daniel', 'last_Name': 'Escobar', 'phone_Num': '9542402809',
                          'email': 'danielescobar492@gmail.com', 'date_Purchased': 'Monday, January 23, 07:14', 'id': 1, 'meals_collected': []},
             'Member#2': {'first_Name': 'Ana', 'last_Name': 'Abinazar', 'phone_Num': '9542494584', 'email': 'asdasdf333',
                          'date_Purchased': 'Monday, January 23, 07:14', 'id': 2, 'meals_collected': []}}
memberID = 0

def collectMeal(DatabaseCollect, memberCollect):
    # search for the member
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekSelection = []
    valid_characters = "yn"
    searchWord = input("Please type Phone Number: ")
    for member in DatabaseCollect:
        if DatabaseCollect[str(member)]['phone_Num'] == searchWord:
            print("Result: " + DatabaseCollect[str(member)]['first_Name'] + ' ' + DatabaseCollect[str(member)]['last_Name'])
            todaySelection = input("is picking up today only?(y/n)").lower()
            if todaySelection == 'n':
                weekSelection = x = list(map(str, input("Enter Days: ").split()))
                for day in weekSelection:
                    sameWeekDay = False
                    for memberDay in DatabaseCollect[str(member)]['meals_collected']:
                        if memberDay == day:
                            sameWeekDay = True
                            break
                    if not sameWeekDay:
                        DatabaseCollect[str(member)]['meals_collected'].append(day)
            elif todaySelection == 'y':
                weekSelection = time.strftime("%A")
            print("Record of week: " + str(DatabaseCollect[str(member)]['meals_collected']))
            main(memberCollect)
        else:
            print("No Record Found")
            main(memberCollect)
        # print(weekSelection)



    # plot for the option to select a

def addMember(MDatabaseNew, NewMemberID):
    member = {}

    valid_characters = "yn"
    # create input validation for each input
    print("Please complete the following form")
    member['first_Name'] = input("First Name: ")
    member['last_Name'] = input("Last Name: ")
    member['phone_Num'] = input("Phone Number: ")
    member['email'] = input("email: ")
    member['date_Purchased'] = time.strftime("%A, %B " + str("%d") + ", %I:%M")
    member['id'] = NewMemberID
    member['meals_collected'] = []

    while True:
        print("please confirm the information below")
        print("Member ID: " + str(NewMemberID))
        print("First Name: " + member['first_Name'])
        print("Last Name: " + member['last_Name'])
        print("Phone Number: " + member['phone_Num'])
        print("Email: " + member['email'])
        print("Date Purchased: " + member['date_Purchased'])

        confirmation = input("is this correct?(y/n): ").lower()
        if all(char in valid_characters for char in confirmation):
            break

    if confirmation == "y":
        print("Printing...")
        MDatabaseNew["Member#" + str(NewMemberID)] = member
        return NewMemberID

    elif confirmation == "n":
        addMember(MDatabaseNew, NewMemberID)

def cantinaRecords(MDataBaseRecord, memberIDRecord):
    print(("Name" + "\t" + "Monday" + "\t" + "Tuesday" + "\t" + "Wednesday" + "\t" + "Thrusday" + "\t" + "Friday").expandtabs(30))
    for member in MDataBaseRecord:
        calendarName = MDataBaseRecord[str(member)]['first_Name'] + ' ' + MDataBaseRecord[str(member)]["last_Name"]
        print(calendarName.expandtabs(30))
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main(memberIDRecord)

def displayList(MDataBaseDisplay, DisplayMemberID):
    print(("First Name" + "\t" + "Last Name" + "\t" + "Phone Number" + "\t" + "Email" + "\t" + "ID #"+ "\t" + "Date Purchased" + "\t" + "Meals Collected").expandtabs(30))
    for member in MDataBaseDisplay:
        print((MDataBaseDisplay[str(member)]['first_Name'] + "\t" +
              MDataBaseDisplay[str(member)]['last_Name'] + "\t" +
              str(MDataBaseDisplay[str(member)]['phone_Num']) + "\t" +
              MDataBaseDisplay[str(member)]['email'] + "\t" +
              str(MDataBaseDisplay[str(member)]['id']).zfill(6) + "\t" +
               MDataBaseDisplay[str(member)]['date_Purchased'] + "\t" +
               str(len(MDataBaseDisplay[str(member)]['meals_collected']))).expandtabs(30))
    main(DisplayMemberID)

def main(MainMemberID):
    valid_characters = "abcd"
    while True:
        print("Welcome to the Cantina Tracker App")
        print("Main Menu\n"
              "\t a. Add Member\n"
              "\t b. Display Records\n"
              "\t c. Display Member List\n"
              "\t d. Collect Meal")

        selection = input("Please Select Option: ").lower()

        # data validation

        if all(char in valid_characters for char in selection):
            break
    print("option selected: " + selection)
    if selection == 'a':
        MainMemberID = len(MDatabase) + 1
        addMember(MDatabase, MainMemberID)
        main(MainMemberID)
    elif selection == 'b':
        cantinaRecords(MDatabase, MainMemberID)
    elif selection == 'c':
        displayList(MDatabase, MainMemberID)
    elif selection == 'd':
        collectMeal(MDatabase, MainMemberID)



main(memberID)

# display calendar
# interactive week calendar to check mark delivered food
#  go to previous week calendars  (automatically display the correct week depending on the day today)

# display member list
# edit member
# change form information
# cancel member
