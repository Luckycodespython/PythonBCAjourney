#   || QUIZ COMPEITITION ||
#       Participant List 

list = ["Jamshed","Aditya","Ishant","Harsh","Suresh","Dhruv","Bhanu","Arnav","Yuvraj","Lucky"]
print(list)	

print("\nEdit list : 1.Add | 2.Remove | 3.Urgent add | 4.Sort | 5.Get final list ") 	
	
while True :
	choose = int(input("Choose any one operation : "))
		
	if choose == 1 :
		add_new = input("Enter participant name : ").capitalize()
		list.append(add_new)
		print(add_new, "Successfully added to the list")	
	
	elif choose == 2 :
		remove_old = input("Enter the participant name : ").capitalize()
		if remove_old in list :
			list.remove(remove_old)
			print(remove_old, "Successfully removed from the list")
		
		else :
			print(remove_old, "is not in the list") 		
	
	elif choose == 3 :
		urgent_add = input("Enter the participant name : ").capitalize()
		list.insert(0,urgent_add)
		print(urgent_add, "Successfully added to the list")
	
	elif choose == 4 :
		list.sort()
		print("List sorted successfully")
	
	elif choose == 5 :
		for i in list :
			print("\n",">", i)
		break	
	
	else :
		print("Invalid input")
			