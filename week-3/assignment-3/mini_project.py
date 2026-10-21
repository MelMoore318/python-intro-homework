# Ask the user for the day and time of day
day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day is it? (morning, afternoon, evening) ").strip().lower()

# Check whether the time of day is valid
if time_of_day not in ["morning", "afternoon", "evening"]:
    print("Invalid time of day. Please enter morning, afternoon, or evening.")

# Suggest an activity based on the day and time of day
if day == "monday":
    if time_of_day == "morning":
        print("It's Monday morning! How about a brisk walk to start the week?")
    elif time_of_day == "afternoon":
        print("It's Monday afternoon! Maybe a quick workout or some yoga would be nice.")
    elif time_of_day == "evening":
        print("It's Monday evening! How about some light stretching or meditation before bed?")
    else:
        print("Invalid time of day. Please enter morning, afternoon, or evening.")

elif day == "tuesday":
    if time_of_day == "morning":
        print("It's Tuesday morning! How about a jog or a bike ride to start the day?")
    elif time_of_day == "afternoon":
        print("It's Tuesday afternoon! Maybe a dance class or some strength training would be fun.")
    elif time_of_day == "evening":
        print("It's Tuesday evening! How about a relaxing walk or some gentle yoga before bed?")
    else:
        print("Invalid time of day. Please enter morning, afternoon, or evening.")

elif day == "wednesday":
    if time_of_day == "morning":
        print("It's Wednesday morning! How about a swim or a hike to start the day?")
    elif time_of_day == "afternoon":
        print("It's Wednesday afternoon! Maybe a Pilates class or some core exercises would be great.")
    elif time_of_day == "evening":
        print("It's Wednesday evening! How about a calming yoga session or some meditation before bed?")
    else:
        print("Invalid time of day. Please enter morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Please enter Monday, Tuesday, or Wednesday.")
