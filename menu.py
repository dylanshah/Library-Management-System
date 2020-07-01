# Written by Dylan Shah on 10/12/2019

from tkinter import*
from tkinter import Tk
from bookcheckout import *
from bookreturn import *
from booksearch import *
from database import *
from booklist import *

gui= Tk()

gui.title("Dylan's Library")
gui.geometry("900x750")
gui.configure(background="turquoise")

#What type the inputs are stored as
bookIDentry=StringVar()
bknameentry=StringVar()
membIDentry=IntVar()

#----------------Frame------------
#All the widgets used in designing the Gui

Frame=Label(gui, text="Dylan's Library", font=("Arial", 36, "bold"),
bg="cyan", borderwidth=10, relief="ridge", width=1000)
Frame.pack()

libdetails=Label(text="Enter Details", font=("Arial", 16), bg="turquoise")
libdetails.place(x=5, y=100)

libframe=Label(gui, borderwidth=10, relief="ridge", width=70, height=15,
bg="light grey")
libframe.place(x=5, y=130)

messagedisplay=Listbox(libframe, borderwidth=10, relief="flat", width=30,
height=1, bg="light grey")
messagedisplay.place(x=10, y=185)

bookdisplay=Label(text="Book Display",font=("Arial", 16), bg="turquoise")
bookdisplay.place(x=5, y=400)

displayframe=Label(gui, borderwidth=10, relief="ridge", width=100, height=14,
bg="light grey")
displayframe.place(x=5, y=430)

buttonframe=Label(gui, borderwidth=10, relief="ridge", width=100, height=3,
bg="light grey")
buttonframe.place(x=5, y=680)

#----------------------Input Section---------------
#widgets associated with the inputs
bookID=Label(libframe, text="Book ID:", font=("Arial", 16), bg="light grey")
bookID.place(x=25, y=25)

bkIDentry=Entry(libframe, bg="white", textvariable=bookIDentry)
bkIDentry.place(x=180, y=25)

bookname=Label(libframe, text="Book Name:", font=("Arial", 16), bg="light grey")
bookname.place(x=25, y=85)

bknmentry=Entry(libframe, bg="white", textvariable=bknameentry)
bknmentry.place(x=180, y=85)

memberID=Label(libframe, text="Member ID:", font=("Arial", 16), bg="light grey")
memberID.place(x=25, y=145)

memIDentry=Entry(libframe, bg="white", textvariable=membIDentry)
memIDentry.place(x=180, y=145)

#--------------------Display Section------------------

tablabel=Label(displayframe,relief="flat",bg="light grey",width=98,height=2,text
="Book ID\tBook Name\t\t\tAuthor\t\t\tBook Status\tPurchase Date\tMember ID")
tablabel.place(x=10, y=10)

tablabel2= Label(displayframe)
tablabel2.place(x=25, y=45)

listbox1=Listbox(tablabel2, relief="flat", bg="light grey", width=8)
listbox1.grid(row=0, column=0)
listbox2=Listbox(tablabel2, relief="flat", bg="light grey", width=25)
listbox2.grid(row=0, column=1)
listbox3=Listbox(tablabel2, relief="flat", bg="light grey", width=30)
listbox3.grid(row=0, column=2)
listbox4=Listbox(tablabel2, relief="flat", bg="light grey", width=15)
listbox4.grid(row=0, column=3)
listbox5=Listbox(tablabel2, relief="flat", bg="light grey", width=16)
listbox5.grid(row=0, column=4)
listbox6=Listbox(tablabel2, relief="flat", bg="light grey", width=9)
listbox6.grid(row=0, column=5)

#---------------------Search Function------------------

def booksearch():
    """ This function calls the search function in booksearch.py and prints to
    result to the listboxes """
    #calls the bksearch function from booksearch.py using the user input
    x = bksearch(bknmentry.get())
    bknmentry.delete(0, END)
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    listbox3.delete(0, END)
    listbox4.delete(0, END)
    listbox5.delete(0, END)
    listbox6.delete(0, END)
    #Prints the result to the listbox
    for i in x:
        listbox1.insert(END, i[0])
        listbox2.insert(END, i[1])
        listbox3.insert(END, i[2])
        listbox4.insert(END, i[3])
        listbox5.insert(END, i[4])
        listbox6.insert(END, i[5])

#-------------------Checkout Function----------

def bookcheckout():
    """This function calls the function in bookcheckout.py and prints the result
    to the error listbox"""
    #Calls the bkcheckout function from bookcheckout.py using the user input
    y =bkcheckout(membIDentry.get(), bookIDentry.get())
    bkIDentry.delete(0, END)
    memIDentry.delete(0, END)
    #displays the error message to the label
    messagedisplay.delete(0, END)
    messagedisplay.insert(END, y)



#-----------------Return Function--------------------
"""This function calls the function in bookreturn.py and prints the result to
the error listbox"""
def bookreturn():
    z=bkreturn(bookIDentry.get())
    bkIDentry.delete(0, END)
    messagedisplay.delete(0, END)
    messagedisplay.insert(END, z)


#------------------Display Function------------------

def bookdisplay():
    """This function calls the function from booklist.py and prints the data to
    the listboxes"""
    a=dispbook()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    listbox3.delete(0, END)
    listbox4.delete(0, END)
    listbox5.delete(0, END)
    listbox6.delete(0, END)
    #prints the book results to the listbox
    for i in a:
        listbox1.insert(END, i[0])
        listbox2.insert(END, i[1])
        listbox3.insert(END, i[2])
        listbox4.insert(END, i[3])
        listbox5.insert(END, i[4])
        listbox6.insert(END, i[5])

#--------------Visualize Book--------------

def visualize():
    """This calls the matplotlib graph function and opens up the graph to
    visualize data"""
    #calls the functino to show the graph
    b = visualizebook()


#--------------Exit Function------------------

def screen_exit():
    """This is a function to close the whole screen"""
    gui.destroy()
    return

#--------------------Button Section-------------------

checkoutbutton=Button(buttonframe, text="Checkout Book",font=("Arial", 11,
"bold"), bg="light grey", relief="ridge", bd=5, width=17, command=bookcheckout)
checkoutbutton.place(x=1, y=5)

visualbutton=Button(libframe, text="Visualize Data",font=("Arial", 11, "bold"),
bg="light grey", relief="ridge", bd=5, width=13, command=visualize)
visualbutton.place(x=340, y=145)

returnbutton=Button(buttonframe, text="Return Book", font=("Arial", 11,
"bold"), bg="light grey", relief="ridge", bd=5, width=17, command=bookreturn)
returnbutton.place(x=180, y=5)

displaybtn=Button(buttonframe, text="Display Book", font=("Arial", 11, "bold"),
bg="light grey", relief="ridge", bd=5, width=17, command=bookdisplay)
displaybtn.place(x=355, y=5)

searchbutton=Button(libframe, text="Search Book", font=("Arial", 12, "bold"),
bg="light grey", relief="ridge", bd=4, command=booksearch)
searchbutton.place(x=340, y=185)

closebutton=Button(buttonframe, text="Close", font=("Arial", 11, "bold"),
bg="light grey", relief="ridge", bd=5, width=17, command=screen_exit)
closebutton.place(x=533, y=5)



gui.mainloop()
