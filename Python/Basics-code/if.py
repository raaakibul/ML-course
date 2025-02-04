indian = ['samosa', 'daal', 'naan']
chinese = ['egg role', 'pot sticker', 'fried rice']
italian = ['pizza', 'pasta', 'risotto']

dish = input("Enter a dish name: ")

if dish in indian:
    print("Indian dish")
elif dish in chinese:
    print("Chinese dish")
elif dish in italian:
    print("Italian dish")
else:
    print("I don't know which cuisine is this")
    