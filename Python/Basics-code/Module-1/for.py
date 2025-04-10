monthly_expense = [2300, 2350, 2600, 2130, 2190]

total = 0
for item in monthly_expense:
    total += item
print("Total expenses: ", total)

yearly_expense = [2500, 2600, 2400, 2800, 2900, 2750, 3000, 2900, 3100, 2600, 3000, 3250]

total_yearly_expense = 0
for item in yearly_expense:
    total_yearly_expense += item
print("Total yearly expense: ", total_yearly_expense)

# range function
# range gives you range of numbers from 0 to n-1
for i in range (0, 10):
    print(i) # prints 0 to 9
    
for i in range (1, 10):
    print(i*i) 
    
for i in range (len(monthly_expense)):
    print('Month:', i+1, 'Expense:', monthly_expense[i])
    total += monthly_expense[i]
print('Total expense:', total)