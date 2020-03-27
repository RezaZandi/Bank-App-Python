class Transaction:
	def __init__(self):
		self.name = ''
		self.amount = 0.0
		self.type = ''

class Account:
	def __init__(self, name=''):
		self.name = name
		self.ledger = []

	def newtransaction(self, name, amount, type):
		transaction = Transaction()
		transaction.name = name
		transaction.amount = amount
		transaction.type = ''
		self.ledger.append(transaction)

	def getbalance(self):
		balance = 0.0
		for transaction in self.ledger:
			balance += transaction.amount
			return balance

# Within your main program somewhere.
myaccount = Account()

# get transaction data from user or file
name = 'cash'
amount = 20.0
type = 'deposite'
myaccount.newtransaction(name,amount,type)



name = 'cash'
amount = 10.0
type = 'withdrawl'
myaccount.newtransaction('cash',10,'withdrawl')
print(myaccount.getbalance())

for i in myaccount.ledger:
	print (i.amount)





