from datetime import datetime, timedelta

#Monday
mondayin = input("Hello, Input your Monday Time In:\n")
mondayout = input("Input your Monday Time Out:\n")

#Tuesday
tuesdayin = input("Input your Tuesday Time In:\n")
tuesdayout = input("Input your Tuesday Time Out:\n")


print("Monday In/Out:" + mondayin + " / " + mondayout + "\n" + "Tuesday In/Out:" + tuesdayin + " / " + tuesdayout  )

# convert time string to datetime
m1 = datetime.strptime(mondayin, "%H:%M")
m2 = datetime.strptime(mondayout, "%H:%M") + timedelta(hours=12)

t1 = datetime.strptime(tuesdayin, "%H:%M")
t2 = datetime.strptime(tuesdayout, "%H:%M") + timedelta(hours=12)

# get difference
delta = (m2 - m1) + (t2 - t1)

#print(f"Time difference is {delta.total_seconds()} seconds")
deltahour = delta.total_seconds() //3600
deltahourleft = 28.5 - deltahour

print(f"You have clocked in a total of {deltahour} hours from Mon-Thur and {deltahourleft} hours left for Friday")

#Friday
fridayin = input("Input your Friday Time In:\n")

f1 = datetime.strptime(fridayin, "%H:%M") + timedelta(hours=deltahourleft)

#print(f1)

f2 = datetime(1900, 1, 1, 15, 00, 00)

if f1 < f2:
    print("Yes, you can go back at 3PM")
else:
    print("You can only go back at")
    print(f1.strftime('%H:%M'))

exit = input("You can exit the program now:\n")


