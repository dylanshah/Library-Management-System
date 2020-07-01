# Written by Dylan Shah on 10/12/2019

def getbook():
    """This function opens the database.txt file and checks all the entries
    and returns a line in the database.txt file"""
    #Opens the database file to read the lines
    with open("database.txt", "r") as f:
        #Iterates through each line and splits the line into individual strings
        for line in f:
            s=line.strip()
            string=s.split(":")
            return(string)

if __name__ == '__main__':
    x = getbook()
    print(x)
