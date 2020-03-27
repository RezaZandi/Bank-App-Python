from Account import Account 
from Transaction import Transaction


#BLANK CLASS TEMPLATE
Bank_Accounts = type("Bank_Accounts",(object,),{})


#LIST OF NEW ACCOUNTS
new_accounts = []


#LIST OF NEW TRANSACTIONS
Transaction_list = []


#TEMPORARY VARIABLES 
user_name = "Josh"
email = "Josh@gmail.com"
account_type = "Debit"
balance = 0
account_number = 1


#BANK ACCOUNT CREATION AND VARIABLE
#Checking_Accounts = type("Checking_Accounts",(Bank_Accounts,),{"x" : Account(user_name,email,1,balance,account_number)})
#Savings_Accounts = type("Savings_Accounts",(Bank_Accounts,),{"x" : Account(user_name,email,2,balance,account_number)})

@classmethod
def CreateAccount(self,user_name,email,num,balance,account_number):
	if (num == 1): return CreateCheckingAccount(user_name,email,1,balance,account_number)
	if (num == 2): return CreateSavingsAccount(user_name,email,2,balance,account_number)
@classmethod
def CreateCheckingAccount(self,user_name,email,1,balance,account_number):
	return Account(user_name,email,1,balance,account_number)

def CreateSavingsAccount(self,user_name,email,1,balance,account_number):
	return Account(user_name,email,2,balance,account_number)


temp = CreatAccount(user_name,email, int(input('Choose 1 for Checkings or 2 for Savings:  ')),balance,account_number)

#ADDS TEMPORARY VARIABLES TO LISTS
new_accounts.append(Checking_Accounts)


#TEMPORARY VARIABLES 
account_number = 2
type_of_transaction = "Deposit"
old_balance = 0
new_balance = 100


#NEW TRANSATION CREATION AND VARIABLE 
Transactions_History = type("Transactions_History",(Bank_Accounts,),{"z": Transaction(account_number,type_of_transaction,old_balance,new_balance)})


#ADDS TEMPORARY VARIABLES TO LISTS
Transaction_list.append(Transactions_History)


#PRINT VARIABLES
for i in new_accounts:
	i.x.to_string()

for i in Transaction_list:
	i.z.to_string()











