a = int(input())
books = {}
b=[]
for _ in range(a):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] +=1
max = max(books.values())
for book, number in books.items():
    if number ==max:
        b.append(book)
print(sorted(b)[0])