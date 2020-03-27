from enum import Enum







"""
class Shake(Enum):

	vanilla = 7
	chocolate = 9
	cookies = 4
	mint = 3



account_type_list = []
while True:

	account_type1 = int(input("Enter number: "))

	for s in Shake:

		
	     
		if account_type1 == s.value:
		    	account_type_list.append(s.name)
		    	print(account_type_list)
		    	print("this is working in if statement")


		
	print("this is working outside if statement")
			
"""




class Accounts(Enum):

	Checking = 1
	Savings = 2


account_type_list = []
while True:

	account_type2 = int(input("Choose 1 for checking and 2 for savings:  "))
	
	
	for account in Accounts:

		if account_type2 == account.value:
			account_type_list.append(account.name)
			print(account_type_list)
			



