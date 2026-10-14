print("--- Saur Energy Solution - Bill Calculator ---")
units = int(input("Enter Units Used: "))
rate = 8
monthly_bill = units * rate
yearly_bill = monthly_bill * 12
saving_per_year = yearly_bill * 0.90

print("\n----- Your Report -----")
print(f"Monthly Bill: Rs {monthly_bill}")
print(f"Yearly Bill: Rs {yearly_bill}")
print(f"Yearly Saving with 3kW Solar: Rs {saving_per_year}")
print(f"25 Years Total Saving: Rs {saving_per_year * 25}")
print("\nContact: Saur Energy Solution, Nashik")