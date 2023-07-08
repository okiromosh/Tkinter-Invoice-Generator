import datetime
from docxtpl import DocxTemplate
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk, messagebox

invoice_list = []


def add_item():
    desc = description_entry.get().upper()
    qty = int(quantity_entry.get())
    price = int(unit_price_entry.get())
    price_formatted = format(int(price), ",d")
    # unit_total = format(int(price * qty), ",d")
    unit_total = int(price * qty)

    invoice_items = [desc, qty, price_formatted, unit_total]
    invoice_list.append(invoice_items)

    tree.insert('', 0, values=invoice_items)


def clear_item():
    for entry in [
        description_entry, quantity_entry, unit_price_entry,
    ]:
        entry.delete(0, END)


def generate_invoice():
    doc = DocxTemplate('temp.docx')

    date = date_entry.get()
    name = name_entry.get().upper()
    address = address_entry.get().upper()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    tax = 0.1
    total = int(subtotal * (1 + tax))

    doc.render(
        {
            "date": date,
            "name": name,
            "address": address,
            "phone": phone,
            "invoice_list": invoice_list,
            "subtotal": subtotal,
            "tax": str(tax * 100) + '%',
            "total": total

        }
    )

    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)

    messagebox.showinfo(title="Invoice Created", message="Invoice Created")


def new_invoice():
    for entry in [
        name_entry, address_entry, phone_entry
    ]:
        entry.delete(0, END)
        clear_item()
        tree.delete(*tree.get_children())
        invoice_list.clear()


window = Tk()
window.title("Invoice Generator")

frame = Frame(window)
frame.pack(padx=20, pady=20)

date_label = Label(frame, text='Date: ')
date_label.grid(row=0, column=2)

date_entry = DateEntry(frame, selectmode='day', date_pattern='dd/MM/yyyy')
date_entry.grid(row=0, column=3)

separator = ttk.Separator(frame, orient="horizontal")
separator.grid(column=0, row=1, columnspan=4, padx=10, pady=10, sticky="ew")

name_label = Label(frame, text="Client Name: ")
name_label.grid(row=2, column=0)
name_entry = Entry(frame, )
name_entry.grid(row=3, column=0)

address_label = Label(frame, text="Address: ")
address_label.grid(row=2, column=1)
address_entry = Entry(frame, )
address_entry.grid(row=3, column=1)

phone_label = Label(frame, text="Phone")
phone_label.grid(row=2, column=3)
phone_entry = Entry(frame, )
phone_entry.grid(row=3, column=3)

separator = ttk.Separator(frame, orient="horizontal")
separator.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

description_label = Label(frame, text="Description")
description_label.grid(row=5, column=0)
description_entry = Entry(frame, )
description_entry.grid(row=6, column=0)

quantity_label = Label(frame, text="Quantity", )
quantity_label.grid(row=5, column=1)
quantity_entry = Spinbox(frame, from_=1, to=100)
quantity_entry.grid(row=6, column=1)

unit_price_label = Label(frame, text="Unit Price:")
unit_price_label.grid(row=5, column=3)
unit_price_entry = Entry(frame, )
unit_price_entry.grid(row=6, column=3)

separator = ttk.Separator(frame, orient="horizontal")
separator.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

add_item_button = Button(frame, text="Add Item", command=lambda: [add_item(), clear_item()])
add_item_button.grid(row=8, column=3)

'''
separator = ttk.Separator(frame, orient="horizontal")
separator.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
'''

display = ("one", "two", "three", "four")
tree = ttk.Treeview(frame, columns=display, show="headings")
tree.heading("one", text="Description")
tree.heading("two", text="Quantity")
tree.heading("three", text="Unit Price")
tree.heading("four", text="Total")
tree.grid(row=10, column=0, columnspan=4, padx=20, pady=20)

save_invoice = Button(frame, text="Generate Invoice", command=lambda: [generate_invoice(), new_invoice()])
save_invoice.grid(row=11, column=0, columnspan=4, sticky="NEWS")

invoice = Button(frame, text="New Invoice", command=new_invoice)
invoice.grid(row=12, column=0, columnspan=2, )

show_invoice = Button(frame, text="Show Invoice")
show_invoice.grid(row=12, column=1, columnspan=2, padx=20, pady=20)

window.mainloop()
