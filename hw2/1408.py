desire = input().lower()

books, i, ans = [], 0, 0
while True:
    book = input()
    if book == 'q': break

    i += 1
    books.append(book)
    if (book == desire):
        ans = i

if (ans):
    print("Yes", ans)
else:
    print("No", i)
