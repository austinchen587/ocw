low  = 0.0
high = 10.0
epslion = 1e-6
x = (low + high)/2
exp = x**3 - 27
time = 0

while abs(exp) >= epslion:
    if exp < 0:
        low = x
    else:
        high = x

    x = (low + high)/2
    exp = x**3 - 27

    time += 1

print(f"x = {round(x,6)}")
print(f"times = {time}")
