

# Python 3 program to analysed the speed of Swallow birds


# Heading printed
print("\nSwallow Speed Analysis: Version 1.0 \n")

# Import mean
from statistics import mean

# File opened
file_opened = open('/Users/dipeshwarshah/Desktop/Test/Component_2_Task_2/Bird-speed-data.txt','r')

# Request Message And Request Counter
request_data_message = "Enter The Reading :"

# Counter is made to count the data
request_count = 0

# Error counter is made to count error data
error_data = 0

# Function Defined For Data Validation
def checking_user_entered_data(user_input):

    '''Function for cheking the data criteria. Does it match with U23 or E23 types of data.'''

    # Global Variable is defined
    global error_data

    # Exception handeling is done
    try:

        # Data Sliced And Given For Checking Process
        first_format_slice = user_input[0].upper()
        second_format_slice = user_input[1:]

        # Set The Boolean Values
        has_U = has_E = False
        has_alphabet = True 

        # Check U At First Of Data    
        if first_format_slice == "U":
            has_U = True
        # Check E At First Of Data
        if first_format_slice == "E":
            has_E = True

        # Check Data Containing Any Alphabet Or Not
        for numeric_vlue in second_format_slice:
            if numeric_vlue.isalpha():
                has_alphabet = False
                break
        
        # Checked Value and Summarise in boolean
        if has_U == True and has_alphabet == True:
            data_file = open('/Users/dipeshwarshah/Desktop/Test/Component_2_Task_2/Bird-speed-data.txt','a')
            data_file.write(user_input + '\n')
            print("Reading Saved")
            data_file.close()
        elif has_E == True and has_alphabet == True:
            data_file = open('/Users/dipeshwarshah/Desktop/Test/Component_2_Task_2/Bird-speed-data.txt','a')
            data_file.write(user_input + '\n')
            print("Reading Saved")
            data_file.close()
        else:
            print("The data type not match.") # error data timeout
            error_data += 1          

    except Exception as e:
        # print("No readings entered. Nothing to do.")
        exit()


# Function defined to read and convert data
def data_manupulate(reading_data):
    '''Function for reading data and convert to the format.'''

    # Differend variable is  defined
    count = 0          # To count the number of data
    sum_in_KMPH = 0    # Sum clculated in kilometer per hour as KMPH
    sum_in_MPH = 0     # Sum clculated in Mile per hour as MPH

    kmph = []           # kmph list is defined to append data converted to kmph
    mph = []            # mph list is defined to append data converted to mph
    Mean_value = []

    # For loop to convert every data to its suitable format
    for data in reading_data:
        count += 1

        if data[0].upper()=="U":
            converted_speed_in_KMPH = int(float(data[1:-1])) # all values of E in kmph format
            kmph.append(converted_speed_in_KMPH)
            sum_in_MPH += converted_speed_in_KMPH
            Mean_value.append(converted_speed_in_KMPH)
        else:
            converted_speed_in_MPH = int(float(data[1:-1]))/1.61 # all values of U in mph format
            mph.append(converted_speed_in_MPH)
            sum_in_KMPH += converted_speed_in_MPH
            Mean_value.append(converted_speed_in_MPH)
    
    # For loop to convert every kilometer per hour data in to mile per hour
    for data in kmph:
        all_in_mile_pher_hour = data / 1.61
        mph.append(all_in_mile_pher_hour)


    max_speed = max(mph)    # Maximum speed in mile per hour
    min_speed = min(kmph)    # Minimum speed in mile per hour


    max_speed_kmph = max(mph)*1.61      # Maximum speed in kilometer per hour
    min_speed_kmph = min(kmph)*1.61           # Minimun speed in kilometer per hour

    # Maximum in kmph and mph an vise versa is printed
    print("Max Speed: ",f"{max_speed:.2f}","MPH,",f"{max_speed_kmph:.2f}","KPH.")
    print("Min Speed: ",f"{min_speed:.2f}","MPH,",f"{min_speed_kmph:.2f}","KPH.")


    # The average Finding mechanism
    kmph_sum_to_mph = sum_in_KMPH / 1.61           # kmph sum is converted to mph sum
    Main_sum = sum_in_MPH + kmph_sum_to_mph        # Total sum is calculated
    average_value_of_all_data = mean(Mean_value)   # Average of total is calculated in mph

    print("Avg Speed: ",f"{(average_value_of_all_data):.2f}","MPH,",f"{(average_value_of_all_data)*1.61:.2f}","KPH.")
    
    return (' ') # To return Nothing at last and comeover none output

# Loop To Enter The Values
while True:

    # Input Taken
    user_input = input(request_data_message)

    # Only U and E error has overcomed
    if user_input.upper() == "U":
        print("Only",user_input,"is invalid")
        exit()
    elif user_input.upper() == "E":
        print("Only",user_input,"is invalid")
        exit()

    # When input is nothing
    if user_input =="" and request_count == 0:
        print("No readings entered. Nothing to do.")
        exit()

    # When input is empty
    if user_input == '':
        request_count -= 1
    
    # Request Generated and result taken out
    
    # Request counter is increased
    request_count += 1

    # When the user enterd value is more than one then enter reading is changed
    if request_count == 1:
        request_data_message = request_data_message[:9] + " Next" + request_data_message[9:]

    # If the user input is empty after the first input 
    if request_count >= 1 and user_input == '':
        print("\n\nResult Summary\n")

        # function to give the exact good data is given to the program                  
        def error_subtraction():
            return error_data
        error_subtraction()

        # When there is only one data entered and more than one
        if request_count == 1:
            print(request_count,"Reading Analysed\n")
        else:
            request_count = request_count - error_data              # Actual good data is calculated
            print(request_count,"Readings Analysed\n")

        # calaulated data is printed
        print(data_manupulate(file_opened))

        # Bird-speed-data.txt file is opened in both read and write mode
        f = open('/Users/dipeshwarshah/Desktop/Test/Component_2_Task_2/Bird-speed-data.txt', 'r+')

        # All data of the file is cleared
        f.truncate(0)


    # Checking Function Used
    checking_user_entered_data(user_input)


# To print the actual good readings analysed
print(request_count,"Readings Analysed.")