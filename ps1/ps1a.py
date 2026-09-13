year_salary = float(input("Enter your yearly salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

cost_of_dream_home = float(input("Enter the cost of your dream home:"))

portion_down_payment = .25

amount_saved = 0.0
months = 0

r = .05

while amount_saved <= (cost_of_dream_home * portion_down_payment):
    amount_saved = (year_salary * portion_saved)/12 + amount_saved * (r/12 + 1)
    months += 1


print(f"Number of months: {months}")
