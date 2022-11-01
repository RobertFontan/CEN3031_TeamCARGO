from isbn import lookup_isbn
import book

# this does not work
while True:
    isbn = input("Enter an ISBN: ").strip()
    lookup_isbn(isbn)

    bookList = []
    bookList.append(lookup_isbn)

    user_update = input("Want another ISBN? [Y/N] ").lower().strip()
    
    if user_update != "y":
        break 
    
print(len(bookList))