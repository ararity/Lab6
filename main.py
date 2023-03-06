########################################
#              COP3502C                #
#               Lab 6                  #
#           Encoder/Decoder            #
#       Blake Owen, Braden Azis        #
########################################


# Function to encode password. Each digit is increased by 3. Encoded string is returned.
def encode(p_word):
    code = ''
    for i in range(len(p_word)):    # Loops through each digit of the password

        new_code = int(p_word[i]) + 3   # Digit is encoded

        if new_code <= 9:   # Checks if digit is greater than 9. Wraps back to 0.
            code += str(new_code)
        else:
            code += str(new_code - 10)

    return code

# function to decode password. Each digit of passed in p_word decreases by 3. (written by Braden Azis)
def decode(p_word):
    code = ''
    for i in range(len(p_word)):  # loops through each digit of passed through p_word
        digit = int(p_word[i]) - 3

        if digit < 0:  # checks if digit is negative, adds 10 if true
            digit += 10

        digit = str(digit)  # converts digit to string and adds it to existing string variable code
        code += digit

    return code


# Main function of the program.


if __name__ == "__main__":
    while True:     # Loop for menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        select = int(input("Please enter an option: "))

        if select == 1:     # Encoder selected
            password = input("Please enter your password to encode: ")

            # print(int(encode(password)))

            encoded = encode(password)

            print("Your password has been encoded and stored!\n")

        # written by Braden Azis
        elif select == 2:  # decoder menu option
            try:
                decoded = decode(encoded)
                print(f'The encoded password is {encoded}, and the original password is {decoded}.\n')

            except NameError:  # if user has not stored and encoded password, will print error message
                print('No password encoded!\n')

        elif select == 3:
            quit()

        else:
            print("Error: Invalid selection")
