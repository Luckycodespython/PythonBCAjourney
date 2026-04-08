#      || ATM Machine ||  

balance  = 5000
pin = 9090

checkpin = int(input("Enter your pin : "))

if checkpin == pin :
	
	print("\n1. Check Balance")
	print("2. Withraw money")
	print("3. Exit")
	
	x = 0
	while x != 3 :
		
		x = int(input("\nChoose any one option : ")) 
		
		match x :
			
			case 1 :
				print(balance)
			case 2 :
				amount = int(input("Enter the amount : "))
				if amount <= balance :
				    balance = balance - amount	
				    print(amount ,"debited. Remaining bal. is ",balance)
				else :
					print("Insufficient bal.")  
			case 3 :
				print("Have a nice day")
						
else :
	print("Wrong PIN entered")













