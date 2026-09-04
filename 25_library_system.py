books = {}

def add_book(name):
    books[name] = True

def issue_book(name):
    if name in books and books[name] == True:
        books[name] = False
        print("Book Issued")
    else:
        print("Book Not Available")

def return_book(name):
    if name in books:
        books[name] = True
        print("Book Returned")

def search_book(name):
    if name in books:
        print("Book Found")
    else:
        print("Book Not Found")

def display_books():
    print("Available Books:")
    for name in books:
        if books[name] == True:
            print(name)

add_book("Python")
add_book("Java")
add_book("C++")

issue_book("Python")
return_book("Python")
search_book("Java")
display_books()
