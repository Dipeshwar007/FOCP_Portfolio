

# python 3 program to simulate a online chat of The University of Poppleton


# Important modules imported
import re
import random

# regex variable is made to check the validity of email that user inputed
regex = '^.*@pop.ac.uk$'


# Heading
print('''\nWelcome to Pop Chat
One of our operators will be pleased to help you today.\n''')

# Email taken from user 
user_email = input("Please enter your Poppleton email address: ")

# email_checking function is made 
def email_checking(user_email):

    # two global variable is defined and boolean vale is set 
    global valid
    valid = False

    global count
    count = 0


    # email checking and user name extraction    
    for name_charachter in user_email:
        count += 1
        if name_charachter == "@":
            count -= 1
            break
    
    if count > 2 :
        if (re.search(regex, user_email)):
            valid = True
        else:
            print("Invalid Email ID")
            exit()
    else:
        exit()

# Email finction is called and parameter ia passed
email_checking(user_email)


# operators name list is defined
operator_list = ["Shubhash","Arogya","Sajaha","Dipeshwar","Siri","Saphal","MJ"]

# Network error probablity list is defined
probablity_list = [1,1,1,1,1,0,1,1,1,1]

# From above lists random items value is extracted
random_operator_name = random.choice(operator_list)
random_probablity_network_error = random.choice(probablity_list)

# when email is checked greatings is printed
print("Hi, ",user_email[0:count],"! Thank you, and Welcome to Popchat!")
print("My name is ",random_operator_name,", and it will be my pleasure to help you.")


# When there is network error below code is exicuted
if random_probablity_network_error == 0:
    print("***** NETWORK ERROR *****")
    print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
    exit()



# Chat with user 
while True:
    
    # User requested message is taken 
    user_request = input("---> ")


    # If user input messege is not recognized then list is created to give a random reply
    not_recognized_input = ["Hmmmmm","Tell me more about it","I didn't understand","Can you repeat it please","Oh yes i see"]
    random_reply = random.choice(not_recognized_input)


    # when user asked about wifi
    if "WIFI" in user_request.upper():
        print("Wifi is excelent across the campus.")

    # when user asked about library
    elif "LIBRARY" in user_request.upper():
        print("The library is closed today.")

    # when user asked about deadline
    elif "DEADLINE" in user_request.upper():
        print("Your deadline has been extended by two working days.")

    # when user asked about class
    elif "CLASS" in user_request.upper():
        print("Classes are running today.")

    # when user asked about holiday
    elif "HOLIDAY" in user_request.upper():
        print("No holiday in this week.")
    
    # when user asked about application
    elif "APPLICATION" in user_request.upper():
        print("Please, submit your application in university website.")

    # when user asked about thanks
    elif "THANKS" in user_request.upper():
        print("It's my pleasure to help you.")

    # If above nothing is recognized then below code will check if it should give a random reply or exit the code
    elif ("WIFI" or "LIBRARY" or "DEADLINE" or "CLASS" or "HOLIDAY" or "APPLICATION" or "THANKS") not in  user_request.upper():
        if ("BYE" or "GOODBYE") in user_request.upper():
            print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
            exit()
        elif("HELP") in user_request.upper():
            print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
            exit()
        elif("EXIT") in user_request.upper():
            print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
            exit()
        elif("END") in user_request.upper():
            print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
            exit()
        elif("QUIT") in user_request.upper():
            print("\nThanks, ",user_email[0:count],", for using PopChat. See you again soon!")
            exit()
        else:    
            print(random_reply)
