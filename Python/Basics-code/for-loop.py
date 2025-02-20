# for loop
exp = [3402,2520,2100,2980]
total = 0

for i in range(len(exp)):
    print("Month:", (i+1), 'Expense:', exp[i])
    total = total + exp[i]

print("Total Expenses :", total)

# break
key_location = "chair"
locations = ['garage', 'living room', 'chair', 'closet']

for i in locations:
    if i ==key_location:
        print("Key is found in", i)
        break
    else:
        print("Key is not found in ", i)


# Continue
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)

# while loop
i = 1
while i<=5:
    print(i)
    i = i+1