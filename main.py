from tkinter import *
import pymongo

main = Tk()
main.title("MongoDB Library Manager")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
bookdb = myclient["Librarydb"]
mybooks = bookdb["allBooks"]
rentedbooks = bookdb["rentedBooks"]


button_rent = Button(main, text="Rent a book")
button_rent.pack(padx=25, pady=25)

button_return = Button(main, text="Return a book")
button_return.pack(padx=25, pady=25)

button_addbook = Button(main, text="Add a book to Library", command=lambda:addbookfn())
button_addbook.pack(padx=25, pady=25)

button_rmbook = Button(main, text="Remove a book from Library", command=lambda:rmbookfn())
button_rmbook.pack(padx=25, pady=25)

def addbookfn():
    smain = Tk()
    smain.geometry("300x200")
    label_bname = Label(smain, text="Enter name of book")
    label_bname.grid(row=6, column=6)
    entry_bname = Entry(smain)
    entry_bname.grid(row=6, column=100)
    
    label_aname = Label(smain, text="Enter name of author")
    label_aname.grid(row=8, column=6)
    entry_aname = Entry(smain)
    entry_aname.grid(row=8, column=100)

    label_isbn = Label(smain, text="Enter ISBN of book")
    label_isbn.grid(row=10, column=6)
    entry_isbn = Entry(smain)
    entry_isbn.grid(row=10, column=100)

    button_submit = Button(smain, text="ADD", command=lambda:insertdb(entry_bname, entry_aname, entry_isbn))
    button_submit.grid(row=20, column=10)

def insertdb(ebname,eaname,eisbn):
    bname = ebname.get()
    aname = eaname.get()
    isbn = eisbn.get()

    val = {"Book Name":bname, "Author Name":aname, "ISBN":isbn}
    x = mybooks.insert_one(val)

def rmbookfn():
    smain = Tk()
    smain.geometry("400x600")
    lbox = Listbox(smain, width=150)
    for x in mybooks.find({},{"_id":0,"Book Name":1,"Author Name":1,"ISBN":1}):
        x = dict(x)
        lbox.insert(1,x)
    lbox.pack()

    label_rm = Label(smain, text="Enter ISBN of book to remove from Library")
    label_rm.pack()

    entry_rm = Entry(smain)
    entry_rm.pack()

    button_rm = Button(smain, text="Remove", command=lambda:rmdb(entry_rm))
    button_rm.pack()

def rmdb(rmisbn):
    isbn = rmisbn.get()
    myquery = {"ISBN":isbn}
    mybooks.delete_one(myquery)

        
    
    
    
    
