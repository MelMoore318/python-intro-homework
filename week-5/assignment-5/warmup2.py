#Create a while loop to ask the user for a positive number and keep asking until they enter a positive number.
while True:
    user_input = input("Please enter a positive number: ")
    try:
        number = int(user_input)
        if number > 0:
            print(f"Thank you! You entered a positive number: {number}")
            break
        else:
            print("That's not a positive number. Please try again.")
    except ValueError:
        print("That's not a valid number. Please try again.")
