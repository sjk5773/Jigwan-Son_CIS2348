current_month = int(input("Enter the current month: "))
current_date = int(input("Enter the current date: "))
current_year = int(input("Enter the current year: "))
month_of_birth = int(input("Enter your month of birth: "))
date_of_birth = int(input("Enter your date of birth: "))
year_of_birth = int(input("Enter your year of birth: "))
year = current_year-year_of_birth

print("\nBirthday Calculator")
print("Current date")
print("Month:", current_month)
print("Date:", current_date)
print("Year:", current_year)

print("Birthday")
print("Month:", month_of_birth)
print("Day:", date_of_birth)
print("Year:", year_of_birth)
if current_month == month_of_birth and current_date == date_of_birth:
    print("Happy Birthday!")
print("You are", year, "years old.")
