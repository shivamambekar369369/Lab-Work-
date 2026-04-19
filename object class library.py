class Library:

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True   

    def check_out(self):
        if self.available == True:
            self.available = False
            print("Book checked out successfully.")
        else:
            print("Book is not available.")

    def return_book(self):
        if self.available == False:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book was already available.")

    def display(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Available:", self.available)
        print("----------------------")


book1 = Library("Maths", "RD Sharma")
book2 = Library("Physics", "HC Verma")
book3 = Library("Chemistry", "OP Tandon")

book1.display()
book2.display()
book3.display()

book1.check_out()
book1.display()

book1.return_book()
book1.display()
