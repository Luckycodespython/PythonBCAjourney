# If-else conditional statements along with Nested if statements

#High Waves Club Security Systems

name = input("Enter your Full name : ")
age = int(input("Enter your Age : "))
 
if age >= 18 :
	ID = input("Do you have Identity card(YES/NO) ? : ").upper()
	
	if ID == "YES" :
	   print("\n--------Welcome! To our club --------") 
	
	elif ID == "NO" :
	   print("\n----- You are not allowed to enter without ID card -----: ")	
else :	         
	print("\n-- You should be 18+ first,This time you are not allowed --")  
	
	
	
	