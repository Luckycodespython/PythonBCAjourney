#       Bill Splitter
def totalbill(a, b = 10) :
	return(a + ((a*b)/100)) 
	 
def perperson(c) :
	return(total/c)

a = float(input("Ordered food Bill : $ "))
b = input("Tip (Optional) : ")
c = int(input("Number of people : "))


if b == "" :
	total = totalbill(a)
	print("Your Total Bill is : $", total)
	print("$" ,perperson(c) ,"for each")

else :
	total = totalbill(a,int(b))
	print("Your Total Bill is : $", total)
	print("$" ,perperson(c) ,"for each")		


 













