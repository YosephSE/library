books = {
    'Eat that frog': 10,
    'Atomic habits': 29,
    'Rich dad poor dad': 12,
    'Why we sleep': 10,
    'Limitless': 22,
    'The power of now': 9,
    'The 7 habits of highly effective people': 21,
    'Becoming': 32,
    'The psychology of money': 18,
    'Make time': 17
}


def book_lister():
    for key, value in books.items():
        print(f'{key}: {value}')


def add():
    title = input("Enter the name of the book: ").capitalize()
    if title not in books.keys():
        copies = int(input('Enter number of copies: '))
        books[title] = copies
        book_lister()
    else:
        print("You are trying to add an existing book. use option 2")


def add_copies():
    title = input("Enter the name of the book: ").capitalize()
    if title in books.keys():
        copies = int(input('Enter number of copies: '))
        books[title] = books[title] + copies
        book_lister()
    else:
        print("You are trying to add copies to non-existing book. use option 1")


def sub_copies():
    title = input("Enter the name of the book: ").capitalize()
    if title in books.keys():
        copies = int(input('Enter number of copies: '))
        if books[title] >= copies:
            books[title] = books[title] - copies
            book_lister()
        else:
            print("Sorry to not fulfill your demand. there is limited copies left.")
    else:
        print("You are trying to subtract copies to non-existing book.")


print('Currently we have the following books in store: ')
book_lister()
print('''Enter 
        1) to add new book 
        2) to add copies to existing book
        3) to remove book''')
choose = input("What do you want: ")
if choose == '1':
    add()
elif choose == '2':
    add_copies()
elif choose == '3':
    sub_copies()
else:
    print(f'{choose} is undefined read the command please!!!')
# this is a test from git
