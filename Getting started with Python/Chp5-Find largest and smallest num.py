# 5.2 Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. Once 'done' is entered, print out the 
# largest and smallest of the numbers. If the user enters anything other than a 
# valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest=None
smallest=None
while True:
    num=input('Enter numbers:')

    if num=='done':
        break

    try:
        val=int(num)
    except:
        print('Invalid number')
        continue

    if largest is None or val > largest:
        largest=val
    if smallest is None or val < smallest:
        smallest=val

print('Largest is',largest)
print('Smallest is',smallest)
