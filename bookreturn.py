# Written by Dylan Shah on 10/12/2019

from datetime import date
import shutil
from database import *

returndate=date.today()

message = ""#Makes it a global variable

def editlog(bookID):
    """This function edits the logfile while a book is being returned by
    appending the entry to add the date of return:

        bookID = This is the unique identification of each book"""

    #opens a temporary file to append the checkout entry on the logfile
    with open("logfile.txt", "r") as r, open("temp2file.txt", "w") as rnew:
        for line in r:
            s=line.strip()
            elem=s.split(":")
            #Checks if the entry on the logfile doesnt have a return date
            if elem[0]==bookID and elem[2]=="":
                #Edits the entry on the temporary file
                rnew.write(elem[0]+":"+elem[1]+":"+str(returndate) +"\n")
            else:
                rnew.write(line)
        #moves the temporary file line to the logfile
    shutil.move("temp2file.txt", "logfile.txt")

#creates a function to return books
def bkreturn(bookID):
    """Function that takes an input to return a book by performing valid Checks,
    the editing the book status in the database.txt file:

       bookID = The unique ID belonging to a specific book"""
    f = getbook()
    #Iterates through the book ID's in database to see if the input is valid
    for line in f:
        s= line.strip()
        string= s.split(":")
        if bookID != string[0]:
            message = "Book ID not found!"

    if bookID == "":
        message = "Book ID must be entered!"

    if bookID == "0":
        message = "Book ID not valid"


    else:
        #creates a temp file to write the return entry in the database.txt
        with open("database.txt", "r") as f, open("temp1file.txt", "w") as fnew:
            for line in f:
                s = line.strip()
                string = s.split(":")

                #Checks if book is already returned
                if string[-1] == "0" and string[0] == bookID:
                    message = "Book already available"
                    fnew.write(line)
                    continue

                if string[-1] != "0" and string[0] == bookID:
                    #writes the new line on the temporary file
                    fnew.write(str(bookID)+":"+string[1]+":"+string[2]+
                    ":Available:"+string[-2]+":0"+"\n")
                    message = "Book Returned successfully"
                    editlog(bookID)

                else:
                    fnew.write(line)

        #Changes the status of the book returned on the database.txt file
        shutil.move("temp1file.txt", "database.txt")
    return(message)

if __name__ == "__main__":
    y=input("bookID: ")
    x = bkreturn(y)
    z = editlog(y)
    print(x)
    print(z)
