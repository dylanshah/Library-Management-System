# Written by Dylan Shah on 10/12/2019

import matplotlib.pyplot as plt


def visualizebook():
    """This function checks the logfile and database and appends items to a list
    that can be used as data to make a graph on the popularity of books"""
    #Empty lists for filling to display data
    ids = []
    frequency = []
    titles = []
    booknames=[]
    #This opens database.txt and exports all the book names to a new list
    with open("database.txt" , "r") as f:
        for line in f:
            s=line.strip()
            string2=s.split(":")
            ids.append(string2[0])
            booknames.append(string2[1])
    for id in ids:
      #Counts the number of same books have been borrowed and appends to a list
        with open("logfile.txt", "r") as l:
            count = 0
            for line in l:
                s=line.strip()
                string3=s.split(":")
                if id == string3[0]:
                    count += 1
            frequency.append(count)
    #Uses the number of books borrowed and the book names to plot a graph
    def popularbooks(booknames, frequency):
        """This function takes the frequency list and the booknames list as
        inputs for the data used to generate the graph to visualize the
        popularity of the borrowing of books.

        booknames = This is a list of all the book Titles in the database
        frequency = This is a list of the number of times each book has been
        borrowed."""

        x = booknames
        y = frequency

        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()#Prints the bar graph
    #calls the function so that the graph can be returned to the GUI
    popularbooks(booknames, frequency)
    return(plt.show())

def dispbook():
    """This function displays the books in order or popularity according to the
    data from the graph, by iterating through the entries in the log file and
    all the book titles from the database file."""
    #Empty lists for filling to display data
    ids = []
    frequency = []
    titles = []
    booklist = []
    combinelist = []
    booknames=[]
    with open("database.txt", "r") as f:
        #Opens database.txt and appends all book names to a new list
        for line in f:
            s=line.strip()
            string2=s.split(":")
            ids.append(string2[0])
            booknames.append(string2[1])
    for id in ids:
        #Opens logfile.txt and counts the same number of book ID's
        with open("logfile.txt", "r") as l:
            count = 0
            for line in l:
                s=line.strip()
                string3=s.split(":")
                if id == string3[0]:
                    count += 1
            frequency.append(count)
    #This sorts the frequency of books borrowed with the book names in a list
    for i in range(len(frequency)):
        combinelist.append([frequency[i], ids[i]])
        combinelist.sort(reverse=True)
    for item in combinelist:
        with open("database.txt", "r") as f:
            for line in f:
                s = line.strip()
                string4=s.split(":")
                if item[1] == string4[0]:
                    booklist.append(string4)
    return(booklist)


if __name__ == "__main__":
    x = dispbook()
    y = visualizebook()
    print(x)
    print(y)
