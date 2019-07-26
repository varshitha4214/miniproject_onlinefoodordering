from tkinter import *
import tkinter as tk
import backendadmin
def insert_text():
    backendadmin.insert(itemid_text.get(),itemname_text.get(),hotel_text.get(),price_text.get(),quantity_text.get(),phoneno_text.get(),address_text.get())


def update_text():
    backendadmin.update(itemid_text.get(), itemname_text.get(), hotel_text.get(), price_text.get(),quantity_text.get(),phoneno_text.get(),address_text.get())

def delete_text():
    backendadmin.delete(itemid_text.get())

def view_text():
    list1.delete(0, END)
    for rows_view in backendadmin.view():
        list1.insert(END, rows_view)

def search_text():
    list1.delete(0,END)
    for rows_search in backendadmin.search(itemname_text.get(),price_text.get()):
        list1.insert(END,rows_search)


mycolor="pink"
window=tk.Tk()
window.configure(bg=mycolor)
l1=Label(window,text="Item Name",bg="sky blue",font="Arial")
l1.grid(row=0,column=0)

l2=Label(window,text="Item Id",bg="sky blue",font="Arial")
l2.grid(row=1,column=0)

l3=Label(window,text="Hotel Name",bg="sky blue",font="Arial")
l3.grid(row=2,column=0)

l4=Label(window,text="Price",bg="sky blue",font="Arial")
l4.grid(row=3,column=0)

l5=Label(window,text="Quantity",bg="sky blue",font="Arial")
l5.grid(row=4,column=0)

l6=Label(window,text="Phone no",bg="sky blue",font="Arial")
l6.grid(row=5,column=0)

l7=Label(window,text="Address",bg="sky blue",font="Arial")
l7.grid(row=6,column=0)

itemname_text=StringVar()
itemid_text=StringVar()
hotel_text=StringVar()
price_text=StringVar()
quantity_text=StringVar()
phoneno_text=StringVar()
address_text=StringVar()

e1=Entry(window,textvariable=itemname_text)
e1.grid(row=0,column=1)

e2=Entry(window,textvariable=itemid_text)
e2.grid(row=1,column=1)

e3=Entry(window,textvariable=hotel_text)
e3.grid(row=2,column=1)

e4=Entry(window,textvariable=price_text)
e4.grid(row=3,column=1)

e5=Entry(window,textvariable=quantity_text)
e5.grid(row=4,column=1)

e6=Entry(window,textvariable=phoneno_text)
e6.grid(row=5,column=1)

e7=Entry(window,textvariable=address_text)
e7.grid(row=6,column=1)

b1=Button(window,text="Insert",command=insert_text,bg="light green",font="Times")
b1.grid(row=0,column=4)

b2=Button(window,text="Update",command=update_text,bg="light green",font="Times")
b2.grid(row=1,column=4)

b3=Button(window,text="Delete",command=delete_text,bg="light green",font="Times")
b3.grid(row=2,column=4)

b4=Button(window,text="View",command=view_text,bg="light green",font="Times")
b4.grid(row=3,column=4)

b5=Button(window,text="Search",command=search_text,bg="light green",font="Times")
b5.grid(row=4,column=4)

list1=Listbox(window,height=5,width=50,bg="violet",fg="dark blue",font="Italic")
list1.grid(row=7,column=0,rowspan=5,columnspan=5)
sb=Scrollbar(window)
sb.grid(row=7,column=5,rowspan=12)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

window.mainloop()
