#User book organizer banner
print("====================================================")
print("            My Book Library Organizer")
print("====================================================")

#A place for the user's book info to go into
books = []

add_another = "yes"

#A while loop to continue inputting books into organizer
while add_another == "yes":
    book_title = input("Enter book title: ")
    author_name = input("Enter the author's name: ")
    genre = input("Enter the book genre: ")

    book_type = input("Is this book a standalone, duet, trilogy, or a series? ").lower()
    if book_type == "standalone":
        series_name = "n/a"
        book_num = "n/a"
    elif book_type == "duet" or book_type == "trilogy":
        series_name = input("Enter name of the duet or trilogy: ")
        book_num = int(input("Enter number the book is in the duet or trilogy: "))
    elif book_type == "series":
        series_name = input("Enter the series name: ")
        book_num = int(input("Enter the number the book is in the series: "))
    else:
        series_name ="unknown"
        book_num = "unknown"           
    add_another = input("Would you like to add another book? (yes/no): ").lower()
    print()
