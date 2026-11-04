#Banner for the Number Cruncher program
print("=====================Number Cruncher=====================")

#Make a list with numbers copied from week 5 data file
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

#Keep showing the menu until the user chooses to quit
while True:
    #Show the menu options
    print("\nMenu:")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    

    #Ask the user to choose an option
    choice = input("Please choose an option (1-5): ")

    #Perform the action based on the user's choice
    if choice == "1":
        #Start by remembering the first number
        smallest = numbers[0]
        #Look at each number in the list
        for num in numbers:
            #If this number is smaller, remember it instead
            if num < smallest:
                smallest = num
        #Print the smallest number after checking all numbers
        print(f"The minimum number is {smallest}.")
    elif choice == "2":
        #Start by remembering the first number
        largest = numbers[0]
        #Look at each number in the list
        for num in numbers:
            #If this number is larger, remember it instead
            if num > largest:
                largest = num
        #Print the largest number after checking all numbers
        print(f"The maximum number is {largest}.") 
    elif choice == "3":
        #Ask the user for a number to search for
        search_num = int(input("Enter a number to search for: "))
        #Flag to check if the number is found
        found = False
        #Look at each number in the list
        for i in range(len(numbers)):
            #If this number matches the search number, set found to True and break out of the loop
            if numbers[i] == search_num:
                print(f"Found {search_num} in the list at index {i}.")
                found = True
                break
        #Print whether the number was found or not
        if found == False:
            print(f"{search_num} was not found in the list.")
    elif choice == "4":
        #Make a copy so the original list stays the same
        sorted_nums = numbers[:]
        #Keep making passes until a pass has no swaps
        swapped = True
        while swapped:
            swapped = False
            #Compare each pair of neighbors
            for i in range(len(sorted_nums) -1):
                #If the left number is bigger, swap them
                if sorted_nums[i] > sorted_nums[i + 1]:
                    temp = sorted_nums[i]
                    sorted_nums[i] = sorted_nums[i + 1]
                    sorted_nums[i + 1] = temp
                    swapped = True
        #Print the sorted list
        print(f"The sorted list is: {sorted_nums}")
    elif choice == "5":
        #Say goodbye and break out of the loop to quit
        print("Thank you for using Number Cruncher. Goodbye!")
        break
    else:
        #Anything that isn't 1-5
        print("Invalid option. Please choose a number between 1 and 5.")