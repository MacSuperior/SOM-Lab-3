import tkinter as tk
from sale import Sale
from ticket import Ticket
from tariefeenheden import Tariefeenheden
from ui_info import UIPayment, UIClass, UIWay, UIDiscount, UIPayment

class UI(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.sale = Sale(self)
		self.widgets()
		self.update_checkbox()
		

	def widgets(self):
		self.master.title("Ticket machine")
		menubar = tk.Menu(self.master)
		self.master.config(menu=menubar)

		fileMenu = tk.Menu(menubar)
		fileMenu.add_command(label="Exit", command=self.on_exit)
		menubar.add_cascade(label="File", menu=fileMenu)
		font_style = ("Arial", 17)

		all_stations = Tariefeenheden.get_stations()

		stations_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		stations_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

		self.last_from = all_stations[0]
		self.last_to = all_stations[1]
		tk.Label(stations_frame, text="From station:", font=font_style).grid(row=0, padx=5, sticky=tk.W)
		self.from_station = tk.StringVar(value=all_stations[0])
		self.from_station.trace('w', self.update_menus)
		self.from_station_menu = tk.OptionMenu(stations_frame, self.from_station, *all_stations)
		self.from_station_menu.grid(row=0, column=1, padx=5, sticky=tk.W)

		tk.Label(stations_frame, text="To station:", font=font_style).grid(row=0, column=2, padx=5, sticky=tk.W)
		self.to_station = tk.StringVar(value=all_stations[1])
		self.to_station.trace('w', self.update_menus)
		self.to_station_menu = tk.OptionMenu(stations_frame, self.to_station, *all_stations)
		self.to_station_menu.grid(row=0, column=3, padx=5, sticky=tk.W)

		ticket_options_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		ticket_options_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

		tk.Label(ticket_options_frame, text="Travel class:", font=font_style).grid(row=0, column=0, padx=5, sticky=tk.W)
		self.travel_class = tk.IntVar(value=UIClass.second_class.value)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="First class", variable=self.travel_class, value=UIClass.first_class.value).grid(row=0, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="Second class", variable=self.travel_class, value=UIClass.second_class.value).grid(row=0, column=2, padx=5, sticky=tk.W)

		tk.Label(ticket_options_frame, font=font_style, text="Way:").grid(row=1, column=0, padx=5, sticky=tk.W)

		self.way = tk.IntVar(value=UIWay.single_ticket.value)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="One-way", variable=self.way, value=UIWay.single_ticket.value, command=self.update_checkbox).grid(row=1, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="Return", variable=self.way, value=UIWay.return_ticket.value, command=self.update_checkbox).grid(row=1, column=2, padx=5, sticky=tk.W)

		tk.Label(ticket_options_frame, font=font_style, text="Discount:").grid(row=2, column=0, padx=5, sticky=tk.W)
		self.discount = tk.IntVar(value=UIDiscount.no_discount.value)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="No discount", variable=self.discount, value=UIDiscount.no_discount.value).grid(row=2, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="20% discount", variable=self.discount, value=UIDiscount.twenty_discount.value).grid(row=2, column=2, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="40% discount", variable=self.discount, value=UIDiscount.forty_discount.value).grid(row=2, column=3, padx=5, sticky=tk.W)


		self.use_different_date = tk.BooleanVar(value=False)
		self.use_different_date_checkbox = tk.Checkbutton(ticket_options_frame, font=font_style, text="I want to use my ticket another date", variable= self.use_different_date, onvalue=True, offvalue=False, state=tk.DISABLED)
		self.use_different_date_checkbox.grid(row=3, column=0, padx=5, pady=10, sticky=tk.W)
		
		tk.Button(ticket_options_frame, text="Add Ticket", command=self.on_click_add_ticket, height=3).grid(row=5, column=0, padx=5, pady=10, sticky=tk.W)


		tk.Label(ticket_options_frame, text="Payment:", font=font_style).grid(row=6, column=3, padx=5, sticky=tk.E)
		self.payment = tk.IntVar(value=UIPayment.cash.value)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="Cash", variable=self.payment, value=UIPayment.cash.value).grid(row=6, column=4, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="Credit Card", variable=self.payment, value=UIPayment.credit_card.value).grid(row=6, column=5, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, font=font_style, text="Debit Card", variable=self.payment, value=UIPayment.debit_card.value).grid(row=6, column=6, padx=5, sticky=tk.W)


		tk.Button(self.master, text="Pay", command=self.on_click_pay, width=20, height=5, font=font_style).pack(side=tk.RIGHT, ipadx=10, padx=10, pady=1, anchor='se')
		self.ticket_price_label = tk.Label(self.master, text=f"€{self.sale.total_price}", font=("Arial", 25))
		self.ticket_price_label.pack(side=tk.RIGHT, ipadx=10, padx=10, pady=1, anchor='se')


		self.canvas = tk.Canvas(self.master)
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		self.scrollbar_frame = tk.Frame(self.master)
		self.scrollbar_frame.pack(side=tk.LEFT, fill='y')

		scrollbar = tk.Scrollbar(self.scrollbar_frame, orient="vertical", command=self.canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')

		self.canvas.configure(yscrollcommand=scrollbar.set)
		self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

		self.ticket_frame = tk.Frame(self.canvas)
		self.canvas.create_window((0, 0), window=self.ticket_frame, anchor="nw")

		# Initially hide the scrollbar
		self.scrollbar_frame.pack_forget()
	

		self.pack(fill=tk.BOTH, expand=1)

	def update_menus(self, *args):
		selected_from = self.from_station.get()
		selected_to = self.to_station.get()

		for option in Tariefeenheden.get_stations():
			self.from_station_menu['menu'].entryconfigure(option, state='normal')
			self.to_station_menu['menu'].entryconfigure(option, state='normal')

		self.from_station_menu['menu'].entryconfigure(selected_to, state='disabled')
		self.to_station_menu['menu'].entryconfigure(selected_from, state='disabled')


	def on_click_pay(self):
		Sale.handle_payment(self.sale.total_price, self.payment.get())

	def update_checkbox(self):
		if self.way.get() == UIWay.return_ticket.value:
			self.use_different_date.set(False)
			self.use_different_date_checkbox.config(state=tk.DISABLED)
		else:
			self.use_different_date_checkbox.config(state=tk.NORMAL)

	def spawn_ticket_in_ui(self, ticket: Ticket):
		ticket_frame = tk.Frame(self.ticket_frame)
		ticket_frame.pack()
		get_ticket_type = lambda x: "Return" if x.journey_type == UIWay.return_ticket else "Single"
		get_date = lambda x: x.valid_date if x.valid_date is not None else "No date"
		get_travel_class = lambda x: f'{x.travel_class}nd class' if x.travel_class == UIClass.second_class else f'{x.travel_class}st class'

		label_text = f"{get_date(ticket)} {get_travel_class(ticket)} {get_ticket_type(ticket)} Ticket: {ticket.origin} \u2192 {ticket.destination}  {ticket.price} EUR"
		ticket_label = tk.Label(ticket_frame, text=label_text, font=("Arial", 20))
		ticket_label.pack(side=tk.LEFT)

		delete_button = tk.Button(ticket_frame, text="Delete", command=lambda frame=ticket_frame: self.on_click_delete_ticket(frame, ticket), height=2)
		delete_button.pack(side=tk.RIGHT)
		self.ticket_price_label.config(text=f"Total price: {self.sale.total_price}")

		if self.ticket_frame.winfo_height() > self.canvas.winfo_height():
			self.scrollbar_frame.pack()
		else:
			self.scrollbar_frame.pack_forget()


	def on_click_add_ticket(self):
		ticket = self.sale.create_ticket()
		self.sale.add_ticket_to_total(ticket)
		self.spawn_ticket_in_ui(ticket)


	def on_click_delete_ticket(self, ticket_frame, ticket):
		self.sale.delete_ticket_from_total(ticket)
		ticket_frame.destroy()
		self.ticket_price_label.config(text=f"Total price: {self.sale.total_price}")


	def on_exit(self):
		self.quit()


def main():
	root = tk.Tk()
	root.attributes('-fullscreen', True)
	UI(root)
	root.mainloop()

if __name__ == '__main__':
	main()

