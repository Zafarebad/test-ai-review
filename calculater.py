# Simple calculator - has a few intentional issues for AI review to catch

def add(a, b):
    return a + b

def divide(a, b):
    return a / b   # bug: no check for b == 0

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)   # bug: crashes if list is empty

password = "admin123"   # bug: hardcoded secret, bad practice

def main():
    print(add(5, 3))
    print(divide(10, 0))

main()

# testing n8n webhook

#hi