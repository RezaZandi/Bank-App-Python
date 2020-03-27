
"""
def main():
	print("hi")
	


		
	main_console = ("\nSelect an option to begin:")
	main_console += ("\nEnter 0 to Create a new account")
	main_console += ('\nEnter 1 to Deposit')
	main_console += ('\nEnter 2 to Withdraw')
	main_console += ('\n What would you like to do?:  ')
	



	while True:

		user_option = int(input(main_console))
"""

def action_1():
	print("action1")

def action_2():
	print("action2")

def action_3():
	print("i'm happy with option 3")
def unknown_action():
	print("unknown")

main_console = ("choose a number ")

number_choice = int(input("choose a number:  "))







switcher = {


			1:   
		       action_1,
		    2:
		       action_2,
		    3:
		   	   action_3
		       
		}
switcher.get(number_choice,unknown_action)()


