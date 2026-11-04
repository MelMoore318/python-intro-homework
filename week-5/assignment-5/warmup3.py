#Make a hardcoded list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

#Ask the user to input a name to check if it is in the list
user_input = input("Please enter a name to check if it is in the list: ")

#Flag to check if the name is found
found = False

#Check each name one at a time to see if it matches the user input
for i in range(len(names)):
    if names[i].lower() == user_input.lower():
        print(f"Found {user_input} in the list at index {i}.")
        found = True
        break

#If the name was never found, say so
if found == False:
    print(f" {user_input} was not found in the list.")
    