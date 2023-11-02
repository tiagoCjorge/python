from datetime import datetime, timedelta



now = datetime.now()


print("Enter your date of birth (DD-MM-YYYY):")
dob_input = input()


birthday = datetime.strptime(dob_input, "%d-%m-%Y")


difference = now - birthday

age_in_years = difference.days // 365

print("You are ",age_in_years," years old.")
print("Tens ",difference.days,' dias')