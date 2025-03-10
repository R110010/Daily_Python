# check for weekend
import datetime
today = datetime.datetime.today().strftime("%A")

if today == "Saturday" or today == "Sunday":
    print("its a Weekend")
else:
    print("its a Weekday")
