from Account import Account 
from Transaction import Transaction


#BLANK CLASS TEMPLATE





def CreateAccount(user_name,email,account_type,balance,account_number):
			
			
			if (account_type == 1): return CreateCheckingAccount(user_name,email,1,balance,account_number)
			if (account_type == 2): return CreateSavingsAccount(user_name,email,2,balance,account_number)
			else:
			 return CreatAccount(user_name,email, int(input('Choose 1 for Checkings or 2 for Savings:  ')),balance,account_number)


def CreateCheckingAccount(user_name,email,account_type,balance,account_number):
			return Account(user_name, email,'Checking',balance,account_number)


def CreateSavingsAccount(user_name,email,account_type,balance,account_number):
			return Account(user_name, email,'Savings',balance,account_number)


#temp = CreatAccount(user_name,email, int(input('Choose 1 for Checkings or 2 for Savings:  ')),balance,account_number)

#-------- Below is the old code I took from my maincode that has an enum, input for enum, then gives it a checking or savings
#and then increments , and then creates an object class

"""
	#Account type enum-------------
	class Account_type(Enum):


		Checking = 1
		Savings = 2
	

	account_type_ask = int(input('Choose 1 for Checkings or 2 for Savings:  '))


	account_type = ''

	for account in Account_type:

		if account_type_ask == account.value:
			account_type = account.name
			print(account_type)

	

	end of enum for account type------------

	account_number +=1
	print(account_number)


	new_account = Account(new_username,email,account_type,balance,account_number)
"""



