tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

total = 0
for item in tom_exp_list:
    total = total + item
print("Tom's total expenses: ", total)

total = 0
for item in joe_exp_list:
    total = total + item
print("Joe's total expenses: ", total)

# now using function
print("Using Function:")

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total +item
    return total

tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's Total Expenses: ", toms_total)
print("Joe's Total Expenses: ", joes_total)


def sum(a,b):
    total = a + b
    # print("Sum :", total) #inside function 
    return total
print("Sum :",sum(52,45)) #outside function
