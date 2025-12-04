class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Книга '{self.title}', автор: {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

my_book = Book("Дюна", "Герберт Френк")

def main():
   print(my_book)      
   print(repr(my_book))
   
main()