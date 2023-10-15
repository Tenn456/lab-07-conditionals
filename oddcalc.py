firstnum = input("Give me a number: ")
secondnum = input("Okay, give me another number: ")
operation = input("And what operation do you want? (mul/div/mod): ")
answer = 0

if operation == "mul":
	answer = int(firstnum) * int(secondnum)
elif operation == "div":
	answer = int(firstnum) / int(secondnum)
elif operation == "mod":
	answer = int(firstnum) % int(secondnum)
else:
	answer = "INVALID OPERATION"

print(answer)