#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 7, 2022
# This program asks the user for a number with decimals and rounds
# it to a specified number of decimals places with pass by reference


# This function rounds a number with decimals to a specified number of places using pass by reference
def round_decimal(number, num_decimals):
    # Rounds the user's number
    # Multiplies the number by 10^num_decimals
    number[0] *= 10**num_decimals

    # Adds 0.5 to the number
    number[0] += 0.5

    # Casts number to int (to cut of decimals)
    number[0] = int(number[0])

    # Divides number by 10^num_decimals
    number[0] /= 10**num_decimals


def main():
    # Checks for exceptions
    try:
        # Asks user for the number they want to round
        user_number = float(input("Enter a decimal number: "))

        # Asks user how many decimal places they want to round to
        user_num_decimals = int(
            input("Enter the number of decimal places you want to round to: ")
        )

    # In the event of an exception
    except Exception:
        print("You entered invalid number(s)!")
    else:
        # Initializes list to pass by reference in Python
        user_number_holder = []

        # Adds user's number to the list
        user_number_holder.append(user_number)

        # Calls function to round the user's number (passing by reference)
        round_decimal(user_number_holder, user_num_decimals)

        # Displays to user their rounded number
        print(
            f"{user_number} rounded to {user_num_decimals} places: {user_number_holder[0]}"
        )


if __name__ == "__main__":
    main()
