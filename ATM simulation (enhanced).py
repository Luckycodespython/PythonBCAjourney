pin = 8989
attempts = 0
balance = 15000

while True :
	
	x = int(input("Enter the PIN : "))
	
	if x == pin :
		print("Correct pin entered , Welcome !!")
		print("\n","Choose : ")
		print("1. Check balance")
		print("2. Withdraw money")
		print("3. Exit")
		
		x = int(input("Enter : "))
		
		match x :
			case 1 :
				print("Balance : " ,balance)
				
			case 2 :
				amount = int(input("Enter the amount : "))
				balance = balance - amount
				if balance > amount :
					print(amount ,"debited. Remaining :" ,balance)
				else :
					print("Insufficient balance")
				
			case 3 :
				print("Have a nice day")
				break 	 	 	 
	else :
		attempts = attempts + 1
		
		print("wrong pin entered, remaining :" , (3 - attempts) ,"attempts")
		
		
		if attempts == 3 :
			print("you are out of attempts , try again after 24 hours")
			break
			 	 	 	 		 	 	 	 