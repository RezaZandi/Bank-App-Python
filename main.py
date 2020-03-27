from Account import Account
from Transaction import Transaction
from enum import Enum
from fcp import CreateAccount




#variables and lists needed for program
new_accounts = []

#do no tneed, just put the balance of 0 straight into the factory class attribute 
#balance = 0
				
user_name = []

Transactions = []


account_number = 0




#***Functions for switch statements***
def create_user():
	global new_accounts
	global account_number

	active_create_account = False

					
	new_username = input("\n\nCreate a username:")

	  
	email = input("Write your email: ")

	account_number += 1

	print ("This is " + str(account_number))

	

# append the createaccount call straight into new_accounts.append
	new_accounts.append(CreateAccount(new_username,email, int(input('Choose 1 for Checkings or 2 for Savings:  ')), 0, account_number))
	new_accounts[(account_number-1)].new_account_creation()

	

	main()

				
def Deposit():

	global account_number

	account_search = False

	access_account = int(input("\nEnter your account number Deposit: "))


			#accounts
	for i in new_accounts:

		if access_account == i.account_number:

			i.print_balance()
			old_balance = i.balance
			i.Deposit()

			i.new_balance()

			#Creating transaction object and Storing info in transaction list
			type_of_transaction = 'Deposit'

			
			new_balance = i.balance

			
			#vert important, uses the current account number rather than the global account number for transaction object 
			account_number = access_account

			
			

			new_transaction = Transaction(account_number,type_of_transaction,old_balance,new_balance)

			Transactions.append(new_transaction)

			


			account_search = True





	if account_search == False:

		print ("\nThe number you entered did not match an account number on file. Please return to main console and try again. ")

		main()



def account_withdrawal():

	global account_number

	account_search_withdrawal = False

	access_account = int(input("\nEnter your account number to view your balance: "))
	
	for i in new_accounts:
		
		if access_account == i.account_number:
				i.print_balance()
				#the balance before withdrawal
				old_balance = i.balance



		
				withdraw = int(input("Choose how much you want to withdraw: "))
				if i.balance >= withdraw:
					
					i.withdraw(withdraw)
					i.new_balance()

					#code for transaction object, old_balance is above
					type_of_transaction = 'Withdrawal'
					new_balance = i.balance

					#uses current account number rather than global account number
					account_number = access_account
					

					
					
					
					new_transaction = Transaction(account_number,type_of_transaction,old_balance,new_balance)
					Transactions.append(new_transaction)
					account_search_withdrawal = True
					
					#helper code to print and make sure objects are being appended. Disregard. 
					#for i in Transactions:
						#if account_number == i.account_number:
							#i.to_string()



				else:
					print("\n\n Not enough funds. Go Deposit some money first!")
					account_search_withdrawal = True
					main()


				#takes you back to main console
	if account_search_withdrawal == False:
				print("\nThe number you entered did not match an account number on file. Please re-enter withdrawal mode and try again.")
				main()


def transaction_history():
				###This is where I build the transaction info 
				
		Transaction_history_search = False

		access_account = int(input("\nEnter you account number to view your Transaction History: "))

		
		for i in new_accounts:

			if access_account == i.account_number:

				
				
				for i in Transactions:
					
					if access_account == i.account_number:
						i.to_string()

					Transaction_history_search = True


		if Transaction_history_search == False:
				print("\nThe number you entered did not match an account number on file. Please return to main console and try again.")
				main()


def view_account_balance():

		account_search_balance = False

		access_account = int(input("Enter your account number to view your balance: "))

		for i in new_accounts:
			if i.account_number == access_account:
				i.print_balance()
				account_search_balance = True



		if account_search_balance == False:
				print("\nThat account does not exist. Please re-enter option 5 and try again.")
				main()


def account_info():

	access_account_search = False

	access_account = int(input("Enter your account number to access your account: "))
	for i in new_accounts:
		if i.account_number == access_account:
			i.to_string()
			access_account_search = True




	if access_account_search == False:
		print("\nThat account does not exist. Please re-enter option 6 and try again.")	
		main()

def exit():
	exit()
				














#main program
def main():

	active_create_account = True

	main_console = ("\nSelect an option to begin:")
	main_console += ("\n\nEnter 1 to Create a new account")
	main_console += ('\nEnter 2 to Deposit')
	main_console += ('\nEnter 3 to Withdraw')
	main_console += ('\nEnter 4 for Transactions')
	main_console += ('\nEnter 5 to view Balance')
	main_console += ('\nEnter 6 to view Account Info')
	main_console += ('\nEnter 7 to exit')
	main_console += ('\n\nWhat would you like to do?:')









	while True:

		user_option = int(input(main_console))

	

		#Switch statement
		switcher = {

	
			
			1:

				create_user,

			
			
			2:

				Deposit,


			
			3:

				account_withdrawal,

						



			4:
				
				transaction_history,



			
			5:

				view_account_balance,



		
			6:
				
				account_info,
				

			7:

				exit

			}

		switcher.get(user_option,None)()
							





	


if __name__== "__main__":
	main()


	




					
			
					




