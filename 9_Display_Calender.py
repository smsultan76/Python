import calendar
def display_month(year, month):
    print(calendar.month(year, month))
def display_year(year):
    print(calendar.calendar(year))


print("Choose the option: \n 1. Display Month \n 2. Display Year")
option = int(input())
if option == 1:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    display_month(year, month)
elif option == 2:
    year = int(input("Enter the year: "))
    display_year(year)
else:
    print("Invalid Option")