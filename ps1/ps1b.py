yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
r = .05
portion_down_payment = .25
months = 0
amount_saved = 0

portion_payment = portion_down_payment * cost_of_dream_home

while amount_saved < portion_payment:
    

    amount_saved = yearly_salary*portion_saved/12 + (1+r/12)*amount_saved

    months += 1

    if months % 6 == 0:
            yearly_salary = (1+semi_annual_raise)*yearly_salary

print(f"Number of months: {months}")




