# -------- FOR LOOP ------------
#     |•| LOTTERY 2.0 |•|
# Now more than one player can try their luck 

total = int(input(" How many are here to try their LUCK : "))

for i in range(total) :
	
	x = int(input("\n Choose a number from between 1 to 10 : "))
	
	match x:
		
		case 4 :
			 print("\n" + "|| CONGRATS !! YOU WIN || ".center(50))
		
		case _ if x > 10 :
			 print("\n" + "|| Invalid number entered || ".center(50))
		
		case _ :
			 print("\n" + "|| BETTER LUCK NEXT TIME || ".center(50))	 	 
			 