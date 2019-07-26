from tkinter import *
import backendadmin
def view_text():
    list1.delete(0, END)
    for rows_view in backendadmin.view():
        list1.insert(END, rows_view)

def search_text():
    list1.delete(0,END)
    for rows_search in backendadmin.search(itemname_text.get(),price_text.get()):
        list1.insert(END,rows_search)
mycolor="sky blue"
window=Tk()
window.title("Online Food Search")
window.configure(bg=mycolor)
l1=Label(window,text="Item Name",bg="pink",fg="dark blue",font="Courier")
l1.grid(row=0,column=0)

l2=Label(window,text="Hotel Name",bg="pink",fg="dark blue",font="Courier")
l2.grid(row=1,column=0)

l3=Label(window,text="Price",bg="pink",fg="dark blue",font="Courier")
l3.grid(row=2,column=0)

l4=Label(window,text="Quantity",bg="pink",fg="dark blue",font="Courier")
l4.grid(row=3,column=0)

itemname_text=StringVar()
hotelname_text=StringVar()
price_text=StringVar()
quantity_text=StringVar()

e1=Entry(window,textvariable=itemname_text,bg="silver",font="Arial")
e1.grid(row=0,column=2)

e2=Entry(window,textvariable=hotelname_text,bg="silver",font="Arial")
e2.grid(row=1,column=2)

e3=Entry(window,textvariable=price_text,bg="silver",font="Arial")
e3.grid(row=2,column=2)

e4=Entry(window,textvariable=quantity_text,bg="silver",font="Arial")
e4.grid(row=3,column=2)

b1=Button(window,text="View",command=view_text,bg="orchid",font="Times")
b1.grid(row=0,column=8)

b2=Button(window,text="Search",command=search_text,bg="orchid",font="Times")
b2.grid(row=2,column=8)

list1=Listbox(window,height=5,width=50,fg="dark blue",font="Italic")
list1.grid(row=5,column=0,rowspan=5,columnspan=5)
sb=Scrollbar(window)
sb.grid(row=5,column=4,rowspan=12)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)


window.mainloop()