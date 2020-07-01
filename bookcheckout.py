# Written by Dylan Shah on 10/12/2019

from datetime import date
import shutil
from database import *

checkoutdate=date.today()

message = ""#Makes message a global variable

#Carries out the funcrtion to checkout books
def bkcheckout(memberID, bookID):
    """Function that takes entries to checkout books, It verifies if the inputs
    are valid and displays error messages accordingly:

       memberID = This is the unique ID each customer is identified by
       bookID = This is a unique ID each book is identified by"""
    f = getbook()#Calls the function from database.py
    #Iterates through all the book ID's
    for line in f:
        s= line.strip()
        string= s.split(":")
        if bookID != string[0]:#Checks if the input is within the range
                message = "Book ID not found"
    #Performs Validation checks
    if memberID == "":
        message = "Member ID must be entered!"

    elif bookID == "":
        message = "Book ID must be entered!"

    elif len(str(memberID)) != 4:
        message = "Member ID not Valid!"

    else:
        #Creates a temporary file called new_file
        with open("database.txt", "r") as f, open("new_file.txt", "w") as fnew:
            for line in f:
                s = line.strip()
                string = s.split(":")#splits the line at every occurence of ":"
                ID = string[0]
                borrower = string[-1]
                status = string[3]

                #Checks if the book is already borrowed or not
                if borrower != "0" and bookID == ID:
                    fnew.write(line)
                    message = "Book already borrowed"
                    continue

                elif bookID == ID:
                    #writes on the temporary file and is then moved to database
                    fnew.write(string[0]+":"+string[1]+":"+string[2]+
                    ":Borrowed:"+string[-2]+":"+str(memberID)+"\n")
                    message = "Book withdrawn successfully"
                    #opens logfile.txt to append the entry of book checkout
                    with open("logfile.txt", "a") as r:
                        r.write(string[0]+":"+str(checkoutdate)+":"+""+"\n")


                else:
                    fnew.write(line)

        #Moves the new file to overwrite the database file
        shutil.move("new_file.txt", "database.txt")
    return(message)

if __name__ == "__main__":
    x=int(input("MemberID: "))
    y=input("bookID: ")
    z = bkcheckout(x,y)
    print(z)
