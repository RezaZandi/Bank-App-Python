

class Account(object):

	def __init__(self,user_name,email,account_type,balance,account_number):

		
		self.user_name = user_name
		self.email = email
		self.account_type = account_type
		self.balance = balance
		self.account_number = account_number



	def print_balance(self):

		print("\nAccount bala is "+ str(self.balance))
		return 

	def new_balance(self):
		print("\nThe new account balance is: " + str(self.balance))


	def to_string(self):

		print("\nUsername: " + self.user_name + "\n\nEmail: " + self.email + "\n\nAccount type: " + (self.account_type) + 
			"\n\nYour account balance is:" + str(self.balance) +"\n\nAccount number: " + str(self.account_number))

	def new_account_creation(self):

		print("\nCongragulations on your new account! Below is the info:\nUsername: " + self.user_name + "\nEmail: " + self.email + "\nAccount type: " + self.account_type + 
			"\nYour account balance is:" + str(self.balance) +"\nAccount number: " + str(self.account_number) + " <--- Do NOT forget this number")

	def Deposit(self):
		

		deposit = int(input("\nHow much would you like to deposit?: "))
		self.balance += deposit 

	
	def withdraw(self,withdraw):

		self.balance -= withdraw

		

		



		

		

			

	

	





















