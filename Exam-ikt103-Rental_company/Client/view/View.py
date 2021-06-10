import tkinter as tk
from tkinter import ttk, messagebox
from Requests.Request import car, customer, rentals
from tkcalendar import DateEntry
import requests

color = "#14122a"


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH)

        file().configure_menu()
        self.my_tree = ttk.Treeview(self)

        self.photo = tk.PhotoImage(file="Pictures/background2.png")
        self.photo_label = tk.Label(self, image=self.photo)
        self.photo_label.place(x=0, y=0)
        self.label_space7 = tk.Label(self, height=20, width=1, bg=color)
        self.label_space8 = tk.Label(self, height=4, width=1, bg=color)
        self.label_space9 = tk.Label(self, height=4, width=1, bg="#464646")
        self.label_space10 = tk.Label(self, height=20, width=1, bg=color)
        self.label_space7.place(x=0, y=650)
        self.label_space8.place(x=0, y=64)
        self.label_space9.place(x=0, y=0)

        # Gets
        # Frame
        self.Frame_with_gets = tk.Frame(self, bg=color)
        # Menus
        self.clicked = tk.StringVar()
        self.options = ["id", "brand", "type", "color", "total earned", "all"]
        self.clicked.set(self.options[5])
        self.drop = tk.OptionMenu(self.Frame_with_gets, self.clicked, *self.options)
        self.drop.config(bg="#464646", fg="white")
        self.drop.grid(row=1, column=0)

        self.clicked2 = tk.StringVar()
        self.options2 = ["id", "fullname", "email", "phone", "all"]
        self.clicked2.set(self.options2[4])
        self.drop2 = tk.OptionMenu(self.Frame_with_gets, self.clicked2, *self.options2)
        self.drop2.config(bg="#464646", fg="white")
        self.drop2.grid(row=11, column=0)

        self.clicked3 = tk.StringVar()
        self.options3 = ["rental_id", "car_id", "customer_id", "all"]
        self.clicked3.set(self.options3[3])
        self.drop3 = tk.OptionMenu(self.Frame_with_gets, self.clicked3, *self.options3)
        self.drop3.config(bg="#464646", fg="white")
        self.drop3.grid(row=16, column=0)

        # Labels
        self.label_car = tk.Label(self.Frame_with_gets, text="Car", bg=color, fg="white")
        self.label_car.grid(row=0, column=0)
        self.label_customer = tk.Label(self.Frame_with_gets, text="Customer", bg=color, fg="white")
        self.label_customer.grid(row=10, column=0)
        self.label_rental = tk.Label(self.Frame_with_gets, text="Rental", bg=color, fg="white")
        self.label_rental.grid(row=15, column=0)

        self.label_space1 = tk.Label(self.Frame_with_gets, width=100, height=5, bg=color)
        self.label_space1.grid(row=2, column=0, columnspan=5)

        self.label_space2 = tk.Label(self.Frame_with_gets, width=100, height=5, bg=color)
        self.label_space2.grid(row=12, column=0, columnspan=5)

        self.label_space3 = tk.Label(self.Frame_with_gets, width=100, height=5, bg=color)
        self.label_space3.grid(row=17, column=0, columnspan=5)

        # Entry's
        self.entry_message_car = tk.Entry(self.Frame_with_gets, textvariable=tk.StringVar())
        self.entry_message_car.grid(row=1, column=2, sticky=tk.W, pady=2)

        self.entry_message_customer = tk.Entry(self.Frame_with_gets, textvariable=tk.StringVar())
        self.entry_message_customer.grid(row=11, column=2, sticky=tk.W, pady=2)

        self.entry_message_rental = tk.Entry(self.Frame_with_gets, textvariable=tk.StringVar())
        self.entry_message_rental.grid(row=16, column=2, sticky=tk.W, pady=2)

        # Buttons
        self.btn_search_car = tk.Button(self.Frame_with_gets, text="Search", command=self.create_car_tree, bg="#464646",
                                        fg="white")
        self.btn_search_car.grid(row=1, column=3, sticky=tk.W, pady=2)

        self.btn_search_customer = tk.Button(self.Frame_with_gets, text="Search",
                                             command=self.create_customer_tree, bg="#464646", fg="white")
        self.btn_search_customer.grid(row=11, column=3, sticky=tk.W, pady=2)

        self.btn_search_rental = tk.Button(self.Frame_with_gets, text="Search", command=self.create_rental_tree,
                                           bg="#464646", fg="white")
        self.btn_search_rental.grid(row=16, column=3, sticky=tk.W, pady=2)

        self.Frame_with_gets.place(x=0, y=100)

        # Total earned.
        self.Frame_for_tot_earned = tk.Frame(self, bg=color)
        self.photo1 = tk.PhotoImage(file="Pictures/profit.png")
        self.label_for_profit= tk.Label(self.Frame_for_tot_earned, image=self.photo1)
        self.label_tot_earnings = tk.Label(self.Frame_for_tot_earned, bg=color, fg="white", font=("Courier", 34))
        self.label_for_profit.pack()
        self.label_tot_earnings.pack()
        # Start buttons for add, put and delete
        # Frame
        self.Frame_with_start_buttons = tk.Frame(self, bg=color)

        # Labels
        self.label_space4 = tk.Label(self.Frame_with_start_buttons, width=9, height=5, bg=color)
        self.label_space4.grid(row=0, column=2)
        self.label_space5 = tk.Label(self.Frame_with_start_buttons, width=9, height=5, bg=color)
        self.label_space5.grid(row=0, column=4)

        # Buttons
        self.btn_add_car = tk.Button(self.Frame_with_start_buttons, text="Add car", command=self.insert_car,
                                     bg="#464646", fg="white")
        self.btn_add_customer = tk.Button(self.Frame_with_start_buttons, text="Add customer",
                                          command=self.insert_customer, bg="#464646", fg="white")
        self.btn_add_rental = tk.Button(self.Frame_with_start_buttons, text="Add rental", command=self.insert_rental,
                                        bg="#464646", fg="white")
        self.btn_add_car.grid(row=0, column=1, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_add_customer.grid(row=0, column=3, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_add_rental.grid(row=0, column=5, pady=5, padx=4, ipady=15, ipadx=25)

        self.btn_edit_car = tk.Button(self.Frame_with_start_buttons, text="Edit car",
                                      command=self.edit_id_car,
                                      bg="#464646", fg="white")
        self.btn_edit_customer = tk.Button(self.Frame_with_start_buttons, text="Edit customer",
                                           command=self.edit_id_customer, bg="#464646", fg="white")
        self.btn_edit_rental = tk.Button(self.Frame_with_start_buttons, text="Edit rental",
                                         command=self.edit_id_rental, bg="#464646", fg="white")
        self.btn_edit_car.grid(row=1, column=1, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_edit_customer.grid(row=1, column=3, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_edit_rental.grid(row=1, column=5, pady=5, padx=4, ipady=15, ipadx=25)

        self.btn_delete_car = tk.Button(self.Frame_with_start_buttons, text="Delete car",
                                        command=lambda: self.edit_id_car(delete=True), bg="#464646", fg="white")
        self.btn_delete_customer = tk.Button(self.Frame_with_start_buttons, text="Delete customer",
                                             command=lambda: self.edit_id_customer(delete=True), bg="#464646", fg="white")
        self.btn_delete_rental = tk.Button(self.Frame_with_start_buttons, text="Delete rental",
                                           command=lambda: self.edit_id_rental(delete=True), bg="#464646", fg="white")
        self.btn_delete_car.grid(row=2, column=1, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_delete_customer.grid(row=2, column=3, pady=5, padx=4, ipady=15, ipadx=25)
        self.btn_delete_rental.grid(row=2, column=5, pady=5, padx=4, ipady=15, ipadx=25)

        self.Frame_with_start_buttons.place(x=0, y=480)

        # Add Car
        # Entry
        self.Add_car = tk.Frame(self, bg=color)
        self.Frame_with_buttons = tk.Frame(self.Add_car, bg=color)

        # Labels
        self.label_add_car1 = tk.Label(self.Add_car, text="Car info", bg=color, fg="white")
        self.label_add_car2 = tk.Label(self.Add_car, text="ID: ", bg=color, fg="white")
        self.label_add_car3 = tk.Label(self.Add_car, text="Type: ", bg=color, fg="white")
        self.label_add_car4 = tk.Label(self.Add_car, text="Brand: ", bg=color, fg="white")
        self.label_add_car5 = tk.Label(self.Add_car, text="color: ", bg=color, fg="white")
        self.label_add_car6 = tk.Label(self.Add_car, text="Price_per_day: ", bg=color, fg="white")
        self.label_last_added_car = tk.Label(self, text=f"", bg=color, fg="white")
        self.label_add_car1.grid(row=0, column=1)
        self.label_add_car2.grid(row=1, column=0)
        self.label_add_car3.grid(row=2, column=0)
        self.label_add_car4.grid(row=3, column=0)
        self.label_add_car5.grid(row=4, column=0)
        self.label_add_car6.grid(row=5, column=0)

        # Entry's
        self.entry_message_car1 = tk.Entry(self.Add_car, textvariable=tk.IntVar())
        self.entry_message_car2 = tk.Entry(self.Add_car, textvariable=tk.StringVar())
        self.entry_message_car3 = tk.Entry(self.Add_car, textvariable=tk.StringVar())
        self.entry_message_car4 = tk.Entry(self.Add_car, textvariable=tk.StringVar())
        self.entry_message_car5 = tk.Entry(self.Add_car, textvariable=tk.StringVar())
        self.entry_message_car1.grid(row=1, column=1)
        self.entry_message_car2.grid(row=2, column=1)
        self.entry_message_car3.grid(row=3, column=1)
        self.entry_message_car4.grid(row=4, column=1)
        self.entry_message_car5.grid(row=5, column=1)

        # Buttons
        self.btn_add_car2 = tk.Button(self.Frame_with_buttons, text="Add car", command=self.add_car, bg="#464646",
                                      fg="white")
        self.cancel_car = tk.Button(self.Frame_with_buttons, text="Cancel", command=self.remove_all_in_add_car,
                                    bg="#464646", fg="white")
        self.btn_add_car2.grid(row=0, column=1, pady=5, padx=4)
        self.cancel_car.grid(row=0, column=0, pady=5, padx=4)
        self.Frame_with_buttons.grid(row=6, column=1, columnspan=2)

        # Add customer
        # Frame
        self.Add_customer = tk.Frame(self, bg=color)
        self.Frame_with_buttons_2 = tk.Frame(self.Add_customer, bg=color)
        # Label
        self.label_add_customer1 = tk.Label(self.Add_customer, text="Customer info", bg=color, fg="white")
        self.label_add_customer2 = tk.Label(self.Add_customer, text="Fullname: ", bg=color, fg="white")
        self.label_add_customer3 = tk.Label(self.Add_customer, text="Email: ", bg=color, fg="white")
        self.label_add_customer4 = tk.Label(self.Add_customer, text="Phone: ", bg=color, fg="white")
        self.label_last_added_customer = tk.Label(self, text=f"", bg=color, fg="white")
        self.label_space6 = tk.Label(self.Frame_with_buttons_2, width=1, height=2, bg=color)
        self.label_space6.grid(row=0, column=1)
        self.label_add_customer1.grid(row=0, column=1)
        self.label_add_customer2.grid(row=1, column=0, sticky=tk.E)
        self.label_add_customer3.grid(row=2, column=0, sticky=tk.E)
        self.label_add_customer4.grid(row=3, column=0, sticky=tk.E)

        # Entry's
        self.entry_message_customer1 = tk.Entry(self.Add_customer, textvariable=tk.StringVar())
        self.entry_message_customer2 = tk.Entry(self.Add_customer, textvariable=tk.StringVar())
        self.entry_message_customer3 = tk.Entry(self.Add_customer, textvariable=tk.StringVar())
        self.entry_message_customer1.grid(row=1, column=1)
        self.entry_message_customer2.grid(row=2, column=1)
        self.entry_message_customer3.grid(row=3, column=1)

        # Buttons
        self.cancel_customer = tk.Button(self.Frame_with_buttons_2, text="Cancel",
                                         command=self.remove_all_in_add_customer,
                                         bg="#464646", fg="white")
        self.btn_add_customer2 = tk.Button(self.Frame_with_buttons_2, text="Add customer", command=self.add_customer,
                                           bg="#464646", fg="white")
        self.btn_add_customer2.grid(row=0, column=2)
        self.cancel_customer.grid(row=0, column=0)
        self.Frame_with_buttons_2.grid(row=4, column=1, columnspan=2)

        # Rental
        # Frame
        self.Add_rental = tk.Frame(self, bg=color)
        self.Frame_with_buttons_3 = tk.Frame(self.Add_rental, bg=color)
        self.Frame_with_buttons_4 = tk.Frame(self.Add_rental, bg=color)

        # Labels
        self.label_add_rental1 = tk.Label(self.Add_rental, text="Rental info", bg=color, fg="white")
        self.label_add_rental2 = tk.Label(self.Frame_with_buttons_3, text="Start_time: ", bg=color, fg="white")
        self.label_add_rental3 = tk.Label(self.Frame_with_buttons_3, text="End_time: ", bg=color, fg="white")
        self.label_add_rental4 = tk.Label(self.Add_rental, text="Car_id: ", bg=color, fg="white")
        self.label_add_rental5 = tk.Label(self.Add_rental, text="Customer_id: ", bg=color, fg="white")
        self.label_last_added_rental = tk.Label(self, text=f"", bg=color, fg="white")
        self.label_add_rental1.grid(row=1, column=1, sticky=tk.W)
        self.label_add_rental2.grid(row=1, column=0, sticky=tk.E)
        self.label_add_rental3.grid(row=2, column=0, sticky=tk.E)
        self.label_add_rental4.grid(row=4, column=0, sticky=tk.E)
        self.label_add_rental5.grid(row=5, column=0, sticky=tk.E)
        self.label_date = tk.Label(self.Frame_with_buttons_3, text="Date", bg=color, fg="white")
        self.label_hour = tk.Label(self.Frame_with_buttons_3, text="Hour", bg=color, fg="white")
        self.label_min = tk.Label(self.Frame_with_buttons_3, text="Min", bg=color, fg="white")
        self.label_sec = tk.Label(self.Frame_with_buttons_3, text="Sec", bg=color, fg="white")
        self.label_date.grid(row=0, column=1, sticky=tk.W)
        self.label_hour.grid(row=0, column=2, sticky=tk.W)
        self.label_min.grid(row=0, column=3, sticky=tk.W)
        self.label_sec.grid(row=0, column=4, sticky=tk.W)

        # Entry
        self.entry_message_rental1 = tk.Entry(self.Add_rental, textvariable=tk.IntVar())
        self.entry_message_rental2 = tk.Entry(self.Add_rental, textvariable=tk.IntVar())
        self.entry_message_rental1.grid(row=4, column=1)
        self.entry_message_rental2.grid(row=5, column=1)

        # Buttons
        self.btn_add_rental2 = tk.Button(self.Frame_with_buttons_4, text="Add rental", command=self.add_rental,
                                         bg="#464646", fg="white")
        self.cancel_rental = tk.Button(self.Frame_with_buttons_4, text="Cancel", command=self.remove_all_in_add_rental,
                                       bg="#464646", fg="white")
        self.start_time = DateEntry(self.Frame_with_buttons_3, width=12, background='darkblue', foreground='white',
                                    borderwidth=2,
                                    date_pattern="yyyy-mm-dd", bg=color, fg="white")
        self.end_time = DateEntry(self.Frame_with_buttons_3, width=12, background='darkblue', foreground='white',
                                  borderwidth=2,
                                  date_pattern="yyyy-mm-dd", bg=color, fg="white")
        self.t_0_hour = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=24, format='%02.0f')
        self.t_0_min = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=60, format='%02.0f')
        self.t_0_sec = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=60, format='%02.0f')
        self.t_1_hour = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=24, format='%02.0f')
        self.t_1_min = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=60, format='%02.0f')
        self.t_1_sec = tk.Spinbox(self.Frame_with_buttons_3, width=2, from_=00, to=60, format='%02.0f')
        self.start_time.grid(row=1, column=1, sticky=tk.W)
        self.t_0_hour.grid(row=1, column=2, sticky=tk.W)
        self.t_0_min.grid(row=1, column=3, sticky=tk.W)
        self.t_0_sec.grid(row=1, column=4, sticky=tk.W)
        self.end_time.grid(row=2, column=1, sticky=tk.W)
        self.t_1_hour.grid(row=2, column=2, sticky=tk.W)
        self.t_1_min.grid(row=2, column=3, sticky=tk.W)
        self.t_1_sec.grid(row=2, column=4, sticky=tk.W)
        self.btn_add_rental2.grid(row=0, column=1)
        self.cancel_rental.grid(row=0, column=0)
        self.Frame_with_buttons_4.grid(row=6, column=1, columnspan=2)
        self.Frame_with_buttons_3.grid(row=2, column=0, columnspan=4, rowspan=2)

        # Frame
        self.Frame_for_car_tree = tk.Frame(self, bg=color)
        # Designing the tree-view.
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=3, bd=2, font=('Calibri', 11), background="white")
        style.configure("Treeview.Heading", font=('Calbri', 13, 'bold'))
        style.map("Treeview", background=[("selected", "#464646")])
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.my_tree = ttk.Treeview(self.Frame_for_car_tree, style="Treeview")
        self.my_tree.tag_configure('odd', background=color)
        self.my_tree.tag_configure('even', background=color)

        # Define our columns
        self.my_tree['columns'] = ('ID', 'Brand', 'Type', 'Color', "Price_per_day")
        self.my_tree.column("#0", width=0, stretch=tk.NO)
        self.my_tree.column("ID", anchor=tk.W, width=50)
        self.my_tree.column("Brand", anchor=tk.W, width=100)
        self.my_tree.column("Type", anchor=tk.W, width=100)
        self.my_tree.column("Color", anchor=tk.W, width=100)
        self.my_tree.column("Price_per_day", anchor=tk.W, width=140)
        # Create Headings
        self.my_tree.heading("ID", text="ID", anchor=tk.W)
        self.my_tree.heading("Brand", text="Brand", anchor=tk.W)
        self.my_tree.heading("Type", text="Type", anchor=tk.W)
        self.my_tree.heading("Color", text="Color", anchor=tk.W)
        self.my_tree.heading("Price_per_day", text="Price_per_day(kr)", anchor=tk.W)
        self.my_tree.pack()

        # Frame
        self.Frame_for_customer_tree = tk.Frame(self, bg=color)

        # Designing the tree-view.
        style = ttk.Style()
        self.my_tree1 = ttk.Treeview(self.Frame_for_customer_tree, style="Treeview")
        self.my_tree1.tag_configure('odd', background="#464646")
        self.my_tree1.tag_configure('even', background="#464646")

        # Define our columns
        self.my_tree1['columns'] = ('ID', 'Fullname', 'Email', 'Phone')
        self.my_tree1.column("#0", width=0, stretch=tk.NO)
        self.my_tree1.column("ID", anchor=tk.W, width=50)
        self.my_tree1.column("Fullname", anchor=tk.W, width=150)
        self.my_tree1.column("Email", anchor=tk.W, width=200)
        self.my_tree1.column("Phone", anchor=tk.W, width=150)
        # Create Headings
        self.my_tree1.heading("ID", text="ID", anchor=tk.W)
        self.my_tree1.heading("Fullname", text="Fullname", anchor=tk.W)
        self.my_tree1.heading("Email", text="Email", anchor=tk.W)
        self.my_tree1.heading("Phone", text="Phone", anchor=tk.W)
        self.my_tree1.pack()

        # Frame
        self.Frame_for_rental_tree = tk.Frame(self, bg=color)
        # Designing the tree-view.
        self.my_tree2 = ttk.Treeview(self.Frame_for_rental_tree, style="Treeview")
        self.my_tree2.tag_configure('odd', background='#f9cd86')
        self.my_tree2.tag_configure('even', background='#f9cd86')

        # Define our columns
        self.my_tree2['columns'] = ('Rental_id', 'Start_time', 'End_time', 'Price', 'Car_id', 'Customer_id')
        self.my_tree2.column("#0", width=0, stretch=tk.NO)
        self.my_tree2.column("Rental_id", anchor=tk.W, width=80)
        self.my_tree2.column("Start_time", anchor=tk.W, width=135)
        self.my_tree2.column("End_time", anchor=tk.W, width=135)
        self.my_tree2.column("Price", anchor=tk.W, width=100)
        self.my_tree2.column("Car_id", anchor=tk.W, width=100)
        self.my_tree2.column("Customer_id", anchor=tk.W, width=108)
        # Create Headings
        self.my_tree2.heading("Rental_id", text="Rental_id", anchor=tk.W)
        self.my_tree2.heading("Start_time", text="Start_time", anchor=tk.W)
        self.my_tree2.heading("End_time", text="End_time", anchor=tk.W)
        self.my_tree2.heading("Price", text="Price", anchor=tk.W)
        self.my_tree2.heading("Car_id", text="Car_id", anchor=tk.W)
        self.my_tree2.heading("Customer_id", text="Customer_id", anchor=tk.W)
        self.my_tree2.pack()

        # Error
        self.error_handler_rental = tk.Label(self.Add_rental, text=None, fg="red", bg=color)
        self.error_handler_car = tk.Label(self.Add_car, text=None, fg="red", bg=color)
        self.error_handler_customer = tk.Label(self.Add_customer, text=None, fg="red", bg=color)
        self.error_handler_gets = tk.Label(self.Frame_with_gets, text=None, fg="red", bg=color)
        self.error_handler_car2 = tk.Label(self.Frame_for_car_tree, text=None, fg="red", bg=color)
        self.error_handler_customer2 = tk.Label(self.Frame_for_customer_tree, text=None, fg="red", bg=color)
        self.error_handler_rental2 = tk.Label(self.Frame_for_rental_tree, text=None, fg="red", bg=color)

        # Extra buttons for edit
        self.btn_edit_car2 = tk.Button(self.Frame_for_car_tree, text="", bg="#464646", height=2, width=70,
                                       command=None)
        self.btn_edit_customer2 = tk.Button(self.Frame_for_customer_tree, text="", height=2, width=78,
                                            bg="#464646", command=None)
        self.btn_edit_rental2 = tk.Button(self.Frame_for_rental_tree, text="", height=2, width=94,
                                          bg="#464646", command=None)

    def delete_car(self):
        self.label_space10.place(x=0, y=400)
        try:
            Id = int(self.Select_Item_car_tree()[0])
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
            self.remove_all_in_add_car()
            self.Frame_for_car_tree.place_forget()
        else:
            if tk.messagebox.askquestion("Delete car", f"Are you sure you want to delete car with "
                                                       f"id: {Id}") == "yes":
                Car = car(delete=True, ID=Id)
                if "message" in Car:
                    self.error_handler_car2.config(text=Car['message'])
                    self.error_handler_car2.pack()
                else:
                    self.remove_all_in_add_car()
                    self.Frame_for_car_tree.place_forget()
            else:
                self.remove_all_in_add_car()
                self.Frame_for_car_tree.place_forget()

    def delete_customer(self):
        self.label_space10.place(x=0, y=400)
        try:
            Id = int(self.Select_Item_customer_tree()[0])
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
            self.remove_all_in_add_customer()
            self.Frame_for_customer_tree.place_forget()
        else:
            if tk.messagebox.askquestion("Delete customer", f"Are you sure you want to delete customer with "
                                                            f"id: {Id}") == "yes":
                Customer = customer(delete=True, ID=Id)
                if "message" in Customer:
                    self.error_handler_customer2.config(text=Customer['message'])
                    self.error_handler_customer2.pack()
                else:
                    self.remove_all_in_add_customer()
                    self.Frame_for_customer_tree.place_forget()
            else:
                self.remove_all_in_add_customer()
                self.Frame_for_customer_tree.place_forget()

    def delete_rental(self):
        self.label_space10.place(x=0, y=400)
        try:
            Id = int(self.Select_Item_rental_tree()[0])
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
            self.remove_all_in_add_rental()
            self.Frame_for_rental_tree.place_forget()
        else:
            if tk.messagebox.askquestion("Delete rental", f"Are you sure you want to delete rental with "
                                                          f"id: {Id}") == "yes":
                Rentals = rentals(delete=True, rental_id=Id)
                if "message" in Rentals:
                    self.error_handler_rental2.config(text=Rentals['message'])
                    self.error_handler_rental2.pack()
                else:
                    self.remove_all_in_add_customer()
                    self.Frame_for_rental_tree.place_forget()
            else:
                self.remove_all_in_add_rental()
                self.Frame_for_rental_tree.place_forget()

    def edit_id_car(self, delete=False):
        if delete:
            self.btn_edit_car2.config(text="Delete", bg="red", command=self.delete_car)
        else:
            self.btn_edit_car2.config(text="Edit", bg="#464646", command=lambda: self.insert_car(edit=True))
        self.label_space10.place(x=0, y=400)
        self.create_car_tree(All=True)
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        self.Frame_for_car_tree.place(x=50, y=440)

    def edit_id_customer(self, delete=False):
        if delete:
            self.btn_edit_customer2.config(text="Delete", bg="red", command=self.delete_customer)
        else:
            self.btn_edit_customer2.config(text="Edit", bg="#464646", command=lambda: self.insert_customer(edit=True))
        self.label_space10.place(x=0, y=400)
        self.create_customer_tree(All=True)
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        self.Frame_for_customer_tree.place(x=50, y=440)

    def edit_id_rental(self, delete=False):
        if delete:
            self.btn_edit_rental2.config(text="Delete", bg="red", command=self.delete_rental)
        else:
            self.btn_edit_rental2.config(text="Edit", bg="#464646", command=lambda: self.insert_rental(edit=True))
        self.label_space10.place(x=0, y=400)
        self.create_rental_tree(All=True)
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        self.Frame_for_rental_tree.place(x=50, y=440)

    def insert_car(self, edit=False):
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        if edit:
            if self.Select_Item_car_tree():
                self.entry_message_car1.grid_remove()
                self.label_add_car2.grid_remove()
                self.Frame_for_car_tree.place_forget()
                self.btn_add_car2.config(text="Edit car", command=self.edit_car)
                self.entry_message_car2.delete(0, tk.END)
                self.entry_message_car3.delete(0, tk.END)
                self.entry_message_car4.delete(0, tk.END)
                self.entry_message_car5.delete(0, tk.END)
                self.entry_message_car2.insert(0, self.Select_Item_car_tree()[1])
                self.entry_message_car3.insert(0, self.Select_Item_car_tree()[2])
                self.entry_message_car4.insert(0, self.Select_Item_car_tree()[3])
                self.entry_message_car5.insert(0, self.Select_Item_car_tree()[4])
                self.Add_car.place(x=170, y=450)
            else:
                self.Frame_for_car_tree.place_forget()
                self.remove_all_in_add_car()
        else:
            self.label_space10.place(x=0, y=400)
            self.btn_add_car2.config(text="Add car", command=self.add_car)
            self.Add_car.place(x=170, y=450)

    def insert_customer(self, edit=False):
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        if edit:
            if self.Select_Item_customer_tree():
                self.entry_message_customer1.delete(0, tk.END)
                self.entry_message_customer2.delete(0, tk.END)
                self.entry_message_customer3.delete(0, tk.END)
                self.entry_message_customer1.insert(0, self.Select_Item_customer_tree()[1])
                self.entry_message_customer2.insert(0, self.Select_Item_customer_tree()[2])
                self.entry_message_customer3.insert(0, self.Select_Item_customer_tree()[3])
                self.Frame_for_customer_tree.place_forget()
                self.btn_add_customer2.config(text="Edit customer", command=self.edit_customer)
                self.Add_customer.place(x=170, y=450)
            else:
                self.Frame_for_customer_tree.place_forget()
                self.remove_all_in_add_customer()
        else:
            self.label_space10.place(x=0, y=400)
            self.btn_add_customer2.config(text="Add customer", command=self.add_customer)
            self.Add_customer.place(x=170, y=430)

    def insert_rental(self, edit=False):
        self.label_last_added_car.place_forget()
        self.label_last_added_customer.place_forget()
        self.label_last_added_rental.place_forget()
        self.Frame_with_start_buttons.place_forget()
        if edit:
            if self.Select_Item_rental_tree():
                self.entry_message_rental1.delete(0, tk.END)
                self.entry_message_rental2.delete(0, tk.END)
                self.start_time.delete(0, tk.END)
                self.end_time.delete(0, tk.END)
                self.t_0_sec.delete(0, tk.END)
                self.t_0_min.delete(0, tk.END)
                self.t_0_hour.delete(0, tk.END)
                self.t_1_sec.delete(0, tk.END)
                self.t_1_min.delete(0, tk.END)
                self.t_1_hour.delete(0, tk.END)
                datetime_0 = self.Select_Item_rental_tree()[1].split("T")
                time_0 = datetime_0[1].split(":")
                datetime_1 = self.Select_Item_rental_tree()[2].split("T")
                time_1 = datetime_1[1].split(":")
                self.t_0_sec.insert(0, time_0[2])
                self.t_0_min.insert(0, time_0[1])
                self.t_0_hour.insert(0, time_0[0])
                self.t_1_sec.insert(0, time_1[2])
                self.t_1_min.insert(0, time_1[1])
                self.t_1_hour.insert(0, time_1[0])
                self.start_time.insert(0, datetime_0[0])
                self.end_time.insert(0, datetime_1[0])
                self.entry_message_rental1.insert(0, self.Select_Item_rental_tree()[4])
                self.entry_message_rental2.insert(0, self.Select_Item_rental_tree()[5])
                self.Frame_for_rental_tree.place_forget()
                self.btn_add_rental2.config(text="Edit rental", command=self.edit_rental)
                self.Add_rental.place(x=170, y=450)
            else:
                self.Frame_for_rental_tree.place_forget()
                self.remove_all_in_add_rental()
        else:
            self.label_space10.place(x=0, y=400)
            self.btn_add_rental2.config(text="Add rental", command=self.add_rental)
            self.Add_rental.place(x=170, y=450)

    def remove_all_in_add_car(self):
        self.label_space10.place_forget()
        self.Frame_for_tot_earned.place_forget()
        self.entry_message_car1.delete(0, "end")
        self.entry_message_car2.delete(0, "end")
        self.entry_message_car3.delete(0, "end")
        self.entry_message_car4.delete(0, "end")
        self.entry_message_car5.delete(0, "end")
        self.error_handler_car2.pack_forget()
        self.error_handler_car.grid_remove()
        self.Add_car.place_forget()
        self.Frame_with_start_buttons.place(x=0, y=480)
        self.label_last_added_customer.place(x=180, y=546)
        self.label_last_added_car.place(x=0, y=546)
        self.label_last_added_rental.place(x=390, y=546)

    def remove_all_in_add_customer(self):
        self.Frame_for_tot_earned.place_forget()
        self.entry_message_customer1.delete(0, "end")
        self.entry_message_customer2.delete(0, "end")
        self.entry_message_customer3.delete(0, "end")
        self.error_handler_customer.grid_remove()
        self.error_handler_customer2.pack_forget()
        self.Add_customer.place_forget()
        self.label_space10.place_forget()
        self.Frame_with_start_buttons.place(x=0, y=480)
        self.label_last_added_customer.place(x=180, y=546)
        self.label_last_added_car.place(x=0, y=546)
        self.label_last_added_rental.place(x=390, y=546)

    def remove_all_in_add_rental(self):
        self.Frame_for_tot_earned.place_forget()
        self.start_time.delete(0, 'end')
        self.t_0_hour.delete(0, 'end')
        self.error_handler_rental2.pack_forget()
        self.t_0_min.delete(0, 'end')
        self.t_0_sec.delete(0, 'end')
        self.t_1_hour.delete(0, 'end')
        self.t_1_min.delete(0, 'end')
        self.t_1_sec.delete(0, 'end')
        self.end_time.delete(0, 'end')
        self.label_space10.place_forget()

        self.entry_message_rental1.delete(0, 'end')
        self.entry_message_rental2.delete(0, 'end')
        self.error_handler_rental.grid_remove()
        self.error_handler_rental.grid_remove()
        self.Add_rental.place_forget()
        self.Frame_with_start_buttons.place(x=0, y=480)
        self.label_last_added_customer.place(x=180, y=546)
        self.label_last_added_car.place(x=0, y=546)
        self.label_last_added_rental.place(x=390, y=546)

    def add_customer(self):
        new_customer = {
            "fullname": self.entry_message_customer1.get(),
            "email": self.entry_message_customer2.get(),
            "phone": self.entry_message_customer3.get()
        }
        # Sending post request with json data.
        try:
            Customer = customer(post=True, json=new_customer)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Customer:
                self.error_handler_customer.config(text=Customer['message'])
                self.error_handler_customer.grid(row=10, column=1, columnspan=2)
            else:
                self.remove_all_in_add_customer()
                self.label_last_added_customer.config(text=f"Last added customer with id: {Customer['id']}")
                self.label_last_added_customer.place(x=180, y=546)

    def add_car(self):
        new_car = {
            "id": int(self.entry_message_car1.get()),
            "type": self.entry_message_car2.get(),
            "brand": self.entry_message_car3.get(),
            "color": self.entry_message_car4.get(),
            "price_per_day": self.entry_message_car5.get()
        }
        try:
            Car = car(post=True, json=new_car)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Car:
                self.error_handler_car.config(text=Car['message'])
                self.error_handler_car.grid(row=10, column=1, columnspan=2)
            else:
                self.remove_all_in_add_car()
                self.label_last_added_car.config(text=f"Last car added with id: {Car['id']}")
                self.label_last_added_car.place(x=0, y=546)

    def add_rental(self):
        new_rental = {
            "start_time": f"{self.start_time.get()} {self.t_0_hour.get()}:{self.t_0_min.get()}:{self.t_0_sec.get()}",
            "end_time": f"{self.end_time.get()} {self.t_1_hour.get()}:{self.t_1_min.get()}:{self.t_1_sec.get()}",
            "car_id": int(self.entry_message_rental1.get()),
            "customer_id": int(self.entry_message_rental2.get())
        }
        try:
            Rental = rentals(post=True, json=new_rental)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Rental:
                self.error_handler_rental.config(text=Rental['message'])
                self.error_handler_rental.grid(row=7, column=1, columnspan=2)
            else:
                self.remove_all_in_add_rental()
                self.label_last_added_rental.config(text=f"Last rental added with rental id: {Rental['rental_id']}")
                self.label_last_added_rental.place(x=390, y=546)

    def Select_Item_car_tree(self):
        Car = self.my_tree.focus()
        return self.my_tree.item(Car)['values']

    def Select_Item_customer_tree(self):
        Customer = self.my_tree1.focus()
        return self.my_tree1.item(Customer)['values']

    def Select_Item_rental_tree(self):
        Rental = self.my_tree2.focus()
        return self.my_tree2.item(Rental)['values']

    def edit_car(self):
        new_car = {
            "id": int(self.Select_Item_car_tree()[0]),
            "type": self.entry_message_car2.get(),
            "brand": self.entry_message_car3.get(),
            "color": self.entry_message_car4.get(),
            "price_per_day": self.entry_message_car5.get()
        }
        try:
            Car = car(put=True, json=new_car)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Car:
                self.error_handler_car.config(text=Car["message"])
                self.error_handler_car.grid(row=7, column=1, columnspan=2)
            else:
                self.remove_all_in_add_car()
                self.entry_message_car1.grid(row=1, column=1)
                self.label_add_car2.grid(row=1, column=0)
                self.label_last_added_car.config(text=f"Last car edited with id: {Car['id']}")
                self.label_last_added_car.place(x=0, y=546)

    def edit_customer(self):
        new_customer = {
            "id": int(self.Select_Item_customer_tree()[0]),
            "fullname": self.entry_message_customer1.get(),
            "email": self.entry_message_customer2.get(),
            "phone": self.entry_message_customer3.get()
        }
        try:
            Customer = customer(put=True, json=new_customer)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Customer:
                self.error_handler_customer.config(text=Customer['message'])
                self.error_handler_customer.grid(row=10, column=1, columnspan=2)
            else:
                self.remove_all_in_add_customer()
                self.label_last_added_customer.config(text=f"Last edited customer with id: {Customer['id']}")
                self.label_last_added_customer.place(x=180, y=546)

    def edit_rental(self):
        new_rental = {
            "rental_id": int(self.Select_Item_rental_tree()[0]),
            "start_time": f"{self.start_time.get()} {self.t_0_hour.get()}:{self.t_0_min.get()}:{self.t_0_sec.get()}",
            "end_time": f"{self.end_time.get()} {self.t_1_hour.get()}:{self.t_1_min.get()}:{self.t_1_sec.get()}",
            "car_id": int(self.entry_message_rental1.get()),
            "customer_id": int(self.entry_message_rental2.get())
        }
        try:
            Rental = rentals(put=True, json=new_rental)
        except requests.exceptions.ConnectionError:
            tk.messagebox.showerror("Connection error", "Failed to connect to server")
        except Exception as e:
            print(e)
        else:
            if "message" in Rental:
                self.error_handler_rental.config(text=Rental['message'])
                self.error_handler_rental.grid(row=7, column=1, columnspan=2)
            else:
                self.remove_all_in_add_rental()
                self.label_last_added_rental.config(text=f"Last edited with rental id: {Rental['rental_id']}")
                self.label_last_added_rental.place(x=390, y=546)

    def create_car_tree(self, All=False):
        if All:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_car2.pack_forget()
            self.my_tree.delete(*self.my_tree.get_children())
            self.btn_edit_car2.pack(expand=True)
            self.insert_tree(Car=True)
        else:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_car2.pack_forget()
            self.Add_customer.place_forget()
            self.Add_car.place_forget()
            self.Add_rental.place_forget()
            self.Frame_with_start_buttons.place(x=0, y=480)
            self.btn_edit_car2.pack_forget()
            self.Frame_for_car_tree.place_forget()
            self.Frame_for_customer_tree.place_forget()
            self.Frame_for_rental_tree.place_forget()
            self.my_tree.delete(*self.my_tree.get_children())
            self.Frame_for_car_tree.place(x=600, y=100)
            if self.clicked.get() == "id":
                self.insert_tree(Car=True, ID_Car=True)
            elif self.clicked.get() == 'brand':
                self.insert_tree(Car=True, Brand=True)
            elif self.clicked.get() == 'type':
                self.insert_tree(Car=True, Type=True)
            elif self.clicked.get() == 'color':
                self.insert_tree(Car=True, Color=True)
            elif self.clicked.get() == "all":
                self.insert_tree(Car=True)
            elif self.clicked.get() == "total earned":
                self.insert_tree(Car=True, Tot_earned=True)
            else:
                return -1

    def create_customer_tree(self, All=False):
        if All:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_customer2.pack_forget()
            self.my_tree1.delete(*self.my_tree1.get_children())
            self.btn_edit_customer2.pack()
            self.insert_tree(Customer=True)
        else:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_customer2.pack_forget()
            self.Frame_with_start_buttons.place(x=0, y=480)
            self.Add_customer.place_forget()
            self.Add_car.place_forget()
            self.Add_rental.place_forget()
            self.btn_edit_customer2.pack_forget()
            self.Frame_for_car_tree.place_forget()
            self.Frame_for_rental_tree.place_forget()
            self.Frame_for_customer_tree.place_forget()
            self.my_tree1.delete(*self.my_tree1.get_children())
            self.Frame_for_customer_tree.place(x=600, y=100)
            if self.clicked2.get() == "id":
                self.insert_tree(Customer=True, ID_Customer=True)
            elif self.clicked2.get() == "fullname":
                self.insert_tree(Customer=True, Fullname=True)
            elif self.clicked2.get() == "email":
                self.insert_tree(Customer=True, Email=True)
            elif self.clicked2.get() == "phone":
                self.insert_tree(Customer=True, Phone=True)
            elif self.clicked2.get() == "all":
                self.insert_tree(Customer=True)
            else:
                return -1

    def create_rental_tree(self, All=False):
        if All:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_rental2.pack_forget()
            self.my_tree2.delete(*self.my_tree2.get_children())
            self.btn_edit_rental2.pack()
            self.insert_tree(Rentals=True)
        else:
            self.Frame_for_tot_earned.place_forget()
            self.error_handler_rental2.pack_forget()
            self.Add_customer.place_forget()
            self.Add_car.place_forget()
            self.Add_rental.place_forget()
            self.Frame_with_start_buttons.place(x=0, y=480)
            self.btn_edit_rental2.pack_forget()
            self.Frame_for_car_tree.place_forget()
            self.Frame_for_customer_tree.place_forget()
            self.Frame_for_rental_tree.place_forget()
            self.my_tree2.delete(*self.my_tree2.get_children())
            self.Frame_for_rental_tree.place(x=600, y=100)
            if self.clicked3.get() == "rental_id":
                self.insert_tree(Rentals=True, Rental_id=True)
            elif self.clicked3.get() == "car_id":
                self.insert_tree(Rentals=True, ID_Car=True)
            elif self.clicked3.get() == "customer_id":
                self.insert_tree(Rentals=True, ID_Customer=True)
            elif (self.clicked3.get() == "all") or All:
                self.insert_tree(Rentals=True)
            else:
                return -1

    def insert_tree(self, Car=False, Customer=False, Rentals=False, ID_Car=False, ID_Customer=False, Rental_id=False,
                    Brand=False, Type=False, Color=False, Fullname=False, Email=False, Phone=False, Tot_earned=False):
        if Car:
            if ID_Car:
                try:
                    data = car(get=True, ID=int(self.entry_message_car.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in data:
                        self.Frame_for_car_tree.place_forget()
                        self.error_handler_gets.config(text=data["message"])
                        self.error_handler_gets.grid(row=2, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        self.my_tree.insert(parent='', index='end', value=(data['id'], data['brand'], data['type'],
                                                                           data['color'], data['price_per_day']))
            elif Brand:
                try:
                    Data = car(get=True, brand=self.entry_message_car.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_car_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=2, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree.insert(parent='', index='end', value=(data['id'], data['brand'], data['type'],
                                                                               data['color'], data['price_per_day']))
            elif Type:
                try:
                    Data = car(get=True, Type=self.entry_message_car.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_car_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=2, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree.insert(parent='', index='end', value=(data['id'], data['brand'], data['type'],
                                                                               data['color'], data['price_per_day']))

            elif Color:
                try:
                    Data = car(get=True, color=self.entry_message_car.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_car_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=2, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree.insert(parent='', index='end', value=(data['id'], data['brand'], data['type'],
                                                                               data['color'], data['price_per_day']))
            elif Tot_earned:
                try:
                    Data = car(get=True, tot_price_ID=int(self.entry_message_car.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_car_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=2, column=2, columnspan=2)
                    else:
                        self.label_tot_earnings.config(text=f"{Data['tot_price']}kr profit")
                        self.Frame_for_tot_earned.place(x=700, y=120)
                        self.Frame_for_car_tree.place_forget()

            else:
                try:
                    Data = car()
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    for data in Data:
                        self.my_tree.insert(parent='', index='end', value=(data['id'], data['brand'], data['type'],
                                                                           data['color'], data['price_per_day']))
        elif Customer:
            if ID_Customer:
                try:
                    Data = customer(get=True, ID=int(self.entry_message_customer.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_customer_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=12, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        self.my_tree1.insert(parent='', index='end', value=(Data['id'], Data['fullname'], Data['email'],
                                                                            Data['phone']))
            elif Fullname:
                try:
                    Data = customer(get=True, fullname=self.entry_message_customer.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_customer_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=12, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree1.insert(parent='', index='end', value=(data['id'], data['fullname'],
                                                                                data['email'], data['phone']))
            elif Email:
                try:
                    Data = customer(get=True, email=self.entry_message_customer.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_customer_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=12, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree1.insert(parent='', index='end', value=(data['id'], data['fullname'],
                                                                                data['email'], data['phone']))
            elif Phone:
                try:
                    Data = customer(get=True, phone=self.entry_message_customer.get())
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_customer_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=12, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree1.insert(parent='', index='end', value=(data['id'], data['fullname'],
                                                                                data['email'], data['phone']))
            else:
                try:
                    Data = customer()
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    for data in Data:
                        self.my_tree1.insert(parent='', index='end', value=(data['id'], data['fullname'], data['email'],
                                                                            data['phone']))
        elif Rentals:
            if Rental_id:
                try:
                    Data = rentals(get=True, rental_id=int(self.entry_message_rental.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_rental_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=17, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        self.my_tree2.insert(parent='', index='end', value=(Data['rental_id'], Data['start_time'],
                                                                            Data['end_time'], Data['price'],
                                                                            Data['car_id'], Data['customer_id']))
            elif ID_Car:
                try:
                    Data = rentals(get=True, car_id=int(self.entry_message_rental.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_rental_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=17, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree2.insert(parent='', index='end', value=(data['rental_id'], data['start_time'],
                                                                                data['end_time'], data['price'],
                                                                                data['car_id'], data['customer_id']))
            elif ID_Customer:
                try:
                    Data = rentals(get=True, customer_id=int(self.entry_message_rental.get()))
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    if "message" in Data:
                        self.Frame_for_rental_tree.place_forget()
                        self.error_handler_gets.config(text=Data["message"])
                        self.error_handler_gets.grid(row=17, column=2, columnspan=2)
                    else:
                        self.error_handler_gets.grid_remove()
                        for data in Data:
                            self.my_tree2.insert(parent='', index='end', value=(data['rental_id'], data['start_time'],
                                                                                data['end_time'], data['price'],
                                                                                data['car_id'], data['customer_id']))
            else:
                try:
                    Data = rentals()
                except requests.exceptions.ConnectionError:
                    tk.messagebox.showerror("Connection error", "Failed to connect to server")
                except Exception as e:
                    print(e)
                else:
                    for data in Data:
                        self.my_tree2.insert(parent='', index='end', value=(data['rental_id'], data['start_time'],
                                                                            data['end_time'], data['price'],
                                                                            data['car_id'],
                                                                            data['customer_id']))
        else:
            return


class file(tk.Frame):
    def configure_menu(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.master.destroy)

        menubar.add_cascade(label='File', menu=file_menu)
        self.master.config(menu=menubar)


def main():
    # Creating the Tkinter main window.
    root = tk.Tk()
    width = 1300
    height = 750
    root.geometry("%dx%d" % (width, height))
    photo = tk.PhotoImage(file='Pictures/car.png')
    root.iconphoto(False, photo)
    root.title("Gabriel's rental company")
    root.resizable(0, 0)

    # Create window object
    app = MainApplication(master=root)
    # Run the main loop
    app.mainloop()


if __name__ == '__main__':
    main()
