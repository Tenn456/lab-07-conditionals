move = input("Does it move? (yes/no): ")
if move == "yes":
	should = input("Should it? (yes/no): ")
	if should == "yes":
		print("No problem.")
	elif should == "no":
		print("Then use duct tape!!!")
	else:
		print("Answer my question! You didn't type yes or no.")
elif move == "no":
	should = input("Should it? (yes/no): ")
	if should == "yes":
		print("Then use WD-40!!!")
	elif should == "no":
		print("No problem.")
	else:
		print("Answer my question! You didn't type yes or no.")
else:
	print("Answer my question! You didn't type yes or no.")