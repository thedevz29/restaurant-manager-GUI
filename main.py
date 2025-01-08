from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("thedevz Restaurant Manager")

menu = '''1. Water - 20\n2. Tea - 30\n3. Maggie - 40\n4. Pizza - 100\n5. Coffee (fully customized) - 60\n6. Dahi Kabab - 50\n7. Coldrink (Thumbsup, Sprite, etc.) - 20\n8. Indian Thali - 500'''

menu_label = Label(master=root, text=menu, bg="black", fg="white", justify=LEFT)
menu_label.place(x=0, y=55)

order_label = Label(master=root, text="Enter the item number you want to order below", bg="white", fg="black")
order_label.place(x=0, y=200)

order_entry = Entry(master=root)
order_entry.place(x=20, y=250)

def main():
    try:
        order = int(order_entry.get())
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    if order == 5:
        order_label2 = Label(text="Your order is Coffee")
        with open("orders.txt", "a") as file:
            file.write("Coffee - 60\n")
    elif order == 4:
        order_label2 = Label(text="Your order is Pizza")
        with open("orders.txt", "a") as file:
            file.write("Pizza - 100\n")
    elif order == 3:
        order_label2 = Label(text="Your order is Maggie")
        with open("orders.txt", "a") as file:
            file.write("Maggie - 40\n")
    elif order == 2:
        order_label2 = Label(text="Your order is Tea")
        with open("orders.txt", "a") as file:
            file.write("Tea - 30\n")
    elif order == 1:
        order_label2 = Label(text="Your order is Water")
        with open("orders.txt", "a") as file:
            file.write("Water - 20\n")
    elif order == 6:
        order_label2 = Label(text="Your order is Dahi Kabab")
        with open("orders.txt", "a") as file:
            file.write("Dahi Kabab - 50\n")
    elif order == 7:
        order_label2 = Label(text="Your order is Coldrink")
        with open("orders.txt", "a") as file:
            file.write("Coldrink - 20\n")
    elif order == 8:
        order_label2 = Label(text="Your order is Indian Thali")
        with open("orders.txt", "a") as file:
            file.write("Indian Thali - 500\n")
    else:
        order_label2 = Label(text="Invalid order number. Please try again.")
    
    order_label2.place(x=0, y=350)

order_button = Button(master=root, text="Order", command=main)
order_button.place(x=20, y=270)

root.mainloop()