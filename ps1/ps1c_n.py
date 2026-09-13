x = (0+10)/2
epslion = 10**(-6)
step = 0



while abs(x**3 - 27) >= epslion:
    x = x - (x**3 - 27)/(3*x**2)

    step += 1

print(f"x = {round(x,6)}")
print(f"times = {step}")


