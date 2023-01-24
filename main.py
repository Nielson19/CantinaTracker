# this is the main structure of the app to keep track of the meals paid in the week
# keeping track of who ordered the food
import time

memberID = 0
MDatabase = {}
# MDatabase = {'Member#1': {'first_Name': 'Daniel', 'last_Name': 'Escobar', 'phone_Num': '9542402809',
#                           'email': 'danielescobar492@gmail.com', 'date_Purchased': 'Monday, January 23, 07:14', 'id': 1},
#              'Member#2': {'first_Name': 'Ana', 'last_Name': 'Abinazar', 'phone_Num': '33333', 'email': 'asdasdf333',
#                           'date_Purchased': 'Monday, January 23, 07:14', 'id': 2}}


def addMember(MDatabaseNew, NewMemberID):
    member = {
        'first_Name': ' ',
        'last_Name': ' ',
        'phone_Num': 0,
        'email': ' ',
        'date_Purchased': time.strftime("%A, %B " + str("%d") + ", %I:%M")
    }

    valid_characters = "yn"
    # create input validation for each input
    print("Please complete the following form")
    member['first_Name'] = input("First Name: ")
    member['last_Name'] = input("Last Name: ")
    member['phone_Num'] = input("Phone Number: ")
    member['email'] = input("email: ")
    member['id'] = NewMemberID

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
        addMember(MDatabaseNew, NewMemberID - 1)


def displayList(MDataBaseDisplay, DisplayMemberID):
    print(("First Name" + "\t" + "Last Name" + "\t" + "Phone Number" + "\t" + "Email" + "\t" + "ID #"+ "\t" + "Date Purchased").expandtabs(30))
    for member in MDataBaseDisplay:
        print((MDataBaseDisplay[str(member)]['first_Name'] + "\t" +
              MDataBaseDisplay[str(member)]['last_Name'] + "\t" +
              str(MDataBaseDisplay[str(member)]['phone_Num']) + "\t" +
              MDataBaseDisplay[str(member)]['email'] + "\t" +
              str(MDataBaseDisplay[str(member)]['id']).zfill(6) + "\t" + MDataBaseDisplay[str(member)]['date_Purchased']).expandtabs(30)
              )

    main(DisplayMemberID)


def main(MainMemberID):
    valid_characters = "abc"
    while True:
        print("Welcome to the Cantina Tracker App")
        print("Main Menu\n"
              "\t a. Add Member\n"
              "\t b. Display Calendar\n"
              "\t c. Display Member List\n")

        selection = input("Please Select Option: ").lower()

        # data validation

        if all(char in valid_characters for char in selection):
            break
    print("option selected: " + selection)
    if selection == 'a':
        MainMemberID += 1
        addMember(MDatabase, MainMemberID)
        main(MainMemberID)
    # elif selection == 'b':
    #
    elif selection == 'c':
        displayList(MDatabase, MainMemberID)
    # else:
    #


main(memberID)

# display calendar
# interactive week calendar to check mark delivered food
#  go to previous week calendars  (automatically display the correct week depending on the day today)

# display member list
# edit member
# change form information
# cancel member
