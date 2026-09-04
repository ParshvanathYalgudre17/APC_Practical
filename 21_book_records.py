# 21. Book record system

books = {}

def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

def search_book(book_id):
    if book_id in books:
        print("Book Found:", books[book_id])
    else:
        print("Book Not Found")

def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book Issued")
        else:
            print("Book is already issued")
    else:
        print("Book Not Found")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book Returned")
    else:
        print("Book Not Found")

def display_available():
    print("Available Books:")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["title"], book["author"])

add_book(101, "Python", "Guido")
add_book(102, "Java", "James")
add_book(103, "C++", "Bjarne")

display_available()

issue_book(101)
print("\nAfter issuing book:")
display_available()

return_book(101)
print("\nAfter returning book:")
display_available()

search_book(102)
