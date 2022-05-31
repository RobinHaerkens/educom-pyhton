hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = (mins + (dura % 60)) % 60
total_hours = (hour + ((mins + dura) // 60))

# Write your code here.
print(24% (total_hours + (dura // 60)) % 24, total_mins)

