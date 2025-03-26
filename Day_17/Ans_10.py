# Implement operator overloading (+ for combining two objects).
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        new_title = f"{self.title} & {other.title}"
        new_pages = self.pages + other.pages
        return Book(new_title, new_pages)

    def __str__(self):
            return f"{self.title} ({self.pages} pages)"

book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

combined_book = book1 + book2
print(combined_book)
