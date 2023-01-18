# fav_book = input()
# count_books = 0
# while True:
#     book = input()
#     count_books += 1
#     if book == fav_book:
#         count_books -= 1
#         print(f"You checked {count_books} books and found it.")
#         break
#     elif book == 'No More Books':
#         count_books -= 1
#         print("The book you search is not here!")
#         print(f"You checked {count_books} books.")
#         break




book = input()
count_books = 0
input_line = input()
while input_line != 'No More Books':
    if input_line == book:
        print(f"You checked {count_books} books and found it.")
        break

    count_books += 1
    input_line = input()
else:
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")