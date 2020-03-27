#old one

from Account import Account
from Transaction import Transaction 









#give user options
#get user to pick option (create new account, withdraw, deposit, show accounts)









new_accounts = []
balance = 0
				
user_name = []

Transactions = []


account_number = 0

def main():

	active = True
	active_create_account = True

	main_console = ("\nSelect an option to begin:")
	main_console += ("\nEnter 1 to Create a new account")
	main_console += ('\nEnter 2 to Deposit')
	main_console += ('\nEnter 3 to Withdraw')
	main_console += ('\nEnter 4 for Transactions')
	main_console += ('\nEnter 5 to view Balance')
	main_console += ('\nEnter 6 to view Account Info')
	main_console += ('\nEnter 7 to exit')
	main_console += ('\n\nWhat would you like to do?:')

	while active:

		user_option = int(input(main_console))

		#Exit

		if user_option == 7:
			exit()

		#Create a new username
		
		if user_option == 1 :

			
			global new_accounts
			global account_number 
	
			active_create_account = True

							
			new_username = input("\n\nCreate a username: ")

			  
			email = input("Write your email: ")
			account_type = input('Choose an account type(Checking or Savings: ')


			account_number += 1


			new_account = Account(new_username,email,account_type,balance,account_number)

			new_accounts.append(new_account)

			for i in new_accounts:
				if account_number == i.account_number:
					i.new_account_creation()

			print("this is the end")
					

		#Deposit 
		if user_option == 2:

			active = True
			while active:

				
				
				for i in new_accounts:
					access_account = int(input("\nEnter your account number Deposit: "))	
					
			
					if access_account == i.account_number:
							i.print_balance()
							old_balance = i.balance
							

							if access_account == i.account_number:
								i.Deposit()
								i.new_balance()
								
								#Creating transaction object and Storing info in transaction list
								

								type_of_transaction = 'Deposit'

								new_balance = i.balance
								


								account_number = i.account_number
								#i think it needs to be in reverse 


								new_transaction = Transaction(account_number,type_of_transaction,old_balance,new_balance)

								Transactions.append(new_transaction)


						
							else:
								continue
						

							#helper code to print Transc objects to make there they are being appended. Disregard
							"""for i in Transactions:
								if account_number == i.account_number:
									i.to_string()"""



						


					else:
							try_again_or_quit = input("\nThe number you entered did not match an account_number on file. Please type 'continue' or type 'back' to return to main console: ")

							if try_again_or_quit == 'back':
								active = False
								main()
							else:
								continue 

					exit_or_deposit_again = input("\nType 'continue' to deposit again or 'back' to return to the main console: ")

					if exit_or_deposit_again == 'back':
							active = False
							main()

					else:
						continue 


			#withdraw
		if user_option == 3:

			active = True
			while active:

				for i in new_accounts:
					access_account = int(input("\nEnter your account number to view your balance: "))
					
					
					if i.account_number == access_account:
							i.print_balance()
							#the balance before withdrawal
							old_balance = i.balance


					
						
							withdraw = int(input("Choose how much you want to withdraw: "))
							if i.balance >= withdraw:
								i.withdraw(withdraw)
								i.new_balance()

								#code for transaction object, old_balance is above
								type_of_transaction = 'withdrawal'
								new_balance = i.balance
								account_number = i.account_number
								new_transaction = Transaction(account_number,type_of_transaction,old_balance,new_balance)
								Transactions.append(new_transaction)

								
								#helper code to print and make sure objects are being appended. Disregard. 
								#for i in Transactions:
									#if account_number == i.account_number:
										#i.to_string()






							else:
								print("\n\n ***Not enough funds. Go Deposit some money first you broke niggah")
								active = False
								main()


					else:
							try_again_or_quit = input("\nThe number you entered did not match an account_number on file. Please type 'continue' or type 'back' to return to main console: ")

							if try_again_or_quit == 'back':
								active = False
								main()
							else:
									continue 

					exit_or_withdraw_again = input("type 'continue' to deposit again or 'back' to return to the main console: ")

					if exit_or_withdraw_again== 'back':
							active = False
							main()

					else:
						continue



		if user_option == 4:
			

			###This is where I build the transaction info 
			active = True
			while active:


				
				for i in new_accounts:

					access_account = int(input("\nEnter you account number to view your Transaction History: "))

				
					if i.account_number == access_account:
						for i in Transactions:
							if i.account_number == access_account:
								i.to_string()


				
					exit_or_withdraw_again = input("type 'continue' to deposit again or 'back' to return to the main console: ")

					if exit_or_withdraw_again== 'back':
							active = False
							main()

					else:
						continue





		#check balance
		if user_option == 5:

			active = True
			while active:

				access_account = int(input("Enter your account number to view your balance: "))

				for i in new_accounts:
					if i.account_number == access_account:
						i.print_balance()

				return_or_check_other_account = input("type 'continue' to search another account or 'back' to return to the main console: ")

				if return_or_check_other_account == 'back':
							active = False
							main()
				else:
						continue 



		#View account info
		if user_option == 6:
			

			active = True
			while active:


				access_account = int(input("Enter your account number to access your account: "))

				for i in new_accounts:
					if i.account_number == access_account:
						i.to_string()



				return_or_check_other_account = input("type 'continue' to search another account or 'back' to return to the main console: ")

				if return_or_check_other_account == 'back':
						active = False
						main()
				else:
					continue 


if __name__== "__main__":
	main()


	

