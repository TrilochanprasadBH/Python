#write a oops class , to issue, display book in library. 

class BookHouse:
    def __init__(self,author,title,pages,available):
        self.author = author
        self.title = title
        self.pages = pages 
        self.available = available

    def displayBook(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"pages:{self.pages}")
        print(f"{'available' if self.available  else 'borrowed'}")
    
    def issueBook(self):
        if self.available:
            self.available = False
            print('Book available and issued')
        else:
            print('book already borrowed')

book1 = BookHouse('Trilo','Roses and Guns',700,True)
book2 = BookHouse('Trilo','Roses and Guns',700,False)
# print(f"Book1 : {book1}")
book1.displayBook()
book1.issueBook()
book2.issueBook()