def sum_of_digits(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total

number = input("Enter a number: ")
result = sum_of_digits(number)
print("The sum of the digits is:", result)


def sum_of_digits_four_digit(number):
    new_num1 = number % 10
    new_num2 = (number // 10) % 10
    new_num3 = (number // 100) % 10
    new_num4 = (number // 1000) % 10
    total = new_num1 + new_num2 + new_num3 + new_num4
    return total

a = int(input("Enter a four-digit number: "))
result = sum_of_digits_four_digit(a)
print("The sum of the digits is:", result)

# Recursive

def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sum_of_digits(num // 10)
    
number = 4567
result = sum_of_digits(number)

print(result)