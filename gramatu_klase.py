class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def read_pages(self, pages_read):
        print(f"Jūs esat izlasījis {pages_read} lapas no grāmatas '{self.title}'.")

    def is_long_book(self):
        return self.pages > 300
            
objekts1 = Book("Anna",50,"grāmatu")

print(objekts1.read_pages(500))