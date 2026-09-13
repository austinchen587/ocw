initial_deposit = float(input("Enter the initial deposit: "))

cost_your_dream_home = 800000
portion_down_payment = .25
portion_payment = cost_your_dream_home * portion_down_payment

epsilon = 100
steps = 0

if initial_deposit >= portion_payment - epsilon:
    print("Best saving rate : 0.0")
elif initial_deposit * ((1+1.0/12)**36) < (portion_payment -epsilon):
    print("Best saving rate : None")
else:
    r = 0.5

    while True:
        f_r = initial_deposit * ((1+r/12)**36) - portion_payment

        if abs(f_r) <= epsilon:
            break

        f_prime_r = 3 * initial_deposit * ((1+r/12)**35)

        r = r - f_r/f_prime_r
        steps += 1

    print(f"Best saving rate : {r}")
    print(f"Steps in Newton's method : {steps}")