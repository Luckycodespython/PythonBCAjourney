#------------- LOTTERY , LOTTERY , LOTTERY ------------------
#                     Try your luck

# Currently, this program expects an integer input. 
# Handling empty inputs or strings will be added after learning 'Try-Except' or 'String Methods'.
a = int(input("Choose a number from between 1 to 10 : "))

match a:
	
	case 7 :
		print("--- CONGRATULATIONS !!! YOU WIN ---".center(100))
		
	case _ if a > 10 :
		print("--- You have to choose from 1 to 10 ---".center(100))
		
	case _ :
		print("--- Better Luck Next Time ---".center(100))
				 				 