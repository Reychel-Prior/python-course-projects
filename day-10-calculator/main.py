def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = int(input("Type the first number: "))
print("+\n-\n*\n/")
user_choice = input("Pick your operation: ")
second_number = int(input("Type the second number: "))

result = operations[user_choice](first_number, second_number)
print(f"Here's your operation: {first_number} {user_choice} {second_number} = {result}")
