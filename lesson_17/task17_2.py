class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []

    def new_book(self, name: str, year: int, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.author.append(author)
        Book.books += 1
        author.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        books_list = []
        for book in self.books:
            if book.author == author:
                books_list.append(book)
        return books_list

    def group_by_year(self, year: int):
        books_list = []
        for book in self.books:
            if book.year == year:
                books_list.append(book)
        return books_list

    def __repr__(self):
        return f'Name: {self.name}\n' \
               f'books:{self.books}\n' \
               f'author: {self.author}'


class Book:
    books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'name: {self.name}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Name: {self.name}'


auth1 = Author('Mykola', 'Ukraine', '1930')
auth2 = Author('Petro', 'Ukraine', '1950')
book1 = Book('Abetka', '1960', auth1)
book2 = Book('Book', '1980', auth2)
lib1 = Library('Main')
print(lib1)
print()
lib1.new_book('Abetka+', 1960, auth1)
lib1.new_book('Book+', 1980, auth2)
print(lib1)
print()
print(lib1.group_by_author(auth1))
print(lib1.group_by_year(1980))
