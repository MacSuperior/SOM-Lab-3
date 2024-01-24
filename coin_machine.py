from tkinter import messagebox
from payment import Payment

class IKEAMyntAtare2000(Payment):

	def starta(self):
		messagebox.showinfo(message = "Välkommen till IKEA Mynt Ätare 2000")

	def stoppa(self):
		messagebox.showinfo(message = "Hejdå!")
		
	def betala(self, pris: int):
		messagebox.showinfo(message = f"{pris} cent")

	def handle_payment(self, price: int):
		self.starta()
		self.betala(int(round(price * 100)))
		self.stoppa()