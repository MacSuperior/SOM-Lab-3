from enum import IntEnum

class UIClass(IntEnum):
	FirstClass = 1
	SecondClass = 2

class UIWay(IntEnum):
	OneWay = 1
	Return = 2

class UIDiscount(IntEnum):
	NoDiscount = 0
	TwentyDiscount = 20
	FortyDiscount = 40

class UIPayment(IntEnum):
	DebitCard = 1
	CreditCard = 2
	Cash= 3

