exp = [3402,2520,2100,2980]
total = 0

for i in range(len(exp)):
    print("Month:", (i+1), 'Expense:', exp[i])
    total = total + exp[i]

print("Total Expenses :", total)