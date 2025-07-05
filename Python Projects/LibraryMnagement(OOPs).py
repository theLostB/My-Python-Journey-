class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
    def showInfo(self):
        print(f"\nThe Library Has {self.noBooks} Books. The Books are:")
        for book in self.books:
            print(book)
            
l1 = Library()
Bkn = int(input("How many books you want to add: "))
for i in range(Bkn):
    Bk = input('Enter the book name: ')
    l1.addBook(Bk)
l1.showInfo()