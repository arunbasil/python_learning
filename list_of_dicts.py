books = [
    {'title': "The Road Ahead", 'author': "Bill Gates", 'yearPublished': 1995, 'price': 25.99},
    {'title': "Walter Isaacson", 'author': "Steve Jobs", 'yearPublished': 2011, 'price': 30.00},
    {'title': "Mockingjay: The Final Book of The Hunger Games", 'author': "Suzanne Collins", 'yearPublished': 2010,
     'price': 12.99},
    {'title': "The Catcher in the Rye", 'author': "J.D. Salinger", 'yearPublished': 1951, 'price': 22.00},
    {'title': "Brave New World", 'author': "Aldous Huxley", 'yearPublished': 1932, 'price': 19.99},
    {'title': "The Great Gatsby", 'author': "F. Scott Fitzgerald", 'yearPublished': 1925, 'price': 20.99}
]

books_after_2000 = [book for book in books if book['yearPublished'] > 2000]

print(books_after_2000)

books_after_2000 = []

for book in books:
    if book['yearPublished'] > 2000:
        books_after_2000.append(book)

print(books_after_2000)
