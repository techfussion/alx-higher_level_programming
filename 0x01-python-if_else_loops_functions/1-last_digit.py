#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = int(str(number)[-1])
msg = ''

if number < 0:
    msg = f'Last digit of number is -'
else:
    msg = f'Last digit of number is '

if last_digit > 5:
    print(f'{msg}{last_digit} and is greater that 5')
elif last_digit == 0:
    print(f'{msg}{last_digit} and is 0')
elif last_digit < 6 and last_digit != 0:
    print(f'{msg}{last_digit} and is less than 6 and not 0')
