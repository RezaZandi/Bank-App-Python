
import datetime





class Transaction():



	def __init__(self,account_number,type_of_transaction,old_balance,new_balance,date = datetime.datetime.now()):
		
			self.account_number = account_number
			self.type_of_transaction = type_of_transaction
			self.old_balance = old_balance
			self.new_balance = new_balance
			self.date = datetime.datetime.now()
		

	
	

	def to_string(self):

		print("\nThe account number is: " + str(self.account_number) + "\nThe type of transaction is: " + self.type_of_transaction + "\nThe old balance was: " + str(self.old_balance) + "\nThe new balance is: " + str(self.new_balance) + "\nThe date of the transaction was: " + str(self.date))

	def print_date(self):

			print(str(self.date))






		


















