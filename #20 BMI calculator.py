#   ||	BMI calculator    ||
def getBMI(a , b) :
	return(a / (b**2))
	
print("Body Mass Index(BMI) Calculator".center(50))

while True :
	enter = input("Get my BMI (yes/no) : ").lower() 
	
	if enter == "yes" :
		a = float(input("Enter your Weight(in Kg) : "))
		b = float(input("Enter your Height(in m) : "))
		
		x = getBMI(a,b) 
		
		if x < 18.5 :
			print("\n Underweight")
				
		elif 18.5 <= x <= 24.9 :
			print("\n Normalweight")
			
		elif 25 <= x <= 29.9 :
			print(" \n Overweight")
			
		elif x >= 30 :
			print(" \n Obesity")	
			
	else :
		break
	
	
	
	