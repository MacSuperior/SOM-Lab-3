from enum import IntEnum

class UIClass(IntEnum):
	first_class = 1
	second_class = 2

class UIWay(IntEnum):
	single_ticket = 1
	return_ticket = 2

class UIDiscount(IntEnum):
	no_discount = 0
	twenty_discount = 20
	forty_discount = 40

class UIPayment(IntEnum):
	debit_card = 1
	credit_card = 2
	cash= 3

