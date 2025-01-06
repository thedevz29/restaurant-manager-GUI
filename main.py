from tkinter import *
root = Tk()
root.geometry("800x800")
root.title("thedevz Restaurant Manager")

menu = '''1.Water----------20\n2.Tea----------30\n3.Maggie----------40\n4.Pizza----------100\n5.Coffee(fully customised)----------60\n6.Dahi Kabab----------50\n7.Coldrink(Thumbsup,Sprite,Fanta,Limca 20/- bottle)----------20\n8.Indian Thali(all Indian cuisines)----------500'''

menu_label = Label(text=menu, bg = "black", fg = "white")

menu_button = Button(text=menu, bg = "white", fg = "black", activebackground="black", activeforeground= "white")

order_label = Label(text="Enter the item number you want to order below", bg="white", fg = "black")
order_entry = Entry()
order = int(order_entry.get())

