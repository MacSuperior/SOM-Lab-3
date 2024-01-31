from tariefeenheden import Tariefeenheden
import tkinter as tk
from ui_info import UIPayment, UIClass, UIWay, UIDiscount, UIPayment, UIInfo
from ticket import Ticket
from payment import Payment
from ticket_price_calculator import TicketPriceCalculator
from sale import Sale

class UI(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.total_price = 0.0
		self.tickets = []
		self.widgets()

	def widgets(self):
		self.master.title("Ticket machine")
		menubar = tk.Menu(self.master)
		self.master.config(menu=menubar)

		fileMenu = tk.Menu(menubar)
		fileMenu.add_command(label="Exit", command=self.on_exit)
		menubar.add_cascade(label="File", menu=fileMenu)

		all_stations = Tariefeenheden.get_stations()

		stations_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		stations_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
	
		tk.Label(stations_frame, text="From station:").grid(row=0, padx=5, sticky=tk.W)
		self.from_station = tk.StringVar(value=all_stations[0])
		tk.OptionMenu(stations_frame, self.from_station, *all_stations).grid(row=0, column=1, padx=5, sticky=tk.W)

		tk.Label(stations_frame, text="To station:").grid(row=0, column=2, padx=5, sticky=tk.W)
		self.to_station = tk.StringVar(value=all_stations[0])
		tk.OptionMenu(stations_frame, self.to_station, *all_stations).grid(row=0, column=3, padx=5, sticky=tk.W)

		ticket_options_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		ticket_options_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

		tk.Label(ticket_options_frame, text="Travel class:").grid(row=0, column=0, padx=5, sticky=tk.W)
		self.travel_class = tk.IntVar(value=UIClass.SecondClass.value)
		tk.Radiobutton(ticket_options_frame, text="First class", variable=self.travel_class, value=UIClass.FirstClass.value).grid(row=0, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="Second class", variable=self.travel_class, value=UIClass.SecondClass.value).grid(row=0, column=2, padx=5, sticky=tk.W)

		tk.Label(ticket_options_frame, text="Way:").grid(row=1, column=0, padx=5, sticky=tk.W)
		self.way = tk.IntVar(value=UIWay.OneWay.value)
		tk.Radiobutton(ticket_options_frame, text="One-way", variable=self.way, value=UIWay.OneWay.value).grid(row=1, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="Return", variable=self.way, value=UIWay.Return.value).grid(row=1, column=2, padx=5, sticky=tk.W)

		tk.Label(ticket_options_frame, text="Travel Date").grid(row=1, column=0, padx=5, sticky=tk.W)
		self.date = ...
		

		tk.Label(ticket_options_frame, text="Discount:").grid(row=2, column=0, padx=5, sticky=tk.W)
		self.discount = tk.IntVar(value=UIDiscount.NoDiscount.value)
		tk.Radiobutton(ticket_options_frame, text="No discount", variable=self.discount, value=UIDiscount.NoDiscount.value).grid(row=2, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="20% discount", variable=self.discount, value=UIDiscount.TwentyDiscount.value).grid(row=2, column=2, padx=5, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="40% discount", variable=self.discount, value=UIDiscount.FortyDiscount.value).grid(row=2, column=3, padx=5, sticky=tk.W)

		payment_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		payment_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

		tk.Label(payment_frame, text="Payment:").grid(row=0, column=0, padx=5, sticky=tk.W)
		self.payment = tk.IntVar(value=UIPayment.Cash.value)
		tk.Radiobutton(payment_frame, text="Cash", variable=self.payment, value=UIPayment.Cash.value).grid(row=0, column=1, padx=5, sticky=tk.W)
		tk.Radiobutton(payment_frame, text="Credit Card", variable=self.payment, value=UIPayment.CreditCard.value).grid(row=0, column=2, padx=5, sticky=tk.W)
		tk.Radiobutton(payment_frame, text="Debit Card", variable=self.payment, value=UIPayment.DebitCard.value).grid(row=0, column=3, padx=5, sticky=tk.W)

		tk.Button(self.master, text="Add Ticket", command=self.on_click_add_ticket).pack(side=tk.LEFT, ipadx=10, padx=10, pady=10)
		self.ticket_price_label = tk.Label(self.master, text=f"Total price: {self.total_price}")
		self.ticket_price_label.pack(side=tk.RIGHT, ipadx=10, padx=10, pady=10)

		tk.Button(self.master, text="Pay", command=self.on_click_pay).pack(side=tk.BOTTOM, ipadx=10, padx=10, pady=10)

		self.pack(fill=tk.BOTH, expand=1)

	def on_click_pay(self):
		Sale.handle_payment(self.total_price, self.payment.get())
	
	def create_ticket(self):
		return Ticket(origin=self.from_station.get(),
				  		destination=self.to_station.get(),
						travel_class=self.travel_class.get(),
						journey_type=self.way.get(),
						valid_date=0,
						price=0,
						discount=self.discount.get())

	def spawn_ticket(self, ticket: Ticket):
		ticket_frame = tk.Frame(self.master)
		ticket_frame.pack()

		label_text = f"Ticket: {ticket.origin} to {ticket.destination}, {ticket.travel_class}e class {ticket.price} EUR"
		ticket_label = tk.Label(ticket_frame, text=label_text)
		ticket_label.pack(side=tk.LEFT)

		delete_button = tk.Button(ticket_frame, text="Delete", command=lambda frame=ticket_frame: self.on_click_delete_ticket(frame, ticket))
		delete_button.pack(side=tk.RIGHT)

	def add_ticket_to_total(self, ticket: Ticket):
		self.total_price += ticket.price
		self.total_price = round(self.total_price, 2)
		self.tickets.append(ticket)

	def on_click_add_ticket(self):
		ticket = self.create_ticket()
		ticket.price =  TicketPriceCalculator.get_price(ticket)
		self.add_ticket_to_total(ticket)
		self.spawn_ticket(ticket)

		self.ticket_price_label.config(text=f"Total price: {self.total_price}")


	def on_click_delete_ticket(self, ticket_frame, ticket):
		self.tickets.remove(ticket)
		self.total_price -= ticket.price
		ticket_frame.destroy()

		self.ticket_price_label.config(text=f"Total price: {self.total_price}")

	def get_ui_info(self) -> UIInfo:
		return UIInfo(from_station=self.from_station.get(),
			to_station=self.to_station.get(),
			travel_class=self.travel_class.get(),
			way=self.way.get(),
			discount=self.discount.get(),
			payment=self.payment.get())

	def on_exit(self):
		self.quit()

#endregion

def main():
	root = tk.Tk()
	UI(root)
	root.mainloop()

if __name__ == '__main__':
	main()

#TODO: Add date to ticket