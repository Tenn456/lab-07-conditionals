time = int(input("What hour is it? (Military Time 0-23): "))

if time < 5:
	print("It’s early. You should be sleeping!")
elif time >= 5 and time < 7:
	print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif time >= 7 and time < 9:
	print("Time to go to work.")
elif time >= 9 and time < 12:
	print("You should be working!")
elif time >= 12 and time <= 13:
	print("Take your lunch break!")
elif time > 13 and time <= 17:
	print("Do you feel that afternoon lull?")
elif time > 17 and time <= 19:
	print("Time to hit the gym…")
elif time > 19 and time <= 21:
	print("Gotta eat that dinner.")
elif time > 21 and time <= 23:
	print("Get that SLEEP. And REPEAT!")
else:
	print("You didn’t type an acceptable value! (0-23)")