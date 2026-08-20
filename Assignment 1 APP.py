class Library:
    def __init__(self, books=None):
        self.books = books[:] if books else ["MFC", "MCD", "DSA"]

    def show_books(self):
        print("Available books:", self.books)

    def borrow_book(self, *requested_books):
        for book in requested_books:
            if book in self.books:
                self.books.remove(book)
                print(f"{book} borrowed successfully.")
            else:
                print(f"{book} is not available.")

    def return_book(self, book):
        if book in self.books:
            print(f"{book} is already in the library.")
        else:
            self.books.append(book)
            print(f"{book} returned successfully.")

# Example usage:
lib = Library()
lib.show_books()

b1 = input("Enter 1st book to borrow: ").strip()
b2 = input("Enter 2nd book to borrow (or press Enter to skip): ").strip()
to_borrow = [b for b in (b1, b2) if b]  # ignore empty input
if to_borrow:
    lib.borrow_book(*to_borrow)

ret = input("Enter the book you want to return (or press Enter to skip): ").strip()
if ret:
    lib.return_book(ret)

lib.show_books()
