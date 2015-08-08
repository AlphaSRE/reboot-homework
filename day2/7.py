money = 10000
year=0
while True:
    if money < 20000:
        money = money * 1.0325
        year += 1
    else:
        break

print year
print money
