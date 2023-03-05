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

        elif select == 2:
            pass    # TODO: add decoder function

        elif select == 3:
            quit()

        else:
            print("Error: Invalid selection")
