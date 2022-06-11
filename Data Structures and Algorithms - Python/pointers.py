
num1 = 11

num2 = num1 

print('before num2 value is updated:')
print(f'num1 = {num1}')
print(f'num2 = {num2}')

# they are pointing to the same location in memory
print(f'\nnum1 points to: {id(num1)}')
print(f'num2 points to: {id(num2)}')  

num2 = 22

print('\nbefore num2 value is updated:')
print(f'num1 = {num1}')
print(f'num2 = {num2}')

# they are now pointing to different locations in memory
print(f'\nnum1 points to: {id(num1)}')
print(f'num2 points to: {id(num2)}') 

'''
explanation:
this happens because integers have fixed locations in memory
we can change the value of num1 to a different number, and it
will point to a different location in memory

however, this is not the case for dictionaries, dictionaries will be
removed from memory if not referenced by any variable (garbage colection)
'''

