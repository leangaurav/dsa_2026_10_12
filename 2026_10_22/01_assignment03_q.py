sec = int(input("enter time in seconds:"))

# sec = 3620 min=
min = (sec//60) % 60
hour = (sec//(60*60)) % 24
day = (sec//(24*60*60))
sec = sec%60

# # no. of sec in a day = 60*60*24
# day = sec//(60*60*24)
# # no. of sec in a hour = 60*60
# hour = sec//(60*60) % 24
# # no. of sec in a min = 60
# min = sec//60 % 60
# sec = sec % 60


print(f"{day} days {hour}hours {min} minutes {sec}seconds")