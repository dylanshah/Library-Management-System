# Written by Dylan Shah on 10/12/2019

def bksearch(bookname):
    """This function take the book name input and searches for the book:

       bookname = Name of the book being searched"""
    with open("database.txt", "r") as f:
    #Compares the search item with items in the database
        booklist=[]
        for line in f:
            s=line.strip()
            string=s.split(":")
            name = string[1].lower()
            #Changes the search to lowercase for uniformity
            book = bookname.lower()
            if book == "":
                return(booklist)

            #Searches nemes of books with the number of characters input
            elif book == name[:len(book)]:
                booklist.append(string)

    return(booklist)

if __name__ == "__main__":
    bookname = input("Book Name: ")
    x = bksearch(bookname)
    print(x)
