# check for leap year
year = int(input("Enter a year to check for leap year :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Its a leap year")
else:
    print("Its not a leap year")